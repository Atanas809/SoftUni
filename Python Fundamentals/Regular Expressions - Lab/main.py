import re

def final_result(current_title, current_content):

    current_title = current_title.strip()
    current_content = current_content.strip()

    new_title = current_title.split(" ")
    new_content = current_content.split(" ")

    x = 0

    while x < len(new_title):
        if new_title[x] == "" or new_title[x] == " ":
            del new_title[x]
        else:
            x += 1

    y = 0

    while y < len(new_content):
        if new_content[y] == "" or new_content[y] == " ":
            del new_content[y]
        else:
            y += 1

    print(f"Title: {' '.join(new_title)}")
    print(f"Content: {' '.join(new_content)}")

def output(data):

    tags = r"(?P<tags>(<.+?>))"

    matches = re.finditer(tags, data)

    for match in matches:
        tag = match.group("tags")
        data = data.replace(tag, " ", 1)

    data = data.replace("\\n", "")
