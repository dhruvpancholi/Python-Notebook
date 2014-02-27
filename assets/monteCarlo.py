import random
import math
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
	while sDev>=precision/2.0:
		(curEst,sDev)=getEst(numNeedles,numTrials)
		numNeedles*=2
	return curEst

  
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

############################################
## Python Project on Natural Convection
## Name: Dhruv Pancholi
## Roll No: 11110028
############################################

############################################
## About this module
## This module is used to simulate the boundary layer thicknes and the temperature
## for the given system, this is a completely object oriented approach and with
## resuable data attributes
############################################

# import numpy as np
# import pylab
# import matplotlib as plot
# import matplotlib.pyplot as pl
from math import *

############################################
## Class definition of Vertical Plate
############################################

class verticalPlate(object):
	"""docstring for verticalPlate:
		The class which will be used for instantiating the Vertical Plate"""
	def __init__(self, Tw, Tinf):
		""" This is the instantiating method, which initially assigns the value to the variables
		"""
		super (verticalPlate, self).__init__()
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = 25.23E-6
		self.ro = 0.898
		self.Cp=1.013E3
		self.K=0.0328
		self.beta = 2.55E-3
		self.g=9.8
		self.L=1
		self.Pr=0.7
		
	def getBoundary(self,x):
		"""This function is caled when we need to get the boundary layer layer thickness of the given system"""
		num=x*240.0*(20.0/21.0+self.getPrandtlNumber())
		den=((self.getPrandtlNumber()**2)*self.g*self.beta*fabs(self.Tw-self.Tinf))/self.Mu**2
		return (num/den)**0.25
	
	def getgrashofNumber(self,x):
		return (self.L**3*self.ro**2*self.g*self.beta*((self.Tw)-(self.Tinf)))/(self.Mu**2)
	
	# def plotBoundary(self):
	# 	"""This function is called when we need to plot the boundary  of the given system"""
	# 	pl.clf()
	# 	x=[];y=[]
	# 	y=np.linspace(0,self.L,100)
	# 	for i in y:
	# 		x.append(self.getBoundary(i))
	# 	pl.plot(x,y,'r',label='Boundary Layer')
	# 	pl.xlabel("y")
	# 	pl.ylabel("x")
	# 	pl.title("Boundary Layer of Vertical Plate")
	# 	pl.show()

	# def plotTemperature(self):
	# 	"""This function needs to be called when we want to plot the temperature profile for the given system"""
	# 	x=[]
	# 	T=[]
	# 	v=[]
	# 	y=np.linspace(0,self.getBoundary(self.L),100)
	# 	for i in range(y.__len__()):
	# 		T.append((1-(y[i]/self.getBoundary(self.L)))**2)
	# 		x.append(y[i]/self.getBoundary(self.L))
	# 	fig,ax=pl.subplots()
	# 	aArray=pylab.array(x)
	# 	bArray=pylab.array(T)
	# 	ax.plot(aArray,bArray,'b-',label='Temperature (T-Tinf)/(Tw-Tinf)')
	# 	# plotting the velocity
	# 	for i in range(y.__len__()):
	# 		v.append((y[i]/self.getBoundary(self.L))*T[i])
	# 	cArray=pylab.array(v)
	# 	ax.plot(aArray,cArray,'r-',label='Velocity u/u(x)')
	# 	legend = ax.legend(loc='upper right', shadow=False)
	# 	pl.xlabel('Dimensionless boundary layer thickness')
	# 	pl.ylabel('Dimensioless Temperature or Velocity')
	# 	pl.title('Temperature and Velocity profiles')
	# 	pl.show()

        # Some of the common setters and getter, which will be used to change the properties of the system
	def getPrandtlNumber(self):
		return self.Pr
	def setWallTemperature(self, x):
		self.Tw=x
	def setAmbientTemperature(self,x):
		self.Tinf=x
	def setLength(self,x):
		self.L=x
	def setViscosity(self,x):
		self.Mu=x
	def setBeta(self,x):
		self.beta=x
	def setSpecificHeatCapacity(self, x):
		self.Cp=x
	def setThermalConductivity(self, x):
		self.K=x
	def getRayleighNumber(self):
		return self.getgrashofNumber(self.L)*self.getPrandtlNumber()
	def setProperties(self, Tw, Tinf,L, Mu, ro, beta, Cp, K,Pr):
		"""The function which can be used to set the properties of the system all at once"""
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = Mu
		self.ro = ro
		self.beta = beta
		self.g=9.8
		self.L=L
		self.Cp=Cp
		self.K=K
		self.Pr=Pr
	def getH(self):
		return (self.K/self.L)*(0.825+(0.387*self.getRayleighNumber()**(1.0/6.0))/(1+(0.492/self.getPrandtlNumber())**(9.0/16.0))**(8.0/27.0))**2
	
	# def plotData(self):self.plotBoundary();self.plotTemperature()
	# """This function is used to display both the plots at the same time"""

