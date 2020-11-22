#!/bin/bash
./gera.py 20 90 3 23 29 > /tmp/0

./lp.py < /tmp/0 > /tmp/a.lp

glpsol --lp /tmp/a.lp -o /tmp/out &> /dev/null

cat /tmp/out | grep Objective
./greedy.py < /tmp/0
