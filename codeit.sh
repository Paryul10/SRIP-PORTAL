# https://github.com/Paryul10/SPRING19

base="https://github.com"
handle=$1
repo=""
# commitid=$3
end=".git"



var=$2

if [ "$var" == 1 ]
then
    repo="computer-organization-iiith"
elif [ "$var" == 2 ]
then
    repo="computer-graphics-iiith"
elif [ "$var" == 3 ]
then
    repo="pattern-recognition-iiith"
elif [ "$var" == 4 ]
then
    repo="vlsi-iiith"
elif [ "$var" == 5 ]
then
    repo="digital-logic-design-iiith"
elif [ "$var" == 6 ]
then
    repo="speech-signal-processing-iiith"
else
    echo "No repo Matching.! Please check inputs"
fi


url="$base/$handle/$repo$end"

echo $url

git clone $url
cd $repo
# git reset --hard $commitid


# # echo $var


cd ..

dest="$repo/SRIP/Codes/"

# echo $dest

echo $var > abc.txt
cloc $dest >> abc.txt


cloc $dest
# rm abc.txt

# rm -rf $repo

mv $repo $handle


python3 fpevaluator.py