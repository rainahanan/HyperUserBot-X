#!/bin/bash

# Copyright (C) 2020 by sandy1709

echo "
hey master
HyperUserBot-X ZINDA THA HAI AUR RHEGA
"

FILE=/app/.git

if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    rm -rf userbot
    rm -rf .github
    rm -rf sample_config.py
    rm -rf requirements.txt
    git clone -b bugs https://github.com/ahirearyan2/HyperUserBot-X HUB
    mv HUB/userbot .
    mv HUB/.github . 
    mv HUB/.git .
    mv HUB/sample_config.py .
    mv HUB/requirements.txt .
    rm -rf HUB
    python ./.github/update.py
fi

FILE=/app/bin/
if [ -d "$FILE" ] ; then
    echo "$FILE directory exists already."
else
    bash ./.github/bins.sh
fi

python -m userbot
