#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
pg
short $(<topic.txt) < eng.txt | log | trans $lang | log
