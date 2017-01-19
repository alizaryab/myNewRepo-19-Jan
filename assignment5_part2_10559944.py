#Syed Ali Zaryab Assignment 5-2

#Here we are just changing the current directory to the onewhere this file is.
import sys
import os
ThisFileDirectory=os.path.dirname(sys.argv[0])
os.chdir(ThisFileDirectory)
print os.getcwd()

import math 
# values of example 1
T_e1= 800
Lambda_e1 = 3

#values of example 2
Lambda1_e2=0.4
Lambda2_e2=0.76
T_e2=2500

#values of example 3
theeta1_e3 = 50 *(math.pi/180)
theeta2_ex3 = 60*(math.pi/180)
r_ex3 = .75
dA_ex3= .0025

#importing the function file
import radiationCalculations_10559944 as rad 

#finding spectral Emissive Power
result_SpectralEmissivePower = rad.SpectralEmissivePower(Lambda_e1,T_e1)
print "The result is " + str(result_SpectralEmissivePower)


#finding Radiation Fraction
result_radiationFractions = rad.radiationFractions(Lambda1_e2,Lambda2_e2,T_e2 )
print "The Radiation Fraction is " +str(result_radiationFractions)


#finding View Factor for infinitesimal Area
result_viewFactorInfinitesimal = rad.viewFactorInfinitesimal(theeta1_e3,theeta2_ex3,r_ex3,dA_ex3 )
print "The view Factor for Infinitesimal Area is "+ str (result_viewFactorInfinitesimal)