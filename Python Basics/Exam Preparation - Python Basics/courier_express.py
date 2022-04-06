# weight_in_kilos = float(input())
# type_of_service = input()
# distance_in_kilometres = int(input())
# if type_of_service == "standard":
#     if weight_in_kilos < 1:
#         price = 0.03 * distance_in_kilometres
#     elif weight_in_kilos < 10:
#         price = 0.05 * distance_in_kilometres
#     elif weight_in_kilos < 40:
#         price = 0.10 * distance_in_kilometres
#     elif weight_in_kilos < 90:
#         price = 0.15 * distance_in_kilometres
#     elif weight_in_kilos < 150:
#         price = 0.20 * distance_in_kilometres
# if type_of_service == "express":
#     if weight_in_kilos < 1:
#         price = (((0.8 * 0.03) * weight_in_kilos) * distance_in_kilometres) + distance_in_kilometres * 0.03
#     elif weight_in_kilos < 10:
#         price = (((0.4 * 0.05) * weight_in_kilos) * distance_in_kilometres) + distance_in_kilometres * 0.05
#     elif weight_in_kilos < 40:
#         price = (((0.05 * 0.10) * weight_in_kilos) * distance_in_kilometres) + distance_in_kilometres * 0.10
#     elif weight_in_kilos < 90:
#         price = (((0.02 * 0.15) * weight_in_kilos) * distance_in_kilometres) + distance_in_kilometres * 0.15
#     elif weight_in_kilos < 150:
#         price = (((0.01 * 0.20) * weight_in_kilos) * distance_in_kilometres) + distance_in_kilometres * 0.20
# print(f"The delivery of your shipment with weight of {weight_in_kilos:.3f} kg. would cost {price:.2f} lv.")