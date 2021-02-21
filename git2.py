def Ascending():
    """This function will sort the list in the Ascending order"""
    list1 = [20, 30, 40, 110, 60]
    a_l = []
    c = 0
    l = len(list1)
    while c <= l:
        if c > 0:
            a_l.append(s)
            list1.remove(s)
        if c < l:
            s = list1[0]
        for i in list1:
            if s > i:
                s = i
        c += 1
    print("The Given List in the Ascending Order : ",a_l)
Ascending()