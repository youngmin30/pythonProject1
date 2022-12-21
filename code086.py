# 086

txt1 = '안녕하세요?'
txt2 = '1.Title-제목을 넣으세요'
txt3 = '3피오R2D2'
ret1 = txt1.isalnum()
ret2 = txt2.isalnum()
ret3 = txt3.isalnum()
print(ret1) # False가 출력됨 - 안녕하세요는 문자, 숫자가 아니므로 False 출력함
print(ret2) # False가 출력됨 - 숫자, 마침표, 영문 대소문자, 하이픈, 한글을 함께 쓰면 마침표와 하이픈으로 인해 False 출력함
print(ret3) # True를 출력함 - 숫자, 한글, 영문대문자는 모드 문자와 숫자로 True 출력함