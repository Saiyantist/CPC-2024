def count_letterCount(S: str):
    vowels = ['a','e','i','o','u']
    v_count = 0
    c_count = 0 
    for char in S:
        if char.lower() in vowels:
            v_count += 1
        elif char == ' ':
            pass
        else:
            c_count += 1
    
    return [v_count,c_count]
input_string = input("Input: ")
letter_count = count_letterCount (input_string)
print (letter_count)
# print(f"Vowels: {vowels}")
# print(f"Consonant: {consonant}")