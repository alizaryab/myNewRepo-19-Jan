#Syed Ali Zaryab Radiation Calculation assignment 5-2 Module


import math

c0 = 2.9979*10**8 #m/s speed of light in vacuum
h_Plank=6.626069*10**-34 #J.s Plank's Constant
sigma_stefan_Boltzmann= 5.67*10**-8 #Stefan-Boltzmann Constant
k_Boltzmann=1.38065*10**-23 #J/K Boltzmann Constant
C1=2*math.pi*h_Plank*c0**2*(10**24)#J*s*m^2/s^2--W*m2 --->W 
C2=h_Plank*c0/k_Boltzmann*(10**6) #microm m/K

    
def SpectralEmissivePower(Lambda, T):
    #Constants
    """This function takes Value of Lambda in (micro m) and T in (kelvin)  in this order (lambda,T) """
   
    totalEmissivePower = sigma_stefan_Boltzmann*T**4
    spectralEmissivePower = C1/((Lambda**5)*(math.exp(C2/(Lambda*T))-1))
    
    CalculationOutPut = {"totalEmissivePower":totalEmissivePower,"spectralEmissivePower":round(spectralEmissivePower,2)}
    return CalculationOutPut
    
    
def radiationFractions(Lambda1,Lambda2,T):
    """This function takes Value of Lambda1 in (micro m), Lambda2 in (micro m) and T in (kelvin)  in this order (lambda1,lambda2, T) """
   # This while loop would star from lambda1 and go to lambda2 where it would add all values of area under curve
    
    areaE=0 ##area under the curve of E_spec for lambda = .0001
    E_spec=0 # value of E
    EL1_L2 = 0   # this would five the total value of E from lambda1 to lambda2
    LNow1 = Lambda1
    while LNow1<=Lambda2: 
        E_spec= SpectralEmissivePower (LNow1,T) ["spectralEmissivePower"]
        areaE = E_spec*0.0001 # to find area under curve
        EL1_L2 = EL1_L2 +areaE # adding all areas
        LNow1 =LNow1 +0.0001 #increasing lambda values
# Getting total emissive power from the func SpectralEmissivePower defined above
    totalEmissivePower = SpectralEmissivePower (LNow1,T) ["totalEmissivePower"]
# Dividing the total sum of area under curve with total emissive power
    radiation_fraction= EL1_L2/totalEmissivePower

    return radiation_fraction

    
def viewFactorInfinitesimal(theeta1,theeta2, r, dA):
    """This function takes Value of theeta1 (angle with normal first surface from which 2nd surface is being viewed) in (degrees) ,
    theeta2 (angle with normal of second surface) in (degrees)  and distance (r) between two area in (m), 
    and the area (da) of the infatisimal surface in m^2 in this order (theeta1,theeta2, r, da)
    -This function would find viewfactor from first surface to the second, where first surface has angle theeta 1 with normal"""
    # formula of view factor for an infinitesimal surface
    viewFactorInfi = ((math.cos (theeta1))* (math.cos (theeta1))*dA)/((math.pi)*r**2) 
    return viewFactorInfi