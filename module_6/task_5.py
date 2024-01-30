
def get_paired_numbers(number_list: [int]) -> [int]:
    paired_numbers: [int] = []

    for number in number_list:
        if number % 2 == 0:
            paired_numbers.append(number)

    return paired_numbers


def main():
    list_of_numbers = [2, 3, 7, 34, 21, 78, 137, -2, -200, -3]

    print(f"Alkuperäinen lista: {list_of_numbers}")
    print(f"Lista karsittuna parittomista: {get_paired_numbers(list_of_numbers)}")


if __name__ == '__main__':
    main()
