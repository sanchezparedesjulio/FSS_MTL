import math, cmath
from platform import python_branch
import numpy as np

from pyaedt import Hfss
from pyaedt import Q2d

#functions
def generate_Lf_n(Lf,Lf_type, X=0.5, num_values=5):
    # Check if Wf_type is an integer within the allowed range
    if not isinstance(Lf_type, int) or Lf_type not in [0, 1, 2, 3]:
        raise ValueError("Wf_type must be an integer: 0, 1, 2, or 3.")
    
    # Check if X is a float or int and within the range [0, 1]
    if not isinstance(X, (float, int)) or not (0 <= X <= 1):
        print("X value out of range or invalid type. Setting X to default value 0.5.")
        X = 0.5
    
    # Check if num_values is a positive integer and within a reasonable range
    if not isinstance(num_values, int) or num_values <= 0 or num_values > 100:
        print("num_values must be a positive integer within a reasonable range. Setting to default value 5.")
        num_values = 5

    # Assign values to wf_n based on Wf_type
    if Lf_type == 0:
        # Default values
        Lf_n = Lf*[1, 0.94, 0.92, 0.9, 0.88, 0.86, 0.84]
        
    elif Lf_type == 1:
        # Linear values between 1 and X
        Lf_n = Lf*np.linspace(1, X, num=num_values).tolist()
        
    elif Lf_type == 2:
        # Parabolic values between 1 and X
        Lf_n = Lf*(1 - (1 - X) * (np.linspace(0, 1, num=num_values) ** 2)).tolist()
        
    elif Lf_type == 3:
        # Exponential decreasing values between 1 and X
        # Added condition to avoid calculation errors if X is 0
        Lf_n = Lf*(1 - (1 - max(X, 0.01)) * (1 - np.exp(-np.linspace(0, 1, num=num_values)))).tolist()
        
    return Lf_n



## ToDo
# 1) FSS N+M
#   1.0) Generic FSS N + M conductors(------)


projectName = "FSSQ2D" # Change name for a new project
designName  = "Microstrip Q2D "    # Name for HFSS file
designQ2Dname = "Microstrip Q2D s-8"      # Name for Q2D file

## Global variables
mu0 	= 4*math.pi*1e-7             
eps0 	= 8.85418*1e-12
c0 		= 1/math.sqrt(eps0*mu0)
mm 		= 1e-3
cm 		= 1e-2
GHz 	= 1e9

## Project variables
freq_res 	= 14 * GHz		# Hz
lambda_res 	= c0 / freq_res

# Variables to control the flow of the program
Q2design = 1 # If 1 the Q2D file is generated, if 0 the HFSS    <<<<----

hfss= Hfss(projectName, designName)
if Q2design ==1:
    q2d  = Q2d(projectName, designQ2Dname)
    #q2db = Q2d(projectName, designQ2Dname + "B")  

## Variables for geometry
N = 4  # Number of top layer fingers    <<<------
M = 4  # Number of output fingers  <<<------
Nb = 2  # Number of parallel bondings  <<<------# (2.0)future WB

# Declaration of numeric variables as needed for some calculations as wave port creation
    #Cell Parameters
gx= 7    #X length of the cell in mm
gy= 7   #Y length of the cell in mm
Zlen= 30 #Z size of the cell in mm
    #Dipole Parameter
T = 0.032   #Thick of metallization in mm
Lf=5.9  #length of first finger in mm
Lf_type=0   #value of Wf
Lf_list=generate_Lf_n(Lf,Lf_type,X=0.8,num_values=N+M)
desp= 0.7   #separation between fingers in mm
sep=0.6     #separation between layers
Wf1=0.5      #finger 1 width
Wf2=0.4     #finger 2 width
Wf3=0.4     #finger 3 width

q2d["Wf1"] = str(Wf1)+"mm"
q2d["Wf2"] = str(Wf2)+"mm"
q2d["Wf3"] = str(Wf3)+"mm"
q2d["T"] = str(T)+"mm"
q2d["desp"] = str(desp)+"mm"
q2d["sep"] = str(sep)+"mm"