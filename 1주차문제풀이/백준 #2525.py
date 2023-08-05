#문제: 오븐 시계 

h, m = map(int, input().split()) #시와 분 입력받기
time = int(input()) #요리하는데 필요한 시간 입력받기

h += time // 60 
m += time % 60

if m >= 60: #분이 60분 이상이거나 같으면
    h += 1 #시 하나 추가 후
    m -= 60 #분 초기화

if h >= 24: #시가 24시 이상이거나 같으면
    h -= 24 #시 초기화

print(h,m) 