import random

def dictionary(number):
    new_array = []
    for index in range(number):
        rnd = random.choice(wl)
        new_array.append(rnd)
    return print(new_array)



if "__name__" == "__main__":
    wl = open('/usr/share/dict/words', 'r')
    dictionary(number)

#
# all_lines = file.readlines()
#
# lines = []
# for line in all_lines:
#     lines.append(line.strip())
#
# all_lines = [line.strip() for line in all_lines]
