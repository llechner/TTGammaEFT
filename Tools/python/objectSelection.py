# Standard Imports
import textwrap

photonIdCutBasedBitmap = {                     'loose':1, 'medium':2, 'tight':4 }  # NanoAOD Version ID bitmap, 2^(0:loose, 1:medium, 2:tight)
photonIdCutBased       = { 'fail':0,           'loose':1, 'medium':2, 'tight':3 }  # NanoAOD Version
electronIdCutBased     = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # NanoAOD Version

muonPfIsoId            = { 'PFIsoVeryLoose':1, 'PFIsoLoose':2, 'PFIsoMedium':3, 'PFIsoTight':4, 'PFIsoVeryTight':5, 'PFIsoVeryVeryTight':6 }

jetIdNamingList        = [ "tightLepVeto", "tight", "loose" ]

# see https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc80X_doc.html
# or  https://cms-nanoaod-integration.web.cern.ch/integration/master-102X/mc102X_doc.html
# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
vidNestedWPBitMapNamingList = [ 'MinPtCut', 'GsfEleSCEtaMultiRangeCut', 'GsfEleDEtaInSeedCut', 'GsfEleDPhiInCut', 'GsfEleFull5x5SigmaIEtaIEtaCut', 'GsfEleHadronicOverEMEnergyScaledCut', 'GsfEleEInverseMinusPInverseCut', 'GsfEleRelPFIsoScaledCut', 'GsfEleConversionVetoCut', 'GsfEleMissingHitsCut' ][::-1]
vidNestedWPBitMap           = { 'fail':0, 'veto':1, 'loose':2, 'medium':3, 'tight':4 }  # Bitwise (Electron vidNestedWPBitMap ID flags (3 bits per cut), '000'=0 is fail, '001'=1 is veto, '010'=2 is loose, '011'=3 is medium, '100'=4 is tight)

# the PhoAnyPFIsoWithEACut is used twice in the root info, thus I call one PhoAnyPFIsoWithEACut2 (they don't have the same cuts)
# seems like the list is implemented reversed, thus the [::-1] at the end (values make more sense in that way)
vidNestedWPBitMapNamingListPhoton = [ 'MinPtCut', 'PhoSCEtaMultiRangeCut', 'PhoSingleTowerHadOverEmCut', 'PhoFull5x5SigmaIEtaIEtaCut', 'PhoAnyPFIsoWithEACut', 'PhoAnyPFIsoWithEAAndQuadScalingCut', 'PhoAnyPFIsoWithEACut2' ][::-1]

# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
def jetIdBitMapToDict( val ):
    # convert int of vidNestedWPBitMap ( e.g. val = 6 ) to bitmap ( e.g. "110"), then to list ( e.g. [ 1, 1, 0 ] )
    # Jet ID flags bit1 is loose (always false in 2017 since it does not exist), bit2 is tight, bit3 is tightLepVeto : 0 at: 0x5f1a030
    # in 80x no tightLepVeto exists, only 2 bits, bit3 is set to 0
    # create dictionary
    # however some entries of jets don't have a jedId entry, no clue why (very limited number of events e.g. in DY M50 Fall2017)
    try: idList = map( lambda x: int(x), "{0:03b}".format( val ) )
    except: idList = [ 0, 0, 0 ]
    return dict( zip( jetIdNamingList, idList ) )

def photonIdBitMapToDict( val ):
    idList = [ int( x, 2 ) for x in textwrap.wrap( "{0:014b}".format( val ) , 2) ]
    return dict( zip( vidNestedWPBitMapNamingListPhoton, idList ) )

def photonIdBitMapToDictRev( val ):
    idList = [ int( x, 2 ) for x in textwrap.wrap( "{0:014b}".format( val ) , 2) ]
    return dict( zip( vidNestedWPBitMapNamingListPhoton[::-1], idList ) )

