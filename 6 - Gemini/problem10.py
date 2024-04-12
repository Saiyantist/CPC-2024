def masking(S: str):
    masked_string = ""
    printed_x_count = 0
    for i in range(len(S)-1, -1, -1):
        if S[i].isnumeric():

            if printed_x_count <= 3:
                printed_x_count += 1
                masked_string += S[i]
            else:
                masked_string += "*"
        else:
            masked_string += S[i]
    return masked_string[::-1]
     
input_string = input("Input: ")
print(masking(input_string))

# Functionality: 5
# Performance: 4
# Quality: 4