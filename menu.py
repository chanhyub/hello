import time
import random
foodlist = ["짬뽕", "짜장면", "탕수육", "김밥", "라면", "국밥"]
food = random.choice(foodlist)
print("골라줘 메뉴!!!!!!!!!!!!!!!!!!!!!!")
print("AI가 추천해주는 메뉴는?")
time.sleep(1)
for i in range(5, 0, -1):
    print(f"{i}..")
    time.sleep(1)
print("엄청난 분석을 통해 오늘의 메뉴를 추천 드립니다.")
print(f"{food} 입니다.")