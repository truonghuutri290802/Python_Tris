
def vuongcan(n):
	for i in range(0,n):
		s=1
		for j in range(0,i+1):
			print(s,end=" ")
			s=s+1
		print("\n")
n = int(input())
print(vuongcan(n))