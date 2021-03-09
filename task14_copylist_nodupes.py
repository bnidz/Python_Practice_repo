#task14 first and last from list

a = [5, 10, 15, 20, 25, 15, 15, 30, 6, 6, 6, 7]

def NoDupes (a):
    b=[]
    for elem in a:
        if elem not in b:
            b.append(elem)
    return[b]

print(NoDupes(a))
#prints b
