#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
pg
g < topic.txt | log | trans $lang | log