# Attention: only for nanoAOD v94x or higher (in 80x, only 2 bits are used)
def vidNestedWPBitMapToDict( val ):
    # convert int of vidNestedWPBitMap ( e.g. val = 611099940 ) to bitmap ( e.g. "100100011011001010010100100100")
    # split vidBitmap string (containing 3 bits per cut) in parts of 3 bits ( e.g. ["100","100","011","011","001","010","010","100","100","100"] )
    # convert 3 bits to int ( e.g. [4, 4, 3, 3, 1, 2, 2, 4, 4, 4])
    # create dictionary
    idList = [ int( x, 2 ) for x in textwrap.wrap( "{0:030b}".format( val ) , 3) ] #use 2 for nanoAOD version 80x
    return dict( zip( vidNestedWPBitMapNamingList, idList ) )

# General Selection Functions
def deltaRCleaning( cleaningParticles, otherParticles, dRCut = 0.4 ):

    from Analysis.Tools.helpers  import deltaR

    res = []
    for part in cleaningParticles:
        clean = True
        for otherParticle in otherParticles:
            if deltaR( otherParticle, part ) < dRCut:
                clean = False
                break
        if clean:
            res.append( part )
    res.sort( key = lambda p: -p['pt'] )
    return res

def getParticles( c, collVars, coll ):
    from Analysis.Tools.helpers import getVarValue, getObjDict
    return [ getObjDict( c, coll+'_', collVars, i ) for i in range(int(getVarValue(c, 'n'+coll))) ]

# Reco b-Jet Filter
def isBJet( j, tagger='DeepCSV', year=2016 ):
    if tagger == 'CSVv2':
        if year == 2016:
            # https://twiki.cern.ch/twikix/bin/viewauth/CMS/BtagRecommendation80XReReco
            return j['btagCSVV2'] > 0.8484 
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagCSVV2'] > 0.8838 
        elif year == 2018:
            # UPDATE WHEN AVAILABLE
            return j['btagCSVV2'] > 0.8838 
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)
    elif tagger == 'DeepCSV':
        if year == 2016:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation2016Legacy
            return j['btagDeepB'] > 0.6321
        elif year == 2017:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X
            return j['btagDeepB'] > 0.4941
        elif year == 2018:
            # https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation102X
            return j['btagDeepB'] > 0.4184
        else:
            raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def vertexSelector( l ):
#    if abs(l['pdgId']) == 11: absEta = abs(l["eta"] + l["deltaEtaSC"])   # eta supercluster
#    else:                     absEta = abs(l["eta"])                     # eta
    EC = 0 #absEta > 1.479 # only if difference for EndCaps
    if abs(l["dxy"]) > 0.05 + 0.05*EC: return False
    if abs(l["dz"])  > 0.1  + 0.1*EC:  return False
    return True

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

def photonVIDSelector( p, idVal, removedCuts=[] ):
    # https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2

    vidDict = photonIdBitMapToDict( p["vidNestedWPBitmap"] )
    if not removedCuts:
        return all( [ cut >= idVal for cut in vidDict.values() ] )

#    # all cuts in removedCuts
#    if not list( set(vidNestedWPBitMapNamingListPhoton) - set(removedCuts) ):
#        return True

    # sieie is implemented according to the twiki
    if ("sieie"          in removedCuts):
        vidDict = removekey( vidDict, "PhoFull5x5SigmaIEtaIEtaCut" )
    # hoe is implemented according to the twiki
    if ("hoe"            in removedCuts):
        vidDict = removekey( vidDict, "PhoSingleTowerHadOverEmCut" )
    # PhoAnyPFIsoWithEACut seems to be chg-iso cut, pretty sure
    if ("pfRelIso03_chg" in removedCuts):
        vidDict = removekey( vidDict, "PhoAnyPFIsoWithEACut" )
    # PhoAnyPFIsoWithEACut2 seems to be very close to all-iso cut, but not everywhere, sometimes it's the neutral-iso cut
    # no clue what PhoAnyPFIsoWithEAAndQuadScalingCut is, I think its the all-iso cut with additional pt**2 dependence, hard to check
    if ("pfRelIso03_all" in removedCuts):
        vidDict = removekey( vidDict, "PhoAnyPFIsoWithEACut2" )
        vidDict = removekey( vidDict, "PhoAnyPFIsoWithEAAndQuadScalingCut" )
    # no clue what the scEtaMultiRange cut really is, probably out of scope for this analysis as we only use SC barrel photons
    if ("scEtaMultiRange" in removedCuts):
        vidDict = removekey( vidDict, "PhoSCEtaMultiRangeCut" )
    # no clue what the minPt cut really is
    if ("minPt"          in removedCuts):
        vidDict = removekey( vidDict, "MinPtCut" )
        
    return all( [ cut >= idVal for cut in vidDict.values() ] )

