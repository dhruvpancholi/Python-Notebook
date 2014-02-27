import math
import random
import time
def printTheValue():
	print random.random()
#printTheValue()

# Calculate mean of the values  
def mean(values):  
        size = len(values)  
        sum = 0.0  
        for n in range(0, size):  
                sum += values[n]  
        return sum / size;  
  
# Calculate standard deviation  
def standardDeviation(values, mean):  
        size = len(values)  
        sum = 0.0  
        for n in range(0, size):  
                sum += math.sqrt((values[n] - mean)**2)  
        return math.sqrt((1.0/(size-1))*(sum/size))

def throwNeedles(numNeedles):
	inCircle=0
	for Needles in xrange(1,numNeedles+1,1):
		x=random.random()
		y=random.random()
		if (x*x+y*y)**0.5 <=1.0:
			inCircle+=1
	return 4*(inCircle/float(numNeedles))
def getEst(numNeedles,numTrials):
	estimates=[]
	for t in range(numTrials):
		piGuess=throwNeedles(numNeedles)
		estimates.append(piGuess)
	stdDev=standardDeviation(estimates,mean(estimates))
	curEst=sum(estimates)/len(estimates)
	print 'Est.= ',str(curEst),', std Dev.= ',str(stdDev),', Needles.=',str(numNeedles)
	return (curEst,stdDev)
def estPi(precision, numTrials):
	numNeedles=1000
	sDev=precision
	startTime=time.time()
	while sDev>=precision/2.0:
		(curEst,sDev)=getEst(numNeedles,numTrials)
		print 'Time taken to run: ',time.time()-startTime
		startTime=time.time()
		numNeedles*=2
	return curEst
estPi(0.01,1000)
