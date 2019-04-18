''' Helper functions for TTGammaEFT
'''
#Standard imports
import ROOT
import itertools

# Logging
import logging
logger = logging.getLogger(__name__)

def m3( jets, nBJets=0, tagger='DeepCSV', year=2016, photon=None ):
    """ Calculate M3 Variable with a min amount of bJets in it
    """
    if len( jets ) < 3 or nBJets > 3 or nBJets > len( jets ): return -999, -1, -1, -1

    vecs = []
    for i, j in enumerate( jets ):
        vec = ROOT.TLorentzVector()
        vec.SetPtEtaPhiM( j['pt'], j['eta'], j['phi'], 0. )
        vecs.append( ( i, vec ) )

    if photon:
        photonVec = ROOT.TLorentzVector()
        photonVec.SetPtEtaPhiM( photon['pt'], photon['eta'], photon['phi'], 0. )

    maxSumPt   = 0
    m3         = -999
    i1, i2, i3 = -1, -1, -1

    from TTGammaEFT.Tools.objectSelection import isBJet

    for j3_comb in itertools.combinations( vecs, 3 ):
        if nBJets > 0:
            nBs = sum( [ isBJet( jets[v[0]], tagger=tagger, year=year ) for v in j3_comb ] )
            if nBs != nBJets: continue

        vecSum = sum( [ v[1] for v in j3_comb ] + [photonVec] if photon else [ v[1] for v in j3_comb ], ROOT.TLorentzVector() )
        if vecSum.Pt() > maxSumPt:
            maxSumPt   = vecSum.Pt()
            m3         = vecSum.M()
            i1, i2, i3 = [ v[0] for v in j3_comb ]

    return m3, i1, i2, i3


