budget = float(input())
count_video_cards = int(input())
count_processors = int(input())
count_ram = int(input())
total_price = 0

price_video_cards = count_video_cards * 250
price_processors = count_processors * (price_video_cards * 0.35)
price_ram = count_ram * (price_video_cards * 0.1)

total_price += price_video_cards + price_processors + price_ram

if count_video_cards > count_processors:
    discount = 0.15
    total_price -= total_price * discount

difference = abs(total_price - budget)

if budget >= total_price:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
