#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
export FBPROF=$2
export FBPUB=$3
gstoryx | log | trans $lang | log > content.txt
sen < content.txt | log | trans $lang | log | txt2img title.png
fb --media title.png < content.txt
