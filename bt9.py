n = input()
def multiplication_of_luckynumber(n):
    s = str(n)
    if '4' in s:
        return -1
    if len(str(n))> 4 or int(s[0])*int(s[-1]) != 4:
        return  int(s[0])*int(s[-1])

    else: 
        return -1
print(multiplication_of_luckynumber(n))