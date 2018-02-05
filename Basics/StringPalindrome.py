def string_palindrome(str):
    len = str.__len__();
    for i in range((len - 1)/2):
        if str[i] != str[len - 1 - i]:
            print "NOT a palindrome"
            return False
    print "Palindrome"

if __name__ == "__main__":
    string_palindrome("madam")