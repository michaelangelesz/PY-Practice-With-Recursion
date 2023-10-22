# Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

# A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.

def isPalindrome(word):
    
    # base case
    if len(word) < 2:
        return True 
    
    else: 
        if word[0] == word[-1]:
            return isPalindrome(word[1:-1])
        else: 
            return False


sample_word = 'aibohphobia' # aibohphobia is the fear of palindromes
print(isPalindrome(sample_word))