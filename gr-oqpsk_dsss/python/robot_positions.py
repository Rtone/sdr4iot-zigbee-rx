import numpy as np
from gnuradio import gr
import csv
import urllib2

from time import time
from struct import pack, unpack
from datetime import datetime, timedelta
import sys

#Get robot positions
def get_pos_robot(num):
	RobNum='  '+':id: '+str(num)
	position = urllib2.urlopen('http://robotcontrol.wilab2.ilabt.iminds.be:5056/Robot/LocationsYaml')
	posread = position.read()
	posplit = posread.split('\n')
	ind=posplit.index(RobNum)
	location=[posplit[ind+1][6:],posplit[ind+2][6:],posplit[ind+6][10:]]
	return location	
def Record_IQ_pos(start,end,num,csvfile):
	    try:
		t=datetime.now()
		location=get_pos_robot(num)
		#dict[t]=[location,trameInd]
		with open(csvfile, 'a+') as file:
				writer = csv.writer(file)
				writer.writerow([t,num,start,end,location[0],location[1],location[2]])#time,robot number,start,end,x,y,angle
	    except IOError:
		pass


if __name__ == '__main__':
	 Record_IQ_pos(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),sys.argv[4])
