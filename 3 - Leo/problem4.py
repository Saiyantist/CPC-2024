def reverse_string(string):
    a = string
    strlen = len(a)
    for i in range(1,strlen+1):
        word= (a[-i])
        
        print(word, end="")
        
inp = input("enter a word: ")

reverse_string(inp)