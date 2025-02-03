#!/usr/bin/env bash
set -euvxo pipefail
root=$(pwd)
export PATH=$root/sdk/bin:$PATH
export OPENAIMODEL=gpt-4o-mini
export BIBLEHOME=$root/bible
exec httpexec handle.sh lang

