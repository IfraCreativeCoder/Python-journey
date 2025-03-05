
def check_anagram(word1, word2):
    sorted_word1 = sorted(word1.lower())
    sorted_word2 = sorted(word2.lower())
    if sorted_word1 == sorted_word2:
        return True
    else:
        return False
    
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
    
if check_anagram(word1, word2):
    print("Yes,The words are anagrams.")
else: 
    print("No,The words are not anagrams.")   