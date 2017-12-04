#!/bin/bash

if [ ! -f .cookie ]
then
    echo ".cookie file does not exist"
    exit 1
fi

mkdir -p inputs

day() {
    curl -sf --cookie "$(<.cookie)" http://adventofcode.com/$(date +%Y)/day/$((10#$1))/input > inputs/day$1.txt
}

# when we are december get current date
[[ $(date +%m) -eq 12 ]] && days=$(date +%d)

echo "fetching..."
for n in $(seq -w 1 ${days:-25})
do
    echo -n "day$n "
    day $n
    [[ $? -eq 0 ]] && s="✔" || s="✖️"
    echo $s
done
echo "done."