def photonMediumIDSelector( p, year, removedCuts=[], printVar=False ):
    # ATTENTION, there is a problem with the selected cuts
    # https://twiki.cern.ch/twiki/bin/view/CMS/CutBasedPhotonIdentificationRun2

    if year not in [ 2016, 2017, 2018 ]:
        raise ( NotImplementedError, "Don't know what cut to use for year %s"%year )

    missingCuts = list( set( removedCuts ) - set( [ "hoe", "sieie", "pfRelIso03_chg", "pfRelIso03_all", "pfRelIso03_n" ] ) )
    if len( missingCuts ):
        raise ( NotImplementedError, "Cuts %s not in medium photon cutbased ID"%", ".join( missingCuts ))

    EC                 = abs(p["eta"]) > 1.479
    pfRelIso03_neutral = p["pfRelIso03_all"] - p["pfRelIso03_chg"]

    if EC and year == 2016: # photon medium cutbased ID 2016 EC
        hoe_cut                = 0.0219
        sieie_cut              = 0.03001
        pfRelIso03_chg_cut     = 0.442
        pfRelIso03_neutral_cut = 1.715 + 0.0163 * p["pt"] + 0.000014 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 3.863 + 0.0034 * p["pt"]
    elif not EC and year == 2016: # photon medium cutbased ID 2016 Barrel
        hoe_cut                = 0.0396
        sieie_cut              = 0.01022
        pfRelIso03_chg_cut     = 0.441
        pfRelIso03_neutral_cut = 2.725 + 0.0148 * p["pt"] + 0.000017 * p["pt"] * p["pt"] 
        pfRelIso03_all_cut     = 2.571 + 0.0047 * p["pt"]
    elif EC and year != 2016: # photon medium cutbased ID 2017 EC
        hoe_cut                = 0.0326
        sieie_cut              = 0.0272
        pfRelIso03_chg_cut     = 1.051
        pfRelIso03_neutral_cut = 2.718 + 0.0117 * p["pt"] + 0.000023 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 3.867 + 0.0037 * p["pt"]
    elif not EC and year != 2016: # photon medium cutbased ID 2017 Barrel
        hoe_cut                = 0.02197
        sieie_cut              = 0.01015
        pfRelIso03_chg_cut     = 1.141
        pfRelIso03_neutral_cut = 1.189 + 0.01512  * p["pt"] + 0.00002259 * p["pt"] * p["pt"]
        pfRelIso03_all_cut     = 2.08  + 0.004017 * p["pt"]

    if ("sieie"          not in removedCuts) and (p["sieie"]            >= sieie_cut):#              return False
                if printVar: print "sieie"
                return False
    if ("pfRelIso03_chg" not in removedCuts) and (p["pfRelIso03_chg"]*p["pt"]   >= pfRelIso03_chg_cut):#     return False
                if printVar: print "pfRelIso03_chg"
                return False
    if ("pfRelIso03_n"   not in removedCuts) and (pfRelIso03_neutral*p["pt"]    >= pfRelIso03_neutral_cut):# return False
                if printVar: print "pfRelIso03_n"
                return False
    if ("hoe"            not in removedCuts) and (p["hoe"]              >= hoe_cut):
                if printVar: print "hoe"
                return False
    if ("pfRelIso03_all" not in removedCuts) and (p["pfRelIso03_all"]*p["pt"]   >= pfRelIso03_all_cut):#     return False
                if printVar: print "pfRelIso03_all"
                return False
    return True

