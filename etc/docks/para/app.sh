#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
pg
gp < topic.txt | log | trans $lang | log
