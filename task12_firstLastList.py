#task12 first and last from list

a = [5, 10, 15, 20, 25]
b = list()

def FirstAndLastfromList (a):
    #first
    b.append(a[0])
    #last
    b.append(a[-1])
    return[b]

print(FirstAndLastfromList(a))
#prints b
