# 数组的冒泡排序（使用python语言实现的冒泡排序方法）
def sort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]

arr=[1,2,10,8,19,26,28,29]
sort(arr)
# 打印
print(arr)
# python字符串运算符
a = "hello"
b = "python"
print(a+b)
print(a*2)
print(a[1])
print("h" in a)
print("m" not in a)
var1='helloworld'
print(type(var1))
var2="pythonrun"
print(type(var2))
print(var2[0:3])
var3='wuyifan'+var2[0:3]
print(var3)
# python的运算符
# 算术运算符
