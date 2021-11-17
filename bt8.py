n = int(input("Nhap n:"))
def check_number(n):
    xau = []
    for i in str(n):
        xau.append(i)
    if len(set(xau)) == len(str(n)):
        return True
    else:
        return False
       
print(check_number(n))
def check_special_number(n):
    n = list(str(n))
    n.sort()
    #print(n)
    a = list(set(n));
    if len(a) != len(n):
        return False
    for i in range(len(n)):
        if i in n and i not in a:
            return False
    return True
print(check_special_number(n))
