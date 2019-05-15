# https://github.com/Paryul10/SPRING19

base="https://github.com"
handle=$1
repo=$2
commitid=$3
end=".git"

url="$base/$handle/$repo$end"

echo $url

git clone $url
cd $repo
git reset --hard $commitid

var=0

if [ "$repo" == "computer-organization-iiith" ]
then
    var=1
elif [ "$repo" == "computer-graphics-iiith" ]
then
    var=2
elif [ "$repo" == "pattern-recognition-iiith" ]
then
    var=3
elif [ "$repo" == "vlsi-iiith" ]
then
    var=4
elif [ "$repo" == "digital-logic-design-iiith" ]
then
    var=5
elif [ "$repo" == "speech-signal-processing-iiith" ]
then
    var=6
else
    echo "No repo Matching.! Please check inputs"
fi

# echo $var


cd ..

echo $var > abc.txt
cloc $repo >> abc.txt
# rm abc.txt
# cloc $repo

rm -rf $repo
