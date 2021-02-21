
def Descending():
    """This function will sort the list in the Descending order"""
    list1 = [20, 30, 40, 920, 60]
    d_l = []
    c = 0
    l = len(list1)
    while c <= l:
        if c > 0:
            d_l.append(g)
            list1.remove(g)
        if c < l:
             g = list1[0]
        for i in list1:
            if g < i:
                g = i
        c += 1
    print("The Given List in the Descending order : ",d_l)
Descending()