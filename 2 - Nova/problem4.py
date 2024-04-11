def reverse_string(string):

    for x in range((len(string) - 1), -1, -1):
        for z in string[x]:
            print(z, end = "")

reverse_string("Artificial Intelligence")



   