#!/usr/bin/env bash
set -euvxo pipefail
root=$(pwd)
export PATH=$root/sdk/bin:$PATH
export MODEL=gpt-4o-mini
export BIBLEHOME=$root/bible
exec httpexec app.sh lang
