def repeated_string(s, n):
    total_repeated = 0

    # print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))

    # print(s[:n % len(s)].count("a"))
    print(s[:n % len(s)])
    print(s[1])

    # WHERE I STOPPED:
    #
    # DEFINITIONS:
    #
    # * snippet is s
    # * real string is the snippet "s", repeated for as long as n. May be whole (e.g [abc, 6] => abcabc ) or partial
    #   (e.g [aba, 10] => abaabaabaa ) with leftover characters
    #
    # CONCEPT:
    # * Figure out how many times snippet happens in real string
    # * Count how many 'a's in both (snippet * numberOfTimesItHappens) and leftover characters at the end
    # * Sum and return both counts aforementioned
    #

    # 1 - count number of "a"s in snippet string
    # 2 - divide string length (and floor it) by n (the length of real string)
    #     -> the result is the left over characters of the snippet at the end of the real string, if they exist
    # 3 - count number of "a"s in leftover characters of snippet at the end of real string, if they exist
    # 4 - multiply the count for leftover characters along with the division of n per length of s. (as in
    #       how many times does the snippet happens?
    # 5 - sum them and return

    as_in_string = s.count('a')
    partial_string = s[:n % len(s)]
    # print(as_in_string)
    # print(partial_string)
    return total_repeated


repeated_string('aba', 10)
