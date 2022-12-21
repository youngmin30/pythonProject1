# 088
# 문자열의 좌우 공백 제거하기 lstrip, rstrip, strip

txt = ' 이 문자열에 있는 양쪽 공백 제거하기 ' # 문장의 앞 뒤에 공백을 포함했음
ret1 = txt.lstrip()
ret2 = txt.rstrip()
ret3 = txt.strip()
print('<'+txt+'>') # txt 그대로 출력(양쪽에 공백 있음)
print('<'+ret1+'>') # 왼쪽 공백 제거 lstrip
print('<'+ret2+'>') # 오른쪽 공백 제거 rstrip
print('<'+ret3+'>') # 양쪽 공백 제거 strip