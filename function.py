#문자 개수 세기
a = "hobby"
print(a.count('b'))

#위치 알려주기1(find)
# #문자나 문자열이 존재하지 않는다면 -1을 반환
a = "Pyhton is best choice"
print(a.find('b'))
print(a.find('k'))

#위치 알려주기2(index)
#문자나 문자열이 존재하지 않는다면 오류를 발생
a = "Life is too short"
print(a.index('t'))

#문자열 삽입(join)
a = ","
print(a.join('abcd'))

#소문자를 대문자로 바꾸기(upper)
a = "hi"
print(a.upper())

#대문자를 소문자로 바꾸기#(lower)
a = "HI"
print (a.lower())

#왼쪽 공백 지우기(Istrip)
a = "     hi"
print(a.lstrip())

#오른쪽 공백 지우기#(rstrip)
a ="hi     "
print(a.rstrip())

#양쪽 공백 지우기(strip)
a = "   hi   "
print(a.strip())

#문자열 바꾸기(replcae)
a = "Life is too short"
print(a.replace("Life", "Your leg"))

#문자열 나누기(split)
a = "Life is too short"
print(a.split())
a = "a:b:c:d"
print(a.split(':'))


