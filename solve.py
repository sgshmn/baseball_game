# from main import al


# al2 = al


def li_have_n(n, li):
    """
    n = 들어갈 숫자를 문자열로 받은 것
    """

    result = []
    for i in li:
        if n in i:
            result.append(i)

    return result


# temp_list = list(range(al2))


def li_match_s_nums(number, s, li):  # 그 전까지의 구한 정답가능성이 있는 숫자 리스트

    result = []
    for n in li:
        match = 0
        for i in [0, 1, 2]:
            if number[i] == n[i]:
                match += 1
        if match == s:
            result.append(n)

    return result


def li_match_sb_nums(number, sb, li):  # sb = s + b
    have_i = []  # number의 0, 1, 2, 3 인덱스 값이 있는 숫자의 모임

    for i in range(3):
        have_i.append(li_have_n(number[i], li))
    # print(have_i)

    result = []
    for i in li:
        is_cnt = 0
        for j in range(3):
            if i in have_i[j]:
                is_cnt += 1
        if is_cnt == sb:
            result.append(i)

    return result





