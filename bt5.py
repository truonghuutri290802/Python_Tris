n = int(input())
def tinh_tong(n):
 	lst = []
 	for i in range(1,n):
 		if n%i == 0:
 			lst.append(i)
 	return lst
print(sum(tinh_tong(n)))
x = n
def textsa(x):
	xau=[]
	for j in (1,x):
		if n%j == 0:
			xau.append(j)
	s = sum(xau)
	if s<=x:
		return "false"
	return "true"

print(textsa(x))