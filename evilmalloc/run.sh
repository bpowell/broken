#!/bin/bash
echo $@
echo ""
LD_PRELOAD=`pwd`/evil.so $@
