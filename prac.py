def hap(a):
    sum = 0
    for i in range(0, len(a)) :
        sum = sum + int(a[i])
    return sum

a = input("정수를 입력하세요 :")
print(hap(a))

