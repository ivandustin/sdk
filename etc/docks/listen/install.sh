#!/usr/bin/env bash
set -euvxo pipefail
apt update
apt install -y ffmpeg
pip install awscli
git clone https://github.com/ivandustin/sdk.git
git clone https://github.com/ivandustin/bible.git
git clone https://github.com/ivandustin/pod.git
