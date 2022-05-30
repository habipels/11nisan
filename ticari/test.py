"""
toplam = 0
for i in range(10):
    a = int (input("sayı : "))
    toplam = toplam+a
print(toplam/10)"""
"""
a = int (input("sayı1 : "))
b = int (input("sayı2 : "))
sepet = 0
for i in range(b):
    sepet += a
print(sepet)"""


"""
def ad(a,b):
    sepet = 1
    for i in range(b):
        sepet *= a
    return sepet
if True:
    a = 2
    b = 6
    res = ad(a,b)
    print(res)
"""
"""class calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x+self.y
    def multiply(self):
        return self.x*self.y
    def subract(self):
        return self.x-self.y
    def divide(self):
        self.x/self.y
"""
"""
def mod_alma(x,y):
    while ((x >=y) and y>0):
        x-=y
    return x
print(mod_alma(5,3))
"""
#1010
"""
2**0 *0=0
2**1 *1=2
2**2 *0 =0
2**3*1=8
2**4*0=0
10

"""
"""x=input("Değer Giriniz: ")
a=0
j=-1
for i in range(len(x)):
    a+=(2**i)*int(x[j])
    j-=1
print(a)"""

"""10/2   = 0
5/2    = 1
2/2    = 0
1      = 1"""
"""x=int(input("Değer Giriniz: "))
a=[]
while x>=1:
    if x%2==0:
        a.append("0")
    else:
        a.append("1")
    x=x//2
print(a)
"""



