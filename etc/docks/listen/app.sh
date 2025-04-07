#!/usr/bin/env bash
set -euvxo pipefail
key=$1
[ "$key" = "$KEY" ]
tmp=$(mktemp -d)
trap "rm -rf $tmp" EXIT
cd $tmp
make.sh
aws s3 cp . s3://$BUCKET --recursive
