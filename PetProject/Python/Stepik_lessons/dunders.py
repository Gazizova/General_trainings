import  random
#
# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector2D(self.x +
#                         other.x, self.y + other.y)
#
#
# first = Vector2D(5, 7)
# second = Vector2D(3, 9)
# result = first + second
# print(result.x)
# print(result.y)


# class VagueList:
#     def __init__(self, cont):
#         self.cont = cont
#
#     def __getitem__(self, index):
#         return self.cont[index + random.randint(-1, 1)]
    # def len(self):
        # print len[self.cont]
    # def __len__(self):
    #     return random.randint(0, len(self.cont)*2)

# vague_list = VagueList(["A", "B", "C", "D", "E"])
# print len
# # print len(vague_list)
# print vague_list[2]
# print vague_list[2]

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
 return a
a = print(fib(6))


def fibR(n):
 if n==1 or n==2:
  return 1
 return fibR(n-1)+fibR(n-2)
print(fibR(6))


arr = [3,2,1,4,6,5]
def arrSort():
    n = 1
    while(n < (len(arr)-1)):
        for i in range(len(arr)-n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr[i], arr[i+1])
                print(arr)
        n+=1
    return print(arr)

a = arrSort()

