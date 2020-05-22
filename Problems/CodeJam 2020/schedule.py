#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 07 11:44:33 2020

@author: Akash Tyagi
"""
# Question: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9


'''
Approach:

We have to assign jobs such that if one person is already doing a job, other person should do it & if both are busy, then Impossible.

The easiest way is to sort jobs in increasing order of their start time .
Why ?
Because doing this make sure that next job cannot begin earlier than the job already happening. So we only have to check if 
new job starts only after the end-time of previous job. This make sure that no job occurs in-between the time interval of previous job.
''' 

def scheduler(x):
	ds = []
	for i,tup in enumerate(x):	
		tup.append(i)	# Adding index position with every job so after sorting we can identify their actual position.
		ds.append(tup)

	new_list = sorted(ds) # Sorts all job on basis of first parameter.

	out = [0]*len(x)
	c,j = [],[] # Two person C & J, both can have simultaneous jobs at a time.

	cend = None # To keep track of last job's end time.
	jend = None

	for job in new_list:
		if len(c)==0: # If first or second job
			c.append(job)
			cend = job[1]
			out[job[2]] = "C" # Add Person name to actual position of job in array.

		elif len(j)==0: # If first or second job
			j.append(job)
			jend = job[1]
			out[job[2]] = "J"

		elif cend is not None and job[0]>=cend: # If the start time of job is after end time of previous job for C.
			out[job[2]] = "C"
			cend = job[1]

		elif jend is not None and job[0]>=jend:
			out[job[2]] = "J"
			jend = job[1]
		else:	# No person is free for new job at the moment.
			out = "IMPOSSIBLE"
			break

	if isinstance(out,list): 
		answer = "".join(out)
	else:
		answer = out 

	return answer



if __name__ == "__main__":
	x = [[360, 480],
	[420, 540],
	[600, 660]]

	# x = [[0, 1440],
	# [1, 3],
	# [2, 4]]

	# x = [[99, 150],
	# [1, 100],
	# [100, 301],
	# [2, 5],
	# [150,250]]

	# x = [[0,770],
	# 	 [770,1440]]
	print("Jobs: ",x)
	print("Jobs Assigned: ",scheduler(x))

