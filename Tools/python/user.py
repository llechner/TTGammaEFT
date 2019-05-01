import os

redirector        = 'root://hephyse.oeaw.ac.at/'
redirector_global = 'root://cms-xrd-global.cern.ch/'

if os.environ['USER'] in ['schoef', 'rschoefbeck', 'schoefbeck']:
    results_directory               = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT/results/"
    skim_output_directory           = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT/skims/"
    skim_directory                  = "/afs/hephy.at/data/dspitzbart01/TTGammaEFT/skims/"
    tmp_directory                   = "/afs/hephy.at/data/rschoefbeck02/TTGammaEFT_tmp/"
    plot_directory                  = "/afs/hephy.at/user/r/rschoefbeck/www/TTGammaEFT/"
    data_directory                  = "/afs/hephy.at/data/rschoefbeck01/cmgTuples/"
    postprocessing_directory        = "TTGammaEFT_PP_2016_TTG_v5/inclusive/"
    postprocessing_output_directory = "/afs/hephy.at/data/rschoefbeck02/cmgTuples/"
    analysis_results                = results_directory

    cache_directory                     = "/afs/hephy.at/data/rschoefbeck01/TTGammaEFT/cache/"

if os.environ['USER'] in ['llechner']:
    tmp_directory                       = "/afs/hephy.at/data/llechner01/Top_tmp/"
    results_directory                   = "/afs/hephy.at/data/llechner01/TTGammaEFT/results/"

#    skim_directory                      = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"
#    skim_output_directory               = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"

    plot_directory                      = "/afs/hephy.at/user/l/llechner/www/TTGammaEFT/"
    data_directory1                     = "/afs/hephy.at/data/llechner01/TTGammaEFT/nanoTuples/"
    data_directory2                     = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"
    data_directory3                     = "/afs/hephy.at/data/llechner03/TTGammaEFT/nanoTuples/"

    postprocessing_directoryGEN         = "TTGammaEFT_PP_GEN_TTG_v9/gen/"

    postprocessing_directoryMC2016      = "TTGammaEFT_PP_2016_TTG_private_v16/dilep/"
    postprocessing_directoryMC2017      = "TTGammaEFT_PP_2017_TTG_private_v16/dilep/"
    postprocessing_directoryMC2018      = "TTGammaEFT_PP_2018_TTG_private_v16/dilep/"

    postprocessing_directoryRun2016     = "TTGammaEFT_PP_2016_TTG_Data_v16/dilep/"
    postprocessing_directoryRun2017     = "TTGammaEFT_PP_2017_TTG_Data_v16/dilep/"
    postprocessing_directoryRun2018     = "TTGammaEFT_PP_2018_TTG_Data_v16/dilep/"

    postprocessing_directoryMC2016_semilep  = "TTGammaEFT_PP_2016_TTG_private_v16/semilep/"
    postprocessing_directoryMC2017_semilep  = "TTGammaEFT_PP_2017_TTG_private_v16/semilep/"
    postprocessing_directoryMC2018_semilep  = "TTGammaEFT_PP_2018_TTG_private_v16/semilep/"

    postprocessing_directoryRun2016_semilep = "TTGammaEFT_PP_2016_TTG_Data_v16/semilep/"
    postprocessing_directoryRun2017_semilep = "TTGammaEFT_PP_2017_TTG_Data_v16/semilep/"
    postprocessing_directoryRun2018_semilep = "TTGammaEFT_PP_2018_TTG_Data_v16/semilep/"

#    postprocessing_directoryPrefiring   = "TTGammaEFT_PP_2017_TTG_prefiring_v2/dilep/"
    postprocessing_directoryPrefiring   = "TTGammaEFT_PP_2017_TTG_prefiring_v1/dilep/"

    postprocessing_output_directory     = "/afs/hephy.at/data/llechner03/TTGammaEFT/nanoTuples/"

    gridpack_directory                  = "/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/"

    analysis_results                    = results_directory
    cache_directory                     = "/afs/hephy.at/data/llechner01/TTGammaEFT/cache/"
    combineReleaseLocation              = '/afs/hephy.at/user/l/llechner/public/CMSSW_8_1_0/src'
    cardfileLocation                    = '/afs/hephy.at/data/llechner01/TTGammaEFT/results/cardfiles/'

    dpm_directory                       = '/dpm/oeaw.ac.at/home/cms/store/user/llechner/'
