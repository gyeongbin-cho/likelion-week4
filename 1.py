# for 1 in range(1, 6):
#     #1,2,3,4,5 코드를 실행한다는 뜻 , 횟수를 알고싶을때
#      print("안녕하세요 ㅎㅎ...")
#      print("hi")
#      #코드를 전부 출력하고 다시 처음부터


# for 1 cookie in ["우유맛쿠키", "라떼맛쿠키"]
#     print(cookie, "말해라!")

#  #while문을 통한 반복, 조건

#  num =1
#  while num<1:
#      print(num, "번 손님 주문하신 음료나왔습니다")
#      num = num+1

num = 0
while num < 10:
    num= num+1
    if num % 2 == 0:
        continue
    print("홀수 :", num)