#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
export FBPROF=$2
export FBPUB=$3
exgx | log | ifa trans $lang | log > post.txt
ifa trans $lang < topic.txt | txt2img img.png
fbpost --media img.png < post.txt