# nanoAOD 94x or higher
def triggerEmulatorSelector( l, wp ):
    cutDict    = vidNestedWPBitMapToDict( l['vidNestedWPBitmap'] )
    wpCutValue = vidNestedWPBitMap[ wp ]     
    return all( val >= wpCutValue for val in cutDict.values() )

#def triggerEmulatorSelector( l, wp ):
#    # still missing: dPhiSC, dEtaSC (switch to triggerEmulatorCuts in nanoAOD 94x or higher)
#    ECSc = abs(l["eta"] + l["deltaEtaSC"]) > 1.479
#    if l["sieie"]            >= (0.011+0.019*ECSc): return False
#    if l["eInvMinusPInv"]    <= -0.05:              return False
#    if l["eInvMinusPInv"]    >= (0.01-0.005*ECSc):  return False
#    if l["hoe"]              >= (0.10-0.03*ECSc):   return False
#    return True

def barrelEndcapVeto( p ):
    if abs(p['pdgId']) == 11: absEta = abs(p["eta"] + p["deltaEtaSC"])   # eta supercluster
    else:                     absEta = abs(p["eta"])                     # eta
    return ( absEta > 1.566 or absEta < 1.4442 )

# Reco Selectors
def jetSelector( year, noPtEtaCut=False, ptVar="pt" ):
    # https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetIDhttps://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID
    if year == 2016:
        # According to AN-2017/197
        # jetID cuts, pT and eta cuts
        def func(j):
#            if not j["cleanmask"]:                           return False # too much cleaning
            if not noPtEtaCut:
                if j[ptVar]      <= 30:                      return False
                if abs(j["eta"]) >= 2.4:                     return False
            if not jetIdBitMapToDict( j["jetId"] )["loose"]: return False
            return True
        return func

    elif year == 2017 or year == 2018:
        # jetID cuts, pT and eta cuts
        def func(j):
#            if not j["cleanmask"]:                           return False
            if not noPtEtaCut:
                if j[ptVar]      <= 30:                      return False
                if abs(j["eta"]) >= 2.4:                     return False
            if not jetIdBitMapToDict( j["jetId"] )["tight"]: return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for year %s"%year)

def muonSelector( lepton_selection, leading=False, noPtEtaCut=False ):
    # According to AN-2017/197
    if lepton_selection == 'tight':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          <  30:                        return False
                if abs(l["eta"])    > 2.4:                        return False
            if not l["tightId"]:                                  return False
            if not vertexSelector(l):                             return False
            if l['pfRelIso03_all']  > 0.12:                       return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoMedium']: return False
            if l["sip3d"]           > 4:                          return False
            return True
        return func

    elif lepton_selection == 'medium':
        ptCut = 25 if leading else 15
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          < ptCut:                      return False
                if abs(l["eta"])    > 2.4:                        return False
            if not l["mediumId"]:                                 return False
            if not vertexSelector(l):                             return False
            if l['pfRelIso03_all']  > 0.12:                       return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoMedium']: return False
            if l["sip3d"]           > 4:                          return False
            return True
        return func

    elif lepton_selection == 'veto2l':
        # muon loose requirement
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          < 15:                            return False
                if abs(l["eta"])    > 2.4:                           return False
            if not l["isPFcand"]:                                    return False
            if not ( l["isGlobal"] or l["isTracker"] ):              return False
            if not vertexSelector(l):                                return False
            if l['pfRelIso03_all']  > 0.4:                           return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoVeryLoose']: return False
            if l["sip3d"]           > 4:                             return False
            return True
        return func

    elif lepton_selection == 'veto':
        # muon loose requirement
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          < 15:                            return False
                if abs(l["eta"])    > 2.4:                           return False
            if not l["isPFcand"]:                                    return False
            if not ( l["isGlobal"] or l["isTracker"] ):              return False
            if not vertexSelector(l):                                return False
            if l['pfRelIso03_all']  > 0.25:                           return False
