#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
export FBPROF=$2
export FBPUB=$3
pg
cpg
exg < edit.txt | log > exg.txt
(
	ifa trans $lang < edit.txt | log
	echo
	echo —
	echo
	ifa trans $lang < exg.txt | log
) > post.txt
sen < edit.txt | log | ifa trans $lang | log | txt2img title.png
fbpost --media title.png < post.txt
