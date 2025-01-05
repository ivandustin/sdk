#!/usr/bin/env bash
set -euvxo pipefail
lang=$1
sandbox gosmsx | trans2 $lang | log
