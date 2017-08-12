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

sayi = "10"
dizi = [int(i) for i in sayi]
test = krl.bolunebilme_kurallar(dizi)
print(test.iki_ile())
print(test.on_ile())
print(test.uc_ile())
