#!/usr/bin/env bash
set -euvxo pipefail
root=$(pwd)
export PATH=$root/sdk/bin:$PATH
export BIBLEHOME=$root/bible
export MODEL=gpt-4o
exec httpexec app.sh lang
