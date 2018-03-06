#---------------------------------------------------
# Name:       lambdaplotter.py
# Purpose:    plotter to be used with lambda simulations
#
#
# Author:      soumya
#
# Created:    24/10/2017
#---------------------------------------------


import matplotlib.pyplot as plt
import json
import numpy as np
import problib as pl
import pandas as pd
from scipy import stats, integrate
import polarconstruct as pcon
import lambdathreshold as lmb
import math as ma
import matlib as ml

#plt.rc('text', usetex=True)
#plt.rc('font', family='serif')


import seaborn as sns
sns.set(color_codes=True)

#-------------------------------------------polar_channel_FERvsR

#to be automated

#filename1="./simresults/llrsgndict-1024-0p04-17-11-23_17-28-36.txt"
filename="./simresults/llrsgndict-1024-0p04-18-02-15_14-58-19.txt"
LLRdict=lmb.load_LLRdict(filename)
N=1024
design_p=0.04
runsim=1
channel_plist=[0.04]#,0.15,0.2,0.25]
skip=99
C=pl.CapacityBSC(N,design_p)
G=int(C)
F=N-G
color=["red","blue","green","yellow"]

plt.figure(1)
j=0

#print len(range(F))

for channel_p in channel_plist:
	j+=1
	#plt.figure(j)
	for i in range(runsim):
		
		LLRchannels=LLRdict[str(channel_p)][i][0]#[G:]
		SentBitchannels=LLRdict[str(channel_p)][i][1]#[G:]
		presentIrv=[ml.logdomain_sum(0,llr*(2*int(sentbit)-1)) for llr,sentbit in zip(LLRchannels,SentBitchannels)]
		
		#print len(presentIrv)
		plt.scatter(range(N)[::skip+1],[llr/3000 for llr in LLRchannels][::skip+1],color=color[j-1])
		plt.scatter(range(N)[::skip+1],[int(sb) for sb in SentBitchannels][::skip+1],color='k')
		#plt.xticks(index,RI,rotation="vertical")
		
	#plt.hold(True)
	plt.title("LLR for 0.04 , compound_channel=[0.04,0.15,0.2,0.25]")


plt.show();




