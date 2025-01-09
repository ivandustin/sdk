#!/usr/bin/env bash
set -euvxo pipefail
pip install playwright chevron
playwright install chromium
playwright install-deps
git clone https://github.com/ivandustin/sdk.git
git clone https://github.com/ivandustin/bible.git
