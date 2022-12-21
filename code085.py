# 085

txt1 = '010-1234-5678'
txt2 = 'R2D2'
txt3 = '1212'
ret1 = txt1.isdigit()
ret2 = txt2.isdigit()
ret3 = txt3.isdigit()
print(ret1) # False 숫자로 보이는 전화번호는 숫자가 아닌 것으로 나옴
print(ret2) # False 숫자, 영문 대문자
print(ret3) # True 숫자