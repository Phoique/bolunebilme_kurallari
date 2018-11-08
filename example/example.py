import sys
sys.path.append("../calculation")
import sys;sys.path.append("calculation")
import calculation 

print("""
 _____  _           _                     ______ 
|  __ \| |         (_)                  |____  |
| |__) | |__   ___  _  __ _ _   _  ___      / / 
|  ___/| '_ \ / _ \| |/ _` | | | |/ _ \    / /  
| |    | | | | (_) | | (_| | |_| |  __/   / /   
|_|    |_| |_|\___/|_|\__, |\__,_|\___   /_/    
                         | |                 
                         |_|                 
""")

number = 12

test = calculation.remainingCalculation(number)

print(test.all())