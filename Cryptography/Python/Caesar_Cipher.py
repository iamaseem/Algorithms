l = {27:" ", 1:"a", 2:"b", 3:"c", 4:"d", 5:"e", 6:"f", 7:"g", 8:"h", 9:"i", 10:"j", 11:"k", 12:"l", 13:"m", 14:"n", 15:"o", 16:"p", 17:"q", 18:"r", 19:"s", 20:"t", 21:"u", 22:"v", 23:"w", 24:"x", 25:"y",26:"z"}

inst = input("Enter The String:")
pad = 3

for i in inst:
    for x, y in l.items():
        if y == i:
            n = x
            break
    if n == 27:
        print("",end=" ")
        continue
    n = n-1
    e = (n+pad)%26
    print(l[e],end="")