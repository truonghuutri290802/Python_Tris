chuoi = str(input())

def duyet_chuoi():
	text= chuoi.split()
	lst = []
	for i in text:
		if len(i)>3:
			lst.append(i)
	return lst

print(duyet_chuoi())

res =[]
xau = int(input())
for i in range(xau):
	n = input()
	res.append(n)
print(''.join(res))	
#for i in res:  #neu su dung cach nay them  int ở dòng 16 :))
#	print(i,end="")

s = input()
def format(s):
	if len(s)>=3:
		if s[-3:] =="ing":
			s+="ly"
		else:
			s+="ing"
	return s
print(format(s))