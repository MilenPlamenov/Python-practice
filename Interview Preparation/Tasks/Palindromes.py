def is_palindrome(str_input):
    if str_input == str_input[::-1]:
        return True
    return False


input_string = input()

print('Palindrome' if is_palindrome(input_string) else 'Not a palindrome')
