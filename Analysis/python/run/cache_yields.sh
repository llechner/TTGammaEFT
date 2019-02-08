python cache_yields_semilep.py $1 --year 2016 --cores 6 
python cache_yields_semilep.py $1 --year 2017 --cores 6 --noData

python cache_yields.py $1 --year 2016 --cores 6
python cache_yields.py $1 --year 2017 --cores 6 --noData