############################################
## End of class definition
############################################

############################################
## Class definition of Horizontal Cylinder
############################################

class horizontalCylinder(object):
	"""docstring for Horizontal Cylinder:
		The class which will be used for instantiating the Horizontal Cylinder"""
	def __init__(self, Tw, Tinf):
		""" This is the instantiating method, which initially assigns the value to the variables
		"""
		super (horizontalCylinder, self).__init__()
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = 25.23E-6
		self.ro = 0.898
		self.Cp=1.013E3
		self.K=0.0328
		self.beta = 2.55E-3
		self.g=9.8
		self.L=1
		self.Pr=0.7
			
	def getgrashofNumber(self,x):
		return (self.L**3*self.ro**2*self.g*self.beta*((self.Tw)-(self.Tinf)))/(self.Mu**2)
	
        # Some of the common setters and getter, which will be used to change the properties of the system
	def getPrandtlNumber(self):
		return self.Pr
	def setWallTemperature(self, x):
		self.Tw=x
	def setAmbientTemperature(self,x):
		self.Tinf=x
	def setLength(self,x):
		self.L=x
	def setViscosity(self,x):
		self.Mu=x
	def setBeta(self,x):
		self.beta=x
	def setSpecificHeatCapacity(self, x):
		self.Cp=x
	def setThermalConductivity(self, x):
		self.K=x
	def getRayleighNumber(self):
		return self.getgrashofNumber(self.L)*self.getPrandtlNumber()
	def setProperties(self, Tw, Tinf,L, Mu, ro, beta, Cp, K,Pr):
		"""The function which can be used to set the properties of the system all at once"""
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = Mu
		self.ro = ro
		self.beta = beta
		self.g=9.8
		self.L=L
		self.Cp=Cp
		self.K=K
		self.Pr=Pr
	def getH(self):
		return (self.K/self.L)*(0.60+(0.387*self.getRayleighNumber()**(1.0/6.0))/(1+(0.559/self.getPrandtlNumber())**(9.0/16.0))**(8.0/27.0))**2
	

############################################
## End of class definition
############################################

############################################
## Class definition of Sphere
############################################

class sphere(object):
	"""docstring for sphere:
		The class which will be used for instantiating the sphere"""
	def __init__(self, Tw, Tinf):
		""" This is the instantiating method, which initially assigns the value to the variables
		"""
		super (sphere, self).__init__()
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = 25.23E-6
		self.ro = 0.898
		self.Cp=1.013E3
		self.K=0.0328
		self.beta = 2.55E-3
		self.g=9.8
		self.L=1
		self.Pr=0.7
			
	def getgrashofNumber(self,x):
		return (self.L**3*self.ro**2*self.g*self.beta*((self.Tw)-(self.Tinf)))/(self.Mu**2)
	
        # Some of the common setters and getter, which will be used to change the properties of the system
	def getPrandtlNumber(self):
		return self.Pr
	def setWallTemperature(self, x):
		self.Tw=x
	def setAmbientTemperature(self,x):
		self.Tinf=x
	def setLength(self,x):
		self.L=x
	def setViscosity(self,x):
		self.Mu=x
	def setBeta(self,x):
		self.beta=x
	def setSpecificHeatCapacity(self, x):
		self.Cp=x
	def setThermalConductivity(self, x):
		self.K=x
	def getRayleighNumber(self):
		return self.getgrashofNumber(self.L)*self.getPrandtlNumber()
	def setProperties(self, Tw, Tinf,L, Mu, ro, beta, Cp, K,Pr):
		"""The function which can be used to set the properties of the system all at once"""
		self.Tw = Tw
		self.Tinf = Tinf
		self.Mu = Mu
		self.ro = ro
		self.beta = beta
		self.g=9.8
		self.L=L
		self.Cp=Cp
		self.K=K
		self.Pr=Pr
	def getH(self):
		return (self.K/self.L)*(2.0+(0.589*self.getRayleighNumber()**(1.0/4.0))/(1+(0.469/self.getPrandtlNumber())**(9.0/16.0))**(4.0/9.0))
	

############################################
## End of class definition
############################################

# vP=verticalPlate(100.0,10.0)
# vP.plotBoundary()
# vP.plotTemperature()
# vP.plotData()
# sp=sphere(100.0,10.0)
# print sp.getH()
#############################################################################################################################################
#For Zeta vs log10(Pr) graph, consider some point x(say x=5)
#############################################################################################################################################
