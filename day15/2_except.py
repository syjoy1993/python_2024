#except

try: # try는 에러가 날 것 같은 구문을 적는 곳
    num = int(input("숫자 입력:"))
    result = 10 / num
    print(f"결과는 {result}")
except Exception:
    print("클래스 Exception데려옴 어떤 에러든 다 예외시킬수 있뜸")
# except ValueError:
#     print("제발 숫자 좀.. ")
except ZeroDivisionError:
    print("0으로 못나눠여,,,")
else: # 에러 없이 잘 썻을 경우
    print("에러가 없으니 한잔해~")
finally: # 에러가 나던 안나던 보여줘야됨
    print(" 상관없으니 보여주렴")