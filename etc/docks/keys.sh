#!/usr/bin/env bash
set -euvx
for file in */pre.sh
do
	dir=$(dirname $file)
	cd $dir
	fly secrets set OPENAI=$OPENAI
	cd ..
done
