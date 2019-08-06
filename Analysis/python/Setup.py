#Standard import
import copy
import os

# Logging
import logging
logger = logging.getLogger(__name__)

# RootTools
from RootTools.core.standard          import *

#user specific
from TTGammaEFT.Tools.TriggerSelector import TriggerSelector
from TTGammaEFT.Tools.user            import results_directory, cache_directory
from TTGammaEFT.Tools.cutInterpreter  import cutInterpreter, zMassRange
from TTGammaEFT.Analysis.SetupHelpers import *

from Analysis.Tools.metFilters        import getFilterCut

class Setup:
    def __init__(self, year=2016, photonSelection=False, checkOnly=False):
        self.analysis_results = analysis_results
        self.zMassRange       = zMassRange
        self.prefixes         = []
        self.externalCuts     = []
        self.year = year

        #Default cuts and requirements. Those three things below are used to determine the key in the cache!
        self.parameters   = {
            "dileptonic":   default_dileptonic,
            "zWindow":      default_zWindow,
            "nJet":         default_nJet,
            "nBTag":        default_nBTag,
            "nPhoton":      default_nPhoton,
            "invertLepIso": default_invLepIso,
            "addMisIDSF":   default_addMisIDSF,
        }

#        self.puWeight = "reweightPUVUp" if self.year == 2018 else "reweightPU"
        self.sys = {"weight":"weight", "reweight":["reweightL1Prefire", "reweightPU", "reweightLeptonTightSF", "reweightLeptonTrackingTightSF", "reweightPhotonSF", "reweightPhotonElectronVetoSF", "reweightBTag_SF"], "selectionModifier":None} 

        os.environ["gammaSkim"] = str(photonSelection)
        if year == 2016 and not checkOnly:
            #define samples
            from TTGammaEFT.Samples.nanoTuples_Summer16_private_semilep_postProcessed  import TTG_priv_16, TT_pow_16, DY_LO_16, WJets_16, WG_16, ZG_16, QCD_16, GJets_16, rest_16
            from TTGammaEFT.Samples.nanoTuples_Run2016_14Dec2018_semilep_postProcessed import Run2016
            ttg         = TTG_priv_16
            tt          = TT_pow_16
            DY          = DY_LO_16
            zg          = ZG_16
            wg          = WG_16
            wjets       = WJets_16
            other       = rest_16 #other_16
            qcd         = QCD_16
            gjets       = GJets_16
            data        = Run2016

        elif year == 2017 and not checkOnly:
            #define samples
            #os.environ["gammaSkim"]="False" #always false for QCD estimate
            from TTGammaEFT.Samples.nanoTuples_Fall17_private_semilep_postProcessed    import TTG_priv_17, TT_pow_17, DY_LO_17, WJets_17, WG_17, ZG_17, QCD_17, GJets_17, rest_17
            from TTGammaEFT.Samples.nanoTuples_Run2017_14Dec2018_semilep_postProcessed import Run2017
            ttg         = TTG_priv_17
            tt          = TT_pow_17
            DY          = DY_LO_17
            zg          = ZG_17
            wg          = WG_17
            wjets       = WJets_17
            other       = rest_17 #other_17
            qcd         = QCD_17
            gjets       = GJets_17
            data        = Run2017

        elif year == 2018 and not checkOnly:
            #define samples
            #os.environ["gammaSkim"]="False" #always false for QCD estimate
            from TTGammaEFT.Samples.nanoTuples_Autumn18_private_semilep_postProcessed  import TTG_priv_18, TT_pow_18, DY_LO_18, WJets_18, WG_18, ZG_18, QCD_18, GJets_18, rest_18
            from TTGammaEFT.Samples.nanoTuples_Run2018_14Dec2018_semilep_postProcessed import Run2018
            ttg         = TTG_priv_18
            tt          = TT_pow_18
            DY          = DY_LO_18
            zg          = ZG_18
            wg          = WG_18
            wjets       = WJets_18
            other       = rest_18 #other_18
            qcd         = QCD_18
            gjets       = GJets_18
            data        = Run2018


        if checkOnly:
            self.samples = { sample:None for sample in default_sampleList }
            self.samples["Data"] = None

            self.lumi     = -1
            self.dataLumi = -1
        else:
            mc           = [ ttg, tt, DY, zg, wjets, wg, other, qcd, gjets ]
            self.samples = { sample.name:sample for sample in mc }
            self.samples["Data"] = data

            self.lumi     = data.lumi
            self.dataLumi = data.lumi # get from data samples later
        
