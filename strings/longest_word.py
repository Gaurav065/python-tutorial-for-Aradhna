


sentence = input("enter a sentence: ")


word = ""

longest_word = ""

max_length = 0
curent_length = 0

for char in sentence+" ":
    if char != " ":
        word += char
        curent_length += 1
    else:
        if curent_length > max_length:
            max_length = curent_length
            longest_word = word
        word = ""
        curent_length = 0
        
        
        
print   (f"the longest word is: {longest_word}")
print(f"the length of the longest word is: {max_length}")


