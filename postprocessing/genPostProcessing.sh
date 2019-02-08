
# SM
#python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_SingleLeptFromT_SM_1Line_test        #SPLIT20
#python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_SingleLeptFromT_SM_3LinePatched_test #SPLIT20
#python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_SingleLeptFromT_SM_3LineBuggy_test   #SPLIT20

# EFT
#python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_SingleLeptFromT_EFT_1Line_test --addReweights --interpolationOrder 2 #SPLIT20
python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_DiLept_EFT_1Line_small         --addReweights --interpolationOrder 2 #SPLIT20
#python genPostProcessing.py --overwrite --processingEra TTGammaEFT_PP_GEN_TTG_v2 --sample TTGamma_DiLept_EFT_1Line               --addReweights --interpolationOrder 2 #SPLIT200

