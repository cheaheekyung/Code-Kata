a, b = map(int, input().split())  # 현재 시(a)와 분(b) 입력
c = int(input())  # 추가할 분(c) 입력

# 총 분 계산
total_minutes = b + c

# 시와 분으로 변환
new_hours = (total_minutes // 60) + a  # 추가된 시 계산
new_minutes = total_minutes % 60  # 분 계산

# 시간 범위 조정
if new_hours >= 24:
    new_hours %= 24  # 24시가 넘으면 0시부터 시작

# 결과 출력
print(new_hours, new_minutes)