#        dataPUHistForSignalPath = "$CMSSW_BASE/src/TTGammaEFT/Tools/data/puFastSimUncertainty/dataPU.root"
#        self.dataPUHistForSignal = getObjFromFile(os.path.expandvars(dataPUHistForSignalPath), "data")

    def prefix(self):
        return "_".join(self.prefixes+[self.preselection("MC")["prefix"]])

    def defaultCacheDir(self):
        cacheDir = os.path.join(cache_dir, self.year, "estimates")
        logger.info("Default cache dir is: %s", cacheDir)
        return cacheDir

    #Clone the setup and optinally modify the systematic variation
    def sysClone(self, sys=None, parameters=None):
        """Clone setup and change systematic if provided"""

        res            = copy.copy(self)
        res.sys        = copy.deepcopy(self.sys)
        res.parameters = copy.deepcopy(self.parameters)

        if sys:
            for k in sys.keys():
                if k=="remove":
                    for i in sys[k]:
                      res.sys["reweight"].remove(i)
                elif k=="reweight":
                    res.sys[k] = list(set(res.sys[k]+sys[k])) #Add with unique elements
                    
                    for upOrDown in ["Up","Down"]:
                        if "reweightL1Prefire"+upOrDown             in res.sys[k]: res.sys[k].remove("reweightL1Prefire")
                        if "reweightPU"+upOrDown                    in res.sys[k]: res.sys[k].remove("reweightPU")
                        if "reweightLeptonTightSF"+upOrDown         in res.sys[k]: res.sys[k].remove("reweightLeptonTightSF")
                        if "reweightLeptonTrackingTightSF"+upOrDown in res.sys[k]: res.sys[k].remove("reweightLeptonTrackingTightSF")
                        if "reweightPhotonSF"+upOrDown              in res.sys[k]: res.sys[k].remove("reweightPhotonSF")
                        if "reweightPhotonElectronVetoSF"+upOrDown  in res.sys[k]: res.sys[k].remove("reweightPhotonElectronVetoSF")
                        if 'reweightBTag_SF_b_'+upOrDown            in res.sys[k]: res.sys[k].remove('reweightBTag_SF')
                        if 'reweightBTag_SF_l_'+upOrDown            in res.sys[k]: res.sys[k].remove('reweightBTag_SF')
                else:
                    res.sys[k] = sys[k]

        if parameters:
            for k in parameters.keys():
                res.parameters[k] = parameters[k]

        return res

    def defaultParameters(self, update={} ):
        assert type(update)==type({}), "Update arguments with key arg dictionary. Got this: %r"%update
        res = copy.deepcopy(self.parameters)
        res.update(update)
        return res

    def weightString(self, dataMC, addMisIDSF=False):
        if   dataMC == "Data": return "(1)"
        elif dataMC == "MC":
            _weightString = "*".join([self.sys["weight"]] + (self.sys["reweight"] if self.sys["reweight"] else []))
            if addMisIDSF: _weightString += "+%s*(PhotonGood0_photonCat==2)*(%f-1)" %(_weightString, default_misIDSF)
            return _weightString

    def preselection(self, dataMC , channel="all"):
        """Get preselection  cutstring."""
        return self.selection(dataMC, channel = channel, **self.parameters)

    def selection(self, dataMC,
                        dileptonic=False, invertLepIso=False, addMisIDSF=False,
                        nJet=None, nBTag=None, nPhoton=None,
                        zWindow="all",
                        photonCat="all",
                        channel="all"):
        """Define full selection
           dataMC: "Data" or "MC"
           channel: all, e or mu, eetight, mumutight, SFtight
           zWindow: offZeg, onZeg, onZSFllTight or all
        """

        #Consistency checks
        assert dataMC in ["Data","MC"], "dataMC = Data or MC, got %r."%dataMC
        assert channel in allChannels, "channel must be one of "+",".join(allChannels)+". Got %r."%channel
        assert zWindow in ["offZeg", "onZeg", "onZSFllTight", "all"], "zWindow must be one of onZeg, offZeg, onZSFllTight, all. Got %r"%zWindow
        if self.sys['selectionModifier']:
#            assert self.sys['selectionModifier'] in jmeVariations+metVariations, "Don't know about systematic variation %r, take one of %s"%(self.sys['selectionModifier'], ",".join(jmeVariations+metVariations))
            assert self.sys['selectionModifier'] in jmeVariations, "Don't know about systematic variation %r, take one of %s"%(self.sys['selectionModifier'], ",".join(jmeVariations))

        # default lepton selections
        tightLepton = "nLepTight1"
        vetoLepton = "nLepVeto1"

        if invertLepIso:
            # invert leptonIso in lepton cuts
            channel += "Inv"
            zWindow += "Inv"
            tightLepton = "nInvLepTight1"
            vetoLepton = "nNoIsoLepTight1"

        if dileptonic:
#            if   channel == "e":   channel = "eetight"
#            elif channel == "mu":  channel = "mumutight"
#            elif channel == "all": channel = "SFtight"
            tightLepton = "nLepTight2-OStight"
            vetoLepton = "nLepVeto2"

        #Postfix for variables (only for MC and if we have a jme variation)
        sysStr = ""
#        metStr = ""
        if dataMC == "MC" and self.sys['selectionModifier'] in jmeVariations: sysStr = "_" + self.sys['selectionModifier']
