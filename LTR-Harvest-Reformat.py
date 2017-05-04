#!/usr/bin/env python
#python 2.7.5
#LTR-Harvest-Reformat.py
#Version 1. Adam Taranto, May 2017
#Contact, Adam Taranto, adam.taranto@anu.edu.au

######################################################
# Correct sequence names in LTR_Harvest GFF3 output. #
######################################################
import os
import argparse

def dochecks(args):
	# Make outDir if does not exist, else set to current dir.
	if args.outDir:
		tempPathCheck(args)
		outDir = args.outDir
	else:
		outDir = os.getcwd() 
	# Get custom GFF output name, else keep current name.
	if args.gffOut:
		newGFF = os.path.basename(args.gffOut)
	else:
		newGFF = os.path.basename(args.infile)
	return os.path.join(outDir,newGFF)

def tempPathCheck(args):
	absOutDir = os.path.abspath(args.outDir)
	if not os.path.isdir(absOutDir):
		os.makedirs(absOutDir)

def mapNames(infile):
	keys = list()
	values = list()
	hashStr = '#'
	f = open(infile,"r")
	for line in f.readlines():
		if line.split()[0] == '##gff-version':
			continue
		elif line.split()[0] == '##sequence-region':
			keys.append(line.split()[1])
		elif line.split()[0][0] == '#':
			values.append(line.split()[0].strip(hashStr))
		else:
			break
	f.seek(0)
	f.close()
	replacements = dict(zip(keys, values))
	# Alternative method: Make pairs into reverse sorted (on oldname) list of tuples so that large numbers come before smaler ones within them to avoid errors i.e. Seq34 before Seq3
	#replacements = dict(zip(keys, values))
	#replacements = list(replacements.items())
	#replacements.sort(key=lambda x: x[0],reverse=True)
	return replacements

def fixGFF(infile,outPath,replacements):
	lines = list()
	# Read and correct lines from original GFF file
	with open(infile,'r') as infile:
		for line in infile:
			if line.split()[0] == '##sequence-region':
				lines.append(line.replace(line.split()[1],replacements[line.split()[1]]))
			elif line.split()[0][0] == '#':
				lines.append(line)
			elif len(line) > 0:
				lines.append(line.replace(line.split()[0],replacements[line.split()[0]]))
	# Write corrected lines to output file
	with open(outPath, 'w') as outfile:
		for newline in lines:
			outfile.write(newline)

def mainArgs():
		parser = argparse.ArgumentParser(
				description='Correct sequence names in LTR_Harvest GFF3 output.',
				prog='LTR-Harvest-Reformat')
		parser.add_argument('--version',
									action='version',
									version='LTR-Harvest-Reformat-0.0.1')
		parser.add_argument('-i','--infile',
									type=str,
									required=True,
									help='GFF3 file from LTR_Harvest.')
		parser.add_argument('-d','--outDir',
									type=str,
									default=None,
									help='Optional: Set output directory.')
		parser.add_argument('-o','--gffOut',
									type=str,
									default=None,
									help='Optional: Set alternative name for output file.')
		args = parser.parse_args()
		return args

def main(args):
	# Check existence of output directory
	outPath = dochecks(args)
	# Read in name pairs from LTR_Harvest GFF3 file
	replacements = mapNames(args.infile)
	# Write corrected lines to output file
	fixGFF(args.infile,outPath,replacements)

if __name__== '__main__':
	args = mainArgs()
	main(args)