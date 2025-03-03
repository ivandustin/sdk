#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
sandbox gosmsx | log | trans $lang | log
