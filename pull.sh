dir=$1
commitid=$2

cd $dir
git pull

git reset --hard $commitid

cd ..
# cd SRIP
# cd Codes

# cloc . > abc.txt

# cd ../../..

cloc $dir/SRIP/Codes > abc.txt

python3 fpevaluator.py

echo $dir
