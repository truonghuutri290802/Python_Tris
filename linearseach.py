#linear search in python

def linearseach(array, n , x):

	#going through array sequencially
	for i in range(0,n):
		if(array[i] == x):
			return i 
	return -1

array = [2,4,0,1,9]
x = 2  
n = len(array)
rasual= linearseach(array,n,x)
if rasual == -1 :
	print("Khong so nao thoa man")
else:
	print("vi tri cua x :",rasual)