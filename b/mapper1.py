#!/usr/bin/env python

import sys
k = 2
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    # increase counters
    for i in range(len(words)-k+1):
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
	g = ' '.join(words[i:i+k])
        print '%s\t%s' % (g, 1)
