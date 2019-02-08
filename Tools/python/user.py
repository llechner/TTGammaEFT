import os

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

if os.environ['USER'] in ['llechner']:
    tmp_directory                       = "/afs/hephy.at/data/llechner01/Top_tmp/"
    results_directory                   = "/afs/hephy.at/data/llechner01/TTGammaEFT/results/"

    skim_directory                      = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"
    skim_output_directory               = "/afs/hephy.at/data/llechner01/TTGammaEFT/skims/"

    plot_directory                      = "/afs/hephy.at/user/l/llechner/www/TTGammaEFT/"
    data_directory                      = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    data_directoryGEN                   = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    data_directory2016                  = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"
    data_directory2017                  = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"
    data_directory2018                  = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    data_datadirectory2016              = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"
    data_datadirectory2017              = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"
    data_datadirectory2018              = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    data_directoryPrefiring             = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    postprocessing_directoryGEN         = "TTGammaEFT_PP_GEN_TTG_v2/gen/"

    postprocessing_directory2016        = "TTGammaEFT_PP_2016_TTG_private_v4/dilep/"
    postprocessing_directory2017        = "TTGammaEFT_PP_2017_TTG_private_v5/dilep/"
    postprocessing_directory2018        = "TTGammaEFT_PP_2018_TTG_private_v3/dilep/"

    postprocessing_datadirectory2016    = "TTGammaEFT_PP_2016_TTG_Data_v4/dilep/"
    postprocessing_datadirectory2017    = "TTGammaEFT_PP_2017_TTG_Data_v4/dilep/"
    postprocessing_datadirectory2018    = "TTGammaEFT_PP_2018_TTG_Data_v3/dilep/"

    postprocessing_directoryPrefiring   = "TTGammaEFT_PP_2017_TTG_prefiring_v1/dilep/"

    postprocessing_output_directory     = "/afs/hephy.at/data/llechner02/TTGammaEFT/nanoTuples/"

    gridpack_directory                  = "/afs/hephy.at/data/llechner01/TTGammaEFT/gridpacks/"

    analysis_results                    = results_directory
    cache_directory                     = "/afs/hephy.at/data/llechner01/TTGammaEFT/cache/"
