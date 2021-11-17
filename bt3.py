def action(lst):
	chuoi = []
	for i in lst:
		if i not in chuoi:
			chuoi.append(i)
	return chuoi

n = int(input())
lst = []
for j in range(n):
	lst.append(int(input()))
print(action(lst))

def ktra_songuyento(n):
	dem = 0
	for i in range(1, n+1):
		if n%i == 0:
			dem+=1
	if dem ==2:
		return True
	return False
n= int(input())
print(ktra_songuyento(n))

def UCLN(a,b):
	if b == 0:
		return a
	return UCLN(b,a%b)
a = int(input())
b = int(input())
print (UCLN(a,b))
'''
cach khac de tim UCLN:
def UCLN(a,b):
	uoc =[]
	ktra =[]
	for i in range(1 , n+1):
		if a % i ==0:
			uoc.append(i)
	for j in uoc:
		if b % j == 0:
			ktra.append(j)
	return max(ktra)

a = int(input())
b = int(input())
print(UCLN(a,b))

'''
x = int(input())
y = int(input())
z = int(input())

if x== y and y ==z :
	print ("tam giac deu")
if x== y or x == z :
	print("tam giac can")
else: print("tam giac thuong")
