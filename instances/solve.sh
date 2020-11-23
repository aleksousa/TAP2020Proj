#!/bin/bash
INSTANCE=$1

[ ! -f $INSTANCE ] && echo "   *** File '$INSTANCE' does not exist!" && exit 1

./lp.py < $INSTANCE > /tmp/a.lp

glpsol --lp /tmp/a.lp -o /tmp/out &> /dev/null

cat /tmp/out | grep Objective
./greedy.py < $INSTANCE
