#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
export FBPROF=$2
export FBPUB=$3
sandbox exgx | log | ifa trans $lang | log | fbpost
