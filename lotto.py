import random

def lottoziehung():
    zahlen = list(range(1, 46))
    gezogene_zahlen = random.sample(zahlen, 6)
    gezogene_zahlen.sort()
    return gezogene_zahlen

def statistik_lotto(anzahl_ziehungen):
    statistik = {zahl: 0 for zahl in range(1, 46)}
    
    for _ in range(anzahl_ziehungen):
        gezogene_zahlen = lottoziehung()
        
        for zahl in gezogene_zahlen:
            statistik[zahl] += 1
    
    return statistik

anzahl_ziehungen = 1000

statistik = statistik_lotto(anzahl_ziehungen)

for zahl, haeufigkeit in statistik.items():
    print(f"Zahl {zahl} wurde {haeufigkeit} mal gezogen.")
