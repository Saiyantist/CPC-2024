S = input("Input").upper()
rm_map = {
    'I':1,
    'X':10,
    'L': 50,
    'C': 100,
    'M': 1000
} 
N = 0
for i in range (0,len(S)):
    if i == len(S)-1:
        N += rm_map[S[i]]
    elif rm_map[S[i]] < rm_map[S[i+1]]:
        N -= rm_map[S[i]]
    else:
        N += rm_map[S[i]]

print(N)
# print(rm_map)


# Functionality: 5
# Performance: 5
# Quality: 3