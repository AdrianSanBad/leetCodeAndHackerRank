def repeatedString(s, n):
    contador=0
    for i in s:
        if i=="a":
            contador+=1
    veces=n//len(s)
    restantes=n%len(s)
    contador *= veces
    for i in s[:restantes]:
        if i=="a":
            contador+=1
    return contador