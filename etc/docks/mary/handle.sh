#!/usr/bin/env bash
set -euvxo pipefail
export LANGUAGE=$1
export FBPROF=$2
export FBPUB=$3
exec mary
