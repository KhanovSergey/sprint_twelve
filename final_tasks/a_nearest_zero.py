# ID 68065811
import sys

def sort_zero(street_len, house_num):
    len_to_zero = []
    safe_street_len = street_len

    f_zero = [i for i, value in enumerate(house_num) if value == 0]

    if f_zero[0] == 0:
        len_to_zero.append(0)
    else:
        for i in reversed(range(f_zero[0] + 1)):
            len_to_zero.append(i)

    for j in range(0, len(f_zero) - 1):
        raz = int(f_zero[j + 1]) - int(f_zero[j])
        street_len = int(raz / 2 + 1)
        if (raz + 1) % 2 == 0:
            for i in range(1, street_len):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)
        else:
            for i in range(1, street_len - 1):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)

    right_zero = f_zero[len(f_zero) - 1]

    if right_zero < safe_street_len - 1:
        for i in range(1, safe_street_len - right_zero):
            len_to_zero.append(i)
    return len_to_zero


# def valid_street_len(street_len):
#     if type(street_len) != int:
#         raise ValueError('ввод не int')


def valid_street_len(street_len):
    try:
        int(street_len)
        print("ввод int")
        #return int(street_len)

    except ValueError:
        print("Надо ввести число от 1 до 1 000 000")
        sys.exit(1)



def main():
    street_len = input()
    print(street_len)
    print(type(street_len))
    street_len_int = valid_street_len(street_len)
    house_num = list(map(int, input().strip().split()))
    print(house_num)
    print(len(house_num))
    print(" ".join(map(str, sort_zero(street_len_int, house_num))))


if __name__ == '__main__':
    main()
# https://stackoverflow.com/questions/10166686/how-do-i-exit-program-in-try-except