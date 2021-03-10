# 서울의 오늘 날짜를 출력하는 프로그램을 작성하시오.
import datetime
now = datetime.datetime.now()
print(now.strftime('%Y-%m-%d'))
