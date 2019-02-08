#ctZ

#Dileps
python cache_nll.py $1 --years 2016 --variables ctZ ctZI --cores 6 --selections 2l
python cache_nll.py $1 --years 2017 --variables ctZ ctZI --cores 6 --selections 2l
#SemiLep
python cache_nll.py $1 --years 2016 --variables ctZ ctZI --cores 6 --selections 1l
python cache_nll.py $1 --years 2017 --variables ctZ ctZI --cores 6 --selections 1l
#Combined
python cache_nll.py $1 --years 2016 2017 --variables ctZ ctZI --cores 6 --selections 2l
#SemiLep Combined
python cache_nll.py $1 --years 2016 2017 --variables ctZ ctZI --cores 6 --selections 1l
#All Combined
python cache_nll.py $1 --years 2016 2017 --variables ctZ ctZI --cores 6 --selections 1l 2l

#ctW

#Dilep
python cache_nll.py $1 --years 2016 --variables ctW ctWI --cores 6 --selections 2l
python cache_nll.py $1 --years 2017 --variables ctW ctWI --cores 6 --selections 2l
#SemiLep
python cache_nll.py $1 --years 2016 --variables ctW ctWI --cores 6 --selections 1l
python cache_nll.py $1 --years 2017 --variables ctW ctWI --cores 6 --selections 1l
#Combined
python cache_nll.py $1 --years 2016 2017 --variables ctW ctWI --cores 6 --selections 2l
#SemiLep Combined
python cache_nll.py $1 --years 2016 2017 --variables ctW ctWI --cores 6 --selections 1l
#All Combined
python cache_nll.py $1 --years 2016 2017 --variables ctW ctWI --cores 6 --selections 1l 2l
