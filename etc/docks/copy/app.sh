#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
pg
cpg
trans $lang < edit.txt | log
