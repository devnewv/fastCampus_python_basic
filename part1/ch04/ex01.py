#데이터 타입
import math

str1 = 'Niceman'
bool1 = True
float1 = 10.33
int1 = 4
dict1 = {
    'name': 'kim',
    'age': 15
}
tuple1 = 3, 5, 7
set1 = {7, 8, 9}
list1 = [3, 5, 7]

print(type(str1))
print(type(bool1))
print(type(float1))
print(type(int1))
print(type(dict1))
print(type(tuple1))
print(type(set1))
print(type(list1))
print("=========================================================")

a = 5.
b = 4

print(type(a), type(b))
result1 = a + b
print(result1, type(result1))
print(int(result1), type(int(result1)))
print("=========================================================")

print(math.ceil(5.22))
print(math.floor(3.99))