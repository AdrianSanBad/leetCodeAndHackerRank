def sockMerchant(n, ar):
    # Write your code here
    number_of_socks_by_color={}
    pairs=0
    
    #generate list by number
    for i in range(n):
        if ar[i] not in number_of_socks_by_color:
            number_of_socks_by_color[ar[i]]=0
    #count all the socks by color
    for i in ar:
        number_of_socks_by_color[i]+=1
    for i in number_of_socks_by_color.values():
        pairs+=i//2
    return pairs