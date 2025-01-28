#!/usr/bin/env bash
set -euvxo pipefail
root=$(pwd)
export PATH=$root/sdk/bin:$PATH
export BIBLEHOME=$root/bible
export PWSTOR=$root/pw.json
export OPENAIMODEL=gpt-4o
exec httpexec handle.sh lang prof pub
