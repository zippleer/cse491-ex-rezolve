#! /usr/bin/env python
import sys

x = open(sys.argv[1]).read()

x = x.lower()
x = x.replace("e", "z")

fp = open(sys.argv[1], 'w')
fp.write("".join(x))
fp.close()
