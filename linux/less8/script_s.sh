#!/bin/bash
MDIR=/opt/name
mkdir -p tmp/test
set -e
df -h | grep -o /dev/root >> tmp/test/root
for i in {8..3};
do 
mkdir -p $MDIR/$i.exp
done
