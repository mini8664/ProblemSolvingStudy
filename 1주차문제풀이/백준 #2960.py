#문제: 에라토스테네스의 체

n,k = map(int, input().split()) #n,k값 각각 정수로 입력받기
count = 0 #횟수 설정
list = [False]*(n+1) #list안에 False로 n+1개 만큼 채우기

for i in range(2, n+1): #2부터 n까지의 수의 범위 안에서
     for j in range(i, n+1, i): #i의 배수 확인
          if list[j] == False: #j 리스트 값이 False일 때
            list[j] = True #True로 변경 후
            count +=1 #횟수 증가
            if count == k: #횟수가 k와 같아지면
                print(j) #j 출력
            
