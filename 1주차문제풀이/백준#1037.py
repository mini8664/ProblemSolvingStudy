#문제: 약수

a= int(input()) #a값 입력 받기
b= list(map(int, input().split())) #b값입력 받아서 리스트화

print(max(b)*min(b)) #b리스트에서 최댓값과 최솟값을 곱하면 n의 값을 구할 수 있음 