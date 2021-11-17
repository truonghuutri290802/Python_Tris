n = int (input("Moi nhap so diem n:"))

def tinhsoTamGiac(n):
	return (n+2) * (n+1)/2
print(tinhsoTamGiac(n))
'''
với điểm n trên BC, sẽ tạo ra n+1 tam giac đơn, n tam giac kep ,
n-1 tam giác chập 3 ,... 2 tam giac chap n va 1 tam giac lon,
vậy nên số tam là tổng day số từ 1 đến n+
'''
x = int(input())
def sum_of_cubes_odd_number(x):
    s=0

    if x ==1:
       return (1)
    elif x== 0:
       return (0)
    elif x < 0 :
       return (-1)
    else :
        for i in range(1,2*x-1+1,2):
           s += i**3 
    a = s %(10**9+7)
    return a
print(sum_of_cubes_odd_number(x))
arr = str(input())
def soDienThoai(arr):
   return "({0}{1}{2}) {3}{4}{5}-{6}{7}{8}{9}".format(arr[0],arr[1],arr[2],arr[3],arr[4],arr[5],arr[6],arr[7],arr[8],arr[9])
def create_phone_number(arr):
    s = "("
    for i in range(len((arr))):
        if i == 3:
           s= s+") "+ str(arr[i])
        elif i == 6:
           s = s+"-"+ str(arr[i])
        else :
           s = s+str(arr[i])
    return s
print(soDienThoai(arr))
print(create_phone_number(arr))