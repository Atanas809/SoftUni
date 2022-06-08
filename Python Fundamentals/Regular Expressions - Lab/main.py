import re

def final_result(current_title, current_content):

    current_title = current_title.strip()
    current_content = current_content.strip()

    new_title = current_title.split(" ")
    new_content = current_content.split(" ")

    x = 0
