str = "Hello world"

char_dict = {}

for s in str:
    if s in char_dict.keys():
        char_dict.update({s: char_dict[s] + 1})
    else:
        char_dict.update({s:1})

for key, val in char_dict.items():
    print key, val