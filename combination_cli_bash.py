#!/bin/env python
#--*-- coding: utf-8 --*--

import datetime
import os
import sys

def write_brief(brief_path):
	ret = cli("netstat -nlpt")
	f = open(brief_path, "w")

if __name__ == '__main__' :
	term = input("input seconds : ")
	count = input("the count to compare : ")
	
	brief_dir = "/tmp/diff"

	if not os.path.isdir(brief_dir):
		os.mkdir(brief_dir)

	cnt = 1
	while cnt <= count :
		start_time = datetime.datetime.now()
		end_time = start_time + datetime.timedelta(seconds = term)
		now = datetime.datetime.now()

		brief_path1 = "/tmp/breif.txt"
		brief_path2 = "/tmp/brief2.txt"

		write_brief(brief_path1)

	test_time = datetime.datetime.now()
	print test_time
