

# Task 4:
def substitute_word(text, word, replace_word):
    text = text.replace(word, replace_word)

    return text


# Task 5:
def output(value):
    first_name = value["firstname"]
    last_name = value["lastname"]
    points = int(value["points"])

    return f"""Dear {first_name} {last_name},

You have received {points} points for the exercises of session 9.

Best wishes,
Ivan ivanov"""


def create_letter(students):

    result = []

    for key, value in students.items():
        result.append(output(value))

    return '\n'.join(result)

wilhelm_tell = """
A high, rocky shore of the lake of Lucerne opposite Schwytz.
The lake makes a bend into the land; a hut stands at a short
distance from the shore; the fisher boy is rowing about in his
boat. Beyond the lake are seen the green meadows, the hamlets,
and arms of Schwytz, lying in the clear sunshine. On the left
are observed the peaks of the Hacken, surrounded with clouds; to
the right, and in the remote distance, appear the Glaciers. The
Ranz des Vaches, and the tinkling of cattle-bells, continue for
some time after the rising of the curtain.
"""

students_info = {"126128": {"firstname": "Sara", "lastname": "Thomson", "points": 6},
                 "928710": {"firstname": "John", "lastname": "Doe", "points": 2},
                 "118979": {"firstname": "Emily", "lastname": "Jones", "points": 9},
                 "652182": {"firstname": "Martin", "lastname": "Mueller", "points": 12},
                 "526251": {"firstname": "Ella", "lastname": "Bauer", "points": 8}}

print(create_letter(students_info))

print(substitute_word(wilhelm_tell, "Glaciers", "Alps"))

print(count_alphabet("abcdefghijklmnopqrstuvwxyz"))


