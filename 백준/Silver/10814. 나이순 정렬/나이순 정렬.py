class MemberInfo:
    def __init__(self,age, name, num):
        self.age = age
        self.name = name
        self.num = num

n = int(input())
arr = []

for i in range(n):
    age,name = tuple(map(str, input().split()))
    age = int(age)
    arr.append(MemberInfo(age,name,i + 1))

arr.sort(key = lambda x: (x.age, x.num))

for i in range(len(arr)):
    print(arr[i].age, arr[i].name)


