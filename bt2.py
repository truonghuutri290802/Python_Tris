def tinh_tong(lst):
	sumoric = 0
	for v in lst:
		sumoric += v
	return sumoric
lst= []
n=int(input())
for i in range (n):
 	lst. append(int(input()))
print(tinh_tong(lst))

def so_lon_nhat(a, b, c):
	if a>b and a>c:
		return a
	return b if b>c else c 
a= int(input())
b= int(input())
c= int(input())	
print(so_lon_nhat(a,b,c))	

def show(s):
	dem_chuhoa = 0
	dem_chuthuong = 0
	for j in s:
		if j.isupper():
			dem_chuhoa += 1
		if j.islower():
			dem_chuthuong += 1
	print("Chuoi vua nhap :",s)
	print("So chu cai hoa:",dem_chuhoa)
	print("So chu thuong:",dem_chuthuong)
s = str(input())
print(show(s))
