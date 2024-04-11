def mask_my_credit_card_number(string):
    result = ''
    digit_count = 0
    num_checked = False
    for i in range(len(string)):
        if (digit_count < 12):
            for j in range(10):
                if (string[i] == str(j)):
                    result = f"{result}*"
                    digit_count += 1
                    num_checked = True
                    break
        if (num_checked):
            num_checked = False
            continue
        else:
            result = f"{result}{string[i]}"
    return result
print(mask_my_credit_card_number('The number 1234-5678-9123-4567 is my credit card number'))