# 089
# 문자열을 수치형 자료로 변환 int, float

numstr = input('숫자를 입력하세요')
try:
    num = int(numstr)
    print('당신이 입력한 숫자는 정수 <%d>입니다.'%num)
except:
    try:
        num = float(numstr)
        print('당신이 입력한 숫자는 실수<%f>입니다.'%num)
    except:
        print('+++숫자를 입력하세요~+++')