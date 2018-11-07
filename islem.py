import kurallar as krl # Yazdığımız bölünebilme kuralları modülünü dahil ettik.

"""
 _____  _           _                     ______ 
|  __ \| |         (_)                  |____  |
| |__) | |__   ___  _  __ _ _   _  ___      / / 
|  ___/| '_ \ / _ \| |/ _` | | | |/ _ \    / /  
| |    | | | | (_) | | (_| | |_| |  __/   / /   
|_|    |_| |_|\___/|_|\__, |\__,_|\___   /_/    
                         | |                 
                         |_|                 
"""

sayi = 10

test = krl.bolunebilme_kurallar(sayi)
print(test.two())
print(test.ten())
print(test.three())
