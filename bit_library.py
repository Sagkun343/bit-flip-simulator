import random


#
# # we going to simulate a singular bit flip.
#
#
def bit_flip(val: str) -> str:
    length = len(val)
    flipped_digit_index = random.randint(0, length - 1)
    flipped_digit = not (bool(int(val[flipped_digit_index])))
    return val[:flipped_digit_index] + str(int(flipped_digit)) + val[flipped_digit_index + 1:]


# print(bit_flip("10001"))
#
# # Now how about having a chance attribute applied to bit flips?
# # lets say we make sure every bit has a certain chance of being flipped.

def percentage_to_int(val: float) -> tuple[int, int]:
    decimal_flag = False
    count = 0
    for num in str(val):
        if decimal_flag:
            count += 1
        if num == ".":
            decimal_flag = True
    return int(val * pow(10, count)), pow(10, count)


def point_first(val: float) -> float:
    if int(val) == val:
        return val / 100
    val_string = str(val)
    count = 0
    for digit in val_string:
        if digit != ".":
            count += 1
        else:
            break
    return val / pow(10, count)


# print(percentage_to_int(31231.32423))


def bit_flip_by_chance(val: str, percentage_chance: float) -> str:
    if percentage_chance > 100:
        return "percentage too high."
    flip_chance = lambda x: True if random.random() < point_first(x) else False
    res = str()
    for digit in val:
        if flip_chance(percentage_chance):
            res += str(int(not (bool(int(digit)))))
        else:
            res += digit
    return res


print(bit_flip_by_chance("101010", 8.33333333))