#        if dataMC == "MC" and self.sys['selectionModifier'] in metVariations: metStr = "_" + self.sys['selectionModifier']

        res={"cuts":[], "prefixes":[]}

        #leptons or inv. iso leptons
        res["prefixes"].append( tightLepton )
        lepSel = cutInterpreter.cutString( tightLepton )
        res["cuts"].append( lepSel )
              
        #lepton channel or inv. iso lepton channel
        chStr = cutInterpreter.cutString( channel )
        res["cuts"].append(chStr)

        #lepton veto or no Iso lepton veto
        res["prefixes"].append( vetoLepton )
        chVetoStr = cutInterpreter.cutString( vetoLepton )
        res["cuts"].append( chVetoStr )

        if nJet and not (nJet[0]==0 and nJet[1]<0):
            assert nJet[0]>=0 and (nJet[1]>=nJet[0] or nJet[1]<0), "Not a good nJet selection: %r"%nJet
            njetsstr = "nJetGood"+sysStr+">="+str(nJet[0])
            prefix   = "nJet"+str(nJet[0])
            if nJet[1]>=0:
                njetsstr+= "&&"+"nJetGood"+sysStr+"<="+str(nJet[1])
                if nJet[1]!=nJet[0]: prefix+=str(nJet[1])
            else:
                prefix+="p"
            res["cuts"].append(njetsstr)
            res["prefixes"].append(prefix)

        if nBTag and not (nBTag[0]==0 and nBTag[1]<0):
            assert nBTag[0]>=0 and (nBTag[1]>=nBTag[0] or nBTag[1]<0), "Not a good nBTag selection: %r"% nBTag

            # change that after next pp
            if sysStr: nbtstr = "nBTag"+sysStr+">="+str(nBTag[0])
            else:      nbtstr = "nBTagGood"+sysStr+">="+str(nBTag[0])

            prefix = "nBTag"+str(nBTag[0])
            if nBTag[1]>=0:
                if sysStr:             nbtstr+= "&&nBTag"+sysStr+"<="+str(nBTag[1])  # change that after next pp
                else:                  nbtstr+= "&&nBTagGood"+sysStr+"<="+str(nBTag[1])  # change that after next pp
                if nBTag[1]!=nBTag[0]: prefix+=str(nBTag[1])
            else:
                prefix+="p"
            res["cuts"].append(nbtstr)
            res["prefixes"].append(prefix)

        if nPhoton and not (nPhoton[0]==0 and nPhoton[1]<0):
            assert nPhoton[0]>=0 and (nPhoton[1]>=nPhoton[0] or nPhoton[1]<0), "Not a good nPhoton selection: %r"%nPhoton
            nphotonsstr = "nPhotonGood>="+str(nPhoton[0])
            prefix   = "nPhoton"+str(nPhoton[0])
            if nPhoton[1]>=0:
                nphotonsstr+= "&&"+"nPhotonGood<="+str(nPhoton[1])
                if nPhoton[1]!=nPhoton[0]: prefix+=str(nPhoton[1])
            else:
                prefix+="p"
            res["cuts"].append(nphotonsstr)
            res["prefixes"].append(prefix)


        #Z window
        preselZWindow = cutInterpreter.cutString( zWindow )
        res["cuts"].append( preselZWindow )
        res["prefixes"].append( zWindow )

        #photon category
        photoncatCut = cutInterpreter.cutString( photonCat )
        res["cuts"].append( photoncatCut )
        res["prefixes"].append( photonCat )

        #badEEVeto
        if self.year == 2017:
#            res["prefixes"].append("BadEEJetVeto")
            badEEStr = cutInterpreter.cutString( "BadEEJetVeto" )
            res["cuts"].append( badEEStr )

        if dataMC == "MC":
            res["cuts"].append( "overlapRemoval==1" )
#            res["prefixes"].append( "overlapRemoval" )

            tr            = TriggerSelector( self.year, singleLepton=(not dileptonic) )
            triggerCutMc  = tr.getSelection( "MC" )

            res["cuts"].append( triggerCutMc )
#            res["prefixes"].append( "trigger" )


        res["cuts"].append( getFilterCut(isData=(dataMC=="Data"), year=self.year, skipBadChargedCandidate=True) )
#        if dataMC=="Data" and self.year == 2018:
#            res["cuts"].append("reweightHEM>0")

        res["cuts"].extend(self.externalCuts)

        return {"cut":"&&".join(res["cuts"]), "prefix":"-".join(res["prefixes"]), "weightStr": self.weightString(dataMC,addMisIDSF=addMisIDSF)}

if __name__ == "__main__":
    setup = Setup( year=2016 )
    for reg in allCR:
        print
        print reg["name"]
        print
        if reg["name"].startswith("DY"): channels = dilepChannels
        else:                   channels = lepChannels
        for channel in channels:
            print
            print channel
            print
            res = setup.selection("MC", channel=channel, **setup.defaultParameters( update=reg["parameters"] ))
            print res["cut"]
            print res["prefix"]
            print res["weightStr"]

            print
            res = setup.selection("Data", channel=channel, **setup.defaultParameters( update=reg["parameters"] ))
            print res["cut"]
            print res["prefix"]
            print res["weightStr"]


