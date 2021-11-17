A= int(input());

def max_product(A):
    Max_1 = A.pop(A.index(max(A))) #Lấy phần tử có giá trị lớn nhất,sau đó xóa phần tử đó khỏi list A
    Max_2 = A.pop(A.index(max(A))) #Lấy phần tử có giá trị lớn thứ hai,sau đó xóa phần tử đó khỏi list A
    Min_1 = A.pop(A.index(min(A))) #Lấy phần tử có giá trị nhỏ nhất,sau đó xóa phần tử đó khỏi list A
    Min_2 = A.pop(A.index(min(A))) #Lấy phần tử có giá trị nhỏ thứ hai,sau đó xóa phần tử đó khỏi list A
    if Max_1*Max_2>=Min_1*Min_2: #Lấy hai phần tử lớn nhất list A nhân với nhau,rồi so sánh với tích của hai phần tử nhỏ nhất
    #Bước này nhằm check xem tích của hai phần tử nhỏ nhất có phải là tích của hai số âm hay không,và nó có lớn hơn tích của hai số lớn nhất không
        return Max_1*Max_2
    else:
        return Min_1*Min_2 
print(max_product)

print(7**9%9)
