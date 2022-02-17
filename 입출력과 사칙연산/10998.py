
#문제 번호:10998
#문제 제목: AxB
#두 정수 A와 B를 입력받은 다음, AxB를 출력하는 프로그램을 작성하시오.

#입력: 첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
#예제 입력: 1 2

#출력: 첫째 줄에 AxB를 출력한다.
#예제 출력: 2

#체크포인트: input을 사용하여 입력을 받고 두개의 입력을 곱한값을 출력한다.
# input()의 값을 분리하는 기본설정은 공백이다. 
# input().split(",")을 사용하여 공백을 "," 로 변경할 수 있다.

#코드
a,b = map(int, input().split())
print(a*b)

#띄어쓰기로 구분된 a,b 의 경우, 리스트로 저장된다. 이경우 스트링으로 저장이 되면 사칙연산이 불가능 하기 때문에
#map()을 사용하여 데이터의 타입을 지정해 주어야 한다. 이 문제의 경우 int로 지정.
