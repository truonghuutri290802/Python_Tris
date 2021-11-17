lst = [2,6,1,4,7,5]
#tang dan
lst.sort()
print(lst)
#giam dan 
a = lst
#c1:lst.sort(reverse=True)
lst.reverse()
print(a) 

chuoi = []
n = int(input("Moi nhap so luong phan tu:"))
for i in range(n):
	print("ptu thu",i)
	chuoi.append(int(input()))
print(chuoi)
aham = []	
for j in chuoi :
	if j%2 != 0:
		aham.append(j)
print(aham)

