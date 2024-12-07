from math import log2


class PrettyConsole:
    separator1 = "-" * 55
    separator2 = "=" * 55

    def pretty_input():
        print()
        st = input()
        return st
    
    def common_message(*msgs):
        print()
        print(PrettyConsole.separator1)
        for msg in msgs:
            print(msg)
        print(PrettyConsole.separator1)

    def warning_message(error_msg):
        print()
        print(PrettyConsole.separator2)
        print("Ошибка:", error_msg)
        print("Входная строка некорректна. Пожалуйста, повторите ввод.")
        print(PrettyConsole.separator2)

    def listing_message(list):
        translation = {True: 'Истина', False: 'Ложь'}
        for p_class, accessory in list:
            print()
            print(u'\u2022', f'{p_class}:', translation[accessory])


def parse_input(st):
    c_0, c_1, c_space = st.count('0'), st.count('1'), st.count(' ')
    if c_0 + c_1 + c_space != len(st) or c_0 + c_1 == 0:
        return False, None, "Строка должна содержать только символы 0 и 1."
    
    lst = st.split()

    if not all([len(symb) <= 1 for symb in lst]):
        return False, None, "Таблица должна состоять только из 0 и 1."
    
    res = [int(symb) for symb in lst]

    if 2 ** int(log2(len(res))) != len(res):
        return False, None, "Таблица должна из 2^n элементов."
    
    return True, res, ""
        

def belongs_to_t0(truth_table):
    """Проверяет принадлежность функции к классу Т0."""
    return truth_table[0] == 0


def belongs_to_t1(truth_table):
    """Проверяет принадлежность функции к классу Т1."""
    return truth_table[-1] == 1


def is_self_dual(truth_table):
    """Проверяет самодвойственность функции."""
    n = len(truth_table)
    half_length = n // 2
    for i in range(half_length):
        if truth_table[i] != 1 - truth_table[n - 1 - i]:
            return False
    return True


def is_monotonic(truth_table):
    """Проверка монотонности."""
    # n = len(truth_table)
    # for i in range(n):
    #     for j in range(n):
    #         if bin(i & j).count('1') == bin(i).count('1') and truth_table[i] < truth_table[j]:
    #             return False
    #         if bin(i & j).count('1') == bin(j).count('1') and truth_table[j] < truth_table[i]:
    #             return False
    # return True
    pass


def is_linear_function(table):
    """Проверка линейности"""
    ans_columns = [table]

    for i in range(1, len(table)):
        cur_column = ans_columns[-1]
        next_column = [(cur_column[j] + cur_column[j + 1]) % 2 for j in range(len(table) - i)]
        ans_columns.append(next_column)

    for i in range(len(table)):
        c = bin(i)[2:].count("1")
        if c > 1 and ans_columns[i][0] == 1:
            return False
    return True


def main():
    while True:
        exit_code = False
        while True:
            PrettyConsole.common_message(*["Введите таблицу истинности в формате (x1 x2 x3 x4 ...)",
                                           "* Пустая строка - выход"])
            st = PrettyConsole.pretty_input()
            if st == "":
                exit_code = True
                break
            is_correct, parsed_input, error_message = parse_input(st)
            if is_correct:
                truth_table = parsed_input
                n = int(log2(len(truth_table)))
                break
            else:
                PrettyConsole.warning_message(error_message)

        if exit_code:
            break

        PrettyConsole.common_message("Принадлежность функции к классам Поста:")

        post_classes = [
            ("T0", belongs_to_t0(truth_table)),
            ("T1", belongs_to_t1(truth_table)),
            ("Самодвойственность", is_self_dual(truth_table)),
            ("Монотонность", is_monotonic(truth_table)),
            ("Линейность", is_linear_function(truth_table))
            ]

        PrettyConsole.listing_message(post_classes)

    PrettyConsole.common_message("Программа завершена.")


if __name__ == "__main__":
    main()