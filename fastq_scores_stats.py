#!/usr/bin/env python

#Script to calculate statistics for fastq file.
import os, sys
import statistics
import argparse

parser = argparse.ArgumentParser(description="Fastq quality statistics")
parser.add_argument("-f", "--file", dest="filename",
                    help="Fastq input file", metavar="FILE")

args = parser.parse_args()
f = open(args.filename, 'r')
fl = open('fastq_stats.txt','w'); sys.stdout = fl

step = 4
with f as handle:
    all_reads_scores = []
    for linenum, line in enumerate(handle):
        if linenum % step == 3:
            read_scores = []
            trimmedline = line.rstrip('\r\n')
            for c in trimmedline:
                read_scores.append(ord(c) - 33)
            all_reads_scores.append(read_scores)
    print("Cycle\tAvg\tStdev")
    #Calculate average_scores
    average_scores = [statistics.mean(col) for col in zip(*all_reads_scores)]
    #Calculate std_dev_scores
    std_dev_scores = [statistics.stdev(col) for col in zip(*all_reads_scores)]
    for i in range(len(trimmedline)):
        print("%s\t%s\t%s\t" % (i+1,average_scores[i],round(std_dev_scores[i],3)))