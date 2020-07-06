# 1) DOES NOT ACCOUNT FOR LOWER/UPPER CASE
# JUST CONVERT THEM DURING THE FALSE CHECK BETWEEN FIRST AND LAST LETTER IF THAT IS THE DESIRED BEHAVIOR:

# if s[0].lower() != s[1].lower():
#     return False

# 2) Ignoring symbols here does not seem efficient nor maintainable. Need to revisit
# Possible solutions:
#     regex
#     translate table
#     lookup for letter only (expensive to process everytime)

def palindrome_checker_with_recursion(s):
    def remove_whitespace(string):
        return string.replace(" ", "")

    def ignore_symbols():
        return s.replace("'", "").replace("\"", "")

    if len(s) <= 1:
        return True

    s = remove_whitespace(s)
    s = ignore_symbols()

    if s[0] != s[-1]:
        return False



    return palindrome_checker_with_recursion(s[1:-1])

# print(palindrome_checker_with_recursion('racecar'))
# print(palindrome_checker_with_recursion('Lesley'))
# print(palindrome_checker_with_recursion('kayak'))
print(palindrome_checker_with_recursion("madam i'm adam"))