#            if l['pfIsoId']        <  muonPfIsoId['PFIsoVeryLoose']: return False
            if l["sip3d"]           > 4:                             return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for muons")

# electrons 
def eleSelector( lepton_selection, leading=False, noPtEtaCut=False ):
    idVar = "cutBased"
    # According to AN-2017/197
    if lepton_selection == 'tight':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          < 35:                return False
                if abs(l["eta"])    > 2.1:               return False
            if not barrelEndcapVeto(l):                  return False
            if l[idVar] < electronIdCutBased['tight']:   return False
            if l['pfRelIso03_all']  > 0.12:              return False
            if l["sip3d"]           > 4:                 return False
#            if int(l["lostHits"])  != 0:                 return False # in the cutbased id? Ghent!
#            if not l["convVeto"]:                        return False # in the cutbased id? Ghent!
            if not vertexSelector(l):                    return False
            return True
        return func

    elif lepton_selection == 'tight2l':
        ptCut = 25 if leading else 15
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= ptCut:             return False
                if abs(l["eta"])   >= 2.4:               return False
            if not barrelEndcapVeto(l):                  return False
            if l[idVar] < electronIdCutBased['tight']:   return False
            if l['pfRelIso03_all']  > 0.12:              return False
            if l["sip3d"]           > 4:                 return False
#            if int(l["lostHits"])  != 0:                 return False # in the cutbased id? Ghent!
#            if not l["convVeto"]:                        return False # in the cutbased id? Ghent!
            if not vertexSelector(l):                    return False
            return True
        return func

    elif lepton_selection == 'medium':
        ptCut = 25 if leading else 15
        def func(l):
            if not noPtEtaCut:
                if l["pt"]         <= ptCut:             return False
                if abs(l["eta"])   >= 2.4:               return False
            if not barrelEndcapVeto(l):                  return False
            if l[idVar] < electronIdCutBased['medium']:  return False
            if l['pfRelIso03_all']  > 0.12:              return False
            if l["sip3d"]           > 4:                 return False
#            if int(l["lostHits"])  != 0:                 return False # in the cutbased id? Ghent!
#            if not l["convVeto"]:                        return False # in the cutbased id? Ghent!
            if not vertexSelector(l):                    return False
            return True
        return func

    elif lepton_selection == 'veto':
        def func(l):
            if not noPtEtaCut:
                if l["pt"]          < 15:              return False
                if abs(l["eta"])    > 2.4:             return False
            if not barrelEndcapVeto(l):                return False
            if l[idVar] < electronIdCutBased['veto']:  return False
            if l['pfRelIso03_all']  > 0.4:             return False
            if l["sip3d"]           > 4:               return False
            if not vertexSelector(l):                  return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for electrons")

def tauSelector( lepton_selection ):
    # dummy function
        def func(l):
            return True
        return func

def photonSelector( selection, noPtEtaCut=False, year=None, removedCuts=[] ):
    # According to AN-2017/197
    idVar    = "cutBased"       if year==2016 else "cutBasedBitmap"
    photonId = photonIdCutBased if year==2016 else photonIdCutBasedBitmap

    if selection == "mva":
        def func(g):
            if not noPtEtaCut:
                if g["pt"]       <= 20:        return False
#                if not g["isScEtaEB"]:        return False # Supercluster Barrel only
                if abs(g["eta"]) >= 1.4442:    return False # Barrel only
            if g["pixelSeed"]:                 return False
            if not g["electronVeto"]:          return False
            if not g["mvaID_WP80"]:            return False
            return True
        return func

    if selection == "medium":
        def func(g):
            if not noPtEtaCut:
                if g["pt"]       <= 20:                                                  return False
#                if not g["isScEtaEB"]:                                                   return False # Supercluster Barrel only
                if abs(g["eta"]) >= 1.4442:                                              return False # Barrel only
            if not "pixelSeed" in removedCuts:
                if g["pixelSeed"]:                                                       return False
            if not "electronVeto" in removedCuts:
                if not g["electronVeto"]:                                                return False
