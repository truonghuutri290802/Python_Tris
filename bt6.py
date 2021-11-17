n = int(input("nhap so luong phan tu:"))
lst= []
for i in range(n):
	lst.append(int(input()))
def sum_numbers_larger_average(lst):
	TBC = sum(lst)/len(lst)
	sm=0
	for i in lst:
		if i>TBC :
			sm+=i
	if sm != 0:
	    return sm		
	return -1
print(sum_numbers_larger_average(lst))
