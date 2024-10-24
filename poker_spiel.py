import random

## https://de.wikipedia.org/wiki/Poker für kombinationen und Wahrscheinlichkeiten

## High Card -- Keine der anderen Kombinationen
## One Pair -- Zwei Karten gleichen Wertes
## Two Pair -- Zwei Paare
## Three of a Kind -- Drei Karten gleichen Wertes
## Straight -- 5 Karten in einer Reihe
## Flush -- Fünf Karten in einer Farbe
## Full House -- Drilling und ein Paar
## Four of a Kind -- Vier Karten gleichen Wertes
## Straight Flush -- Straße in einer Farbe
## Royal Flush -- Straße in einer Farbe mit Ass als höchster Karte

karten_pro_farbe = 13
karten_satz = 52

def getcolor(karten_nummer):
    number = karten_nummer // karten_pro_farbe
    return number

def getnumber(karten_nummer):
    number = karten_nummer % karten_pro_farbe
    return number

def high_card(cards):
    return "true"

def one_pair(cards):
    for c1 in cards:
        for c2 in cards:
            if c2 != c1:
                if getnumber(c1) == getnumber(c2):
                    return "true"

def two_pair(cards):
    anzahl_wert = {}
    pairs = 0
    for c in cards:
        kartenwert = getnumber(c)
        if kartenwert in anzahl_wert:
            anzahl_wert[kartenwert] += 1
        else:
            anzahl_wert[kartenwert] = 1
    for count in anzahl_wert.values():
        if count == 2:
            pairs += 1
    if pairs == 2:
        return "true"
    return "false"

def three_of_a_kind(cards):
    anzahl_wert = {}
    for c in cards:
        kartenwert = getnumber(c)
        if kartenwert in anzahl_wert:
            anzahl_wert[kartenwert] += 1
        else:
            anzahl_wert[kartenwert] = 1
    for count in anzahl_wert.values():
        if count == 3:
            return "true"
    return "false"

def straight(cards):
    cardsnumbers = []
    for c in cards:
       cardsnumbers.append(getnumber(c))
    for i in range(1, len(cardsnumbers)):
        if cardsnumbers[i] - cardsnumbers[i - 1] != 1:
            return "false"
    return "true"

def flush(cards):
    for i in range(1, len(cards)):
        if getcolor(cards[i]) != getcolor(cards[i - 1]):
            return "false"
    return "true"

def full_house(cards):
    anzahl_wert = {}
    has_triple = False
    has_pair = False

    for c in cards:
        kartenwert = getnumber(c)
        if kartenwert in anzahl_wert:
            anzahl_wert[kartenwert] += 1
        else:
            anzahl_wert[kartenwert] = 1

    for count in anzahl_wert.values():
        if count == 3:
            has_triple = True
        elif count == 2:
            has_pair = True

    if has_triple and has_pair:
        return "true"
    return "false"

def four_of_a_kind(cards):
    anzahl_wert = {}
    for c in cards:
        kartenwert = getnumber(c)
        if kartenwert in anzahl_wert:
            anzahl_wert[kartenwert] += 1
        else:
            anzahl_wert[kartenwert] = 1
    for count in anzahl_wert.values():
        if count == 4:
            return "true"
    return "false"

def straight_flush(cards):
    if straight(cards) == "true" and flush(cards) == "true":
        return "true"
    return "false"

def royal_flush(cards):
    if straight_flush(cards) == "true" and getnumber(cards[0]) == 8:
        return "true"
    return "false"

def kartenziehung(karten_anzahl):
    cards = []
    for i in range(karten_anzahl):
        card = random.randint(0, karten_satz-1)
        while card in cards:
            card = random.randint(0, karten_satz-1)
        cards.append(card)
    if royal_flush(cards) == "true":
        return "Royal Flush"
    if straight_flush(cards) == "true":
        return "Straight Flush"
    if four_of_a_kind(cards) == "true":
        return "Four of a Kind"
    if full_house(cards) == "true":
        return "Full House"
    if flush(cards) == "true":
        return "Flush"
    if straight(cards) == "true":
        return "Straight"
    if three_of_a_kind(cards) == "true":
        return "Three of a Kind"
    if two_pair(cards) == "true":
        return "Two Pair"
    if one_pair(cards) == "true":
        return "One Pair"
    return "High Card"

def statistik(anzahl_spiele):
    kombinationen = {
        "High Card": 0,
        "One Pair": 0,
        "Two Pair": 0,
        "Three of a Kind": 0,
        "Straight": 0,
        "Flush": 0,
        "Full House": 0,
        "Four of a Kind": 0,
        "Straight Flush": 0,
        "Royal Flush": 0
    }
    for i in range(anzahl_spiele):
        kombination = kartenziehung(5)
        if kombination in kombinationen:
            kombinationen[kombination] += 1
        else:
            kombinationen[kombination] = 1
    
    print("Prozentuelle Anteile:")
    for key in kombinationen:
        kombinationen[key] = kombinationen[key] / anzahl_spiele * 100
    return kombinationen

def print_statistik(anzahl_spiele):
    statistik_resultat = statistik(anzahl_spiele)
    print(f"Statistik für {anzahl_spiele} Spiele:")
    for kombination, prozentsatz in statistik_resultat.items():
        print(f"{kombination}: {prozentsatz:.5f}%")


print_statistik(10000)