#            if g[idVar]          <  photonId[selection]:                                 return False
            if not photonVIDSelector( g, photonId[selection], removedCuts=removedCuts ): return False
            return True
        return func

    elif selection == "loose":
        def func(g):
            if not noPtEtaCut:
                if g["pt"]       <= 20:                                             return False
#                if not g["isScEtaEB"]:                                                   return False # Supercluster Barrel only
                if abs(g["eta"]) >= 1.479:                                          return False # Barrel only
            if g["pixelSeed"]:                                                      return False
            if not g["electronVeto"]:                                               return False
#            if g[idVar]          <  photonId[selection]:                            return False
            if not photonVIDSelector( g, photonId[selection], removedCuts=removedCuts ): return False
            return True
        return func

    else:
        raise (NotImplementedError, "Don't know what cut to use for photons")


# Gen Selectors
def genJetSelector():
    # According to AN-2017/197
    def func(j):
        if j["pt"]       <= 30:  return False
        if abs(j["eta"]) >= 2.4: return False
        return True
    return func

def genLeptonSelector():
    # According to AN-2017/197
    def func(l):
        if l["pt"]       <= 15:  return False
        if abs(l["eta"]) >= 2.4: return False
        return True
    return func

def genPhotonSelector( photon_selection=None ):
    # According to AN-2017/197
    if photon_selection == 'overlapTTGamma':
        # Remove events from ttbar sample, keep ttgamma events
        def func(g):
            if g["pt"]       < 13:  return False
            if abs(g["eta"]) > 3.0: return False
            return True
        return func

    elif photon_selection == 'overlapZWGamma':
        # Remove events from DY and W+jets sample, keep Zgamma and Wgamma events
        def func(g):
            if g["pt"]       < 15:  return False
            if abs(g["eta"]) > 2.6: return False
            return True
        return func

    elif photon_selection == 'overlapSingleTopTch':
        # Remove events from single top t-channel sample, keep single top + photon events
        def func(g):
            if g["pt"]       < 10:  return False
            if abs(g["eta"]) > 2.6: return False
            return True
        return func

    else:
        # general gen-photon selection
        def func(g):
            if g["pt"]       < 13:    return False
            if abs(g["eta"]) > 1.479: return False
            return True
        return func

# Gen Particle Filter
def filterGenElectrons( genParts, status=None ):
    if   status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    else:                   stat = [1,23]
    electrons = list( filter( lambda l: abs(l['pdgId']) == 11 and l['status'] in stat, genParts ) )
    return electrons

def filterGenMuons( genParts, status=None ):
    if   status == 'first': stat = [23]
    elif status == 'last':  stat = [1]
    else:                   stat = [1,23]
    muons = list( filter( lambda l: abs(l['pdgId']) == 13 and l['status'] in stat, genParts ) )
    return muons

def filterGenPhotons( genParts, status=None ):
    photons = list( filter( lambda l: abs(l['pdgId']) == 22 and l['status'] >= 0, genParts ) )
    return photons

def filterGenTops( genParts ):
    tops = list( filter( lambda l: abs(l['pdgId']) == 6 and l['status'] == 62, genParts ) )
    return tops

def filterGenBJets( genJets ):
    bjets = list( filter( lambda j: abs(j['hadronFlavour']) == 5, genJets ) )
    return bjets

# Pythia status flags:
#  1: outgoing particle (e.g. photon from decay products of top)
# 23: e.g. intermediate photon (mother of photon with status 1)
# 44: ISR photons (outgoing, but initially produced and then nothing changed (MG photons?)
# 52: photons from e.g. top, probably also initially produced (MG photons?)
# 51: photons from e.g. top, probably also initially produced (MG photons?)

# 62: outgoing subprocess particle with primordial kT included, last gencopy before it decays
# 23: outgoing
# 71: copied partons to collect into contiguous colour singlet (jets)
#  1: stage of event generation inside PYTHIA
# 22: intermediate (intended to have preserved mass) (tops)
