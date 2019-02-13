# Standard
import os
import ROOT

# RootTools
from RootTools.core.standard                     import *

# User specific
import TTGammaEFT.Tools.user as user

def get_parser():
    ''' Argument parser for post-processing module.
    '''
    import argparse
    argParser = argparse.ArgumentParser(description = "Argument parser for nanoPostProcessing")
    argParser.add_argument('--file',    action='store', type=str, default='nanoPostProcessing_Summer16', help="postprocessing sh file to check")
    argParser.add_argument('--semilep', action='store_true', help="check semiLep samples?")
    return argParser

args = get_parser().parse_args()

def filterEmpty( strList ):
    return list( filter ( bool, strList ) )

def getDataDictList( filepath ):
    ''' Read postprocessing sh file and format it to dictionary
    '''
    with open( filepath, 'r' ) as f:
        ppLines = f.readlines()

    ppLines = [ line for line in ppLines if line.startswith('python') ]

    dictList = []
    for line in ppLines:
        skim   = filterEmpty( line.split("--skim ")[1].split(" ") )[0]
        year   = filterEmpty( line.split("--year ")[1].split(" ") )[0]
        dir    = filterEmpty( line.split("--processingEra ")[1].split(" ") )[0]
        sample = filterEmpty( line.split("--sample ")[1].split(" ") )[0]
        if not filterEmpty( line.split("--sample ")[1].split(" ") )[1].startswith("--") and not filterEmpty( line.split("--sample ")[1].split(" ") )[1].startswith("#SPLIT"):
            sample += "_comb"
        nFiles = filterEmpty( line.split("#SPLIT")[1].split(" ") )[0].split("\n")[0]
        dictList.append( { "skim":skim, "year":int(year), "dir":dir, "sample":sample, "nFiles":int(nFiles)} )

    return dictList

print "Now running on pp file %s" %args.file

file = os.path.expandvars( "$CMSSW_BASE/src/TTGammaEFT/postprocessing/%s.sh" % args.file )

dictList = getDataDictList( file )
year     = dictList[0]['year']
isData   = "Run" in args.file

directory = os.path.expandvars( os.path.join ( getattr( user, "data_%sdirectory%s%i"% ("data" if isData else "", "SemiLep" if args.semilep else "", year)), getattr( user, "postprocessing_%sdirectory%s%i"%("data" if isData else "", "SemiLep" if args.semilep else "", year) ) ) )
print directory
#directory = os.path.expandvars( os.path.join (user.data_directoryPrefiring, user.postprocessing_directoryPrefiring))

for ppEntry in dictList:
    print "checking sample %s" %ppEntry['sample']
    path      = os.path.join( directory, ppEntry['sample'] )
    if not os.path.isdir( path ):
        print "Sample not processed: %s" %ppEntry["sample"]
        continue
    rootFiles = [ item for item in os.listdir( path ) if item.endswith(".root") ]
    if len(rootFiles) != ppEntry['nFiles']:
        print "len root files", len(rootFiles), "len processed", ppEntry['nFiles']
        missingFiles = [ int(item.split("_")[-1].split(".root")[0]) for item in rootFiles ]
        missingFiles = list( set( range(ppEntry['nFiles']) ) - set( missingFiles ) )
        missingFiles.sort()
        missingFiles = map( str, missingFiles )
        print "Not all files of sample %s processed! Indices of missing files: %s"%(ppEntry["sample"], ', '.join(missingFiles))
#        print "No further checks on sample %s performed!" %ppEntry['sample']
#        continue
    for file in rootFiles:
        filepath = os.path.join( path, file )

        if os.path.getsize( filepath ) < 100000:
            print "filesize of %s very small: %i bytes" % (file, os.path.getsize( filepath ))
#            print "No further checks on file %s performed!" %file
#            continue
        chain    = ROOT.TChain('Events')
        chain.AddFile( filepath )
        nEntries = chain.GetEntries()
        allBranches = [item.GetName() for item in list(chain.GetListOfBranches()) if item.GetName().startswith('nMuon')]
        if not allBranches:
            print file
            print allBranches
        allBranches = [item.GetName() for item in list(chain.GetListOfBranches()) if item.GetName().startswith('nElectronTight')]
        if not allBranches:
            print file
            print allBranches
        del chain
        if nEntries < 100:
            print "Number of events in file %s lower than 100! Found %i events! Corrupt ROOT file?" %(file, nEntries)
