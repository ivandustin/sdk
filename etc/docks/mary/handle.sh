#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
export FBPROF=$2
export FBPUB=$3
andrew | log | ifa trans $lang | log > content.txt
philip content.txt
sen < content.txt | log | ifa trans $lang | log | txt2img title.png
fbpost --media title.png < content.txt
