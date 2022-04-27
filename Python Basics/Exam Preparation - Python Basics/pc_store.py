processor_in_dollars = float(input())
video_cards_in_dollars = float(input())
ram_in_dollars = float(input())
number_of_ram = int(input())
discount = float(input())

processor_in_leva = processor_in_dollars * 1.57
video_card_in_leva = video_card_in_dollars * 1.57
ram_in_leva = (ram_in_dollars * 1.57) * number_of_ram

processor_discount = processor_in_leva * discount
video_card_discount = video_card_in_leva * discount

total_leva = (processor_in_leva - processor_discount) + (video_card_in_leva - video_card_discount) + ram_in_leva

print(f"Money needed - {total_leva:.2f} leva.")

