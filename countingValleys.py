def countingValleys(steps, path):
    currentLevel=0
    valleys=0
    for i in range(steps):
        if path[i]== "D" and currentLevel==0:
            valleys+=1
            
        if path[i] == "D":
            currentLevel-=1
        elif path[i]== "U":
            currentLevel+=1    
        
    return valleys