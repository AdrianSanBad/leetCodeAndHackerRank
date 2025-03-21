def jumpingOnClouds(c):
    place=0
    jumps=0
    for i in range(len(c)):
        if place==len(c)-2:
            place+=1
            jumps+=1
        if place==len(c)-1:
            return jumps
            break
        if c[place+2]==0:
            place+=2
            jumps+=1
        else:
            place+=1
            jumps+=1