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

cd ..
cloc $repo

rm -rf $repo
