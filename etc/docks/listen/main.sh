#!/usr/bin/env bash
set -euvxo pipefail
export PATH=$PWD/pod:$PWD/sdk/bin:$PATH
export AWS_DEFAULT_REGION=auto
export BIBLE=$PWD/bible
export REASON=o3-mini
export MODEL=gpt-4o
export TTS=tts-1-hd
export VOICE=onyx
exec httpexec app.sh key
