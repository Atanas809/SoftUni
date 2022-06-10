number = int(input())
searched_word = input()
all_data = list()
only_with_searched_word = list()

for _ in range(number):
    current_text = input()
    all_data.append(current_text)
    
    if searched_word in current_text:
        only_with_searched_word.append(current_text)

print(all_data)
print(only_with_searched_word)
