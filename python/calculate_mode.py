def calculate_mode(array):
    amount = {}
    for i in array:
        if i not in amount:
            amount[i] = 1
        else:
            amount[i] += 1
    result = [key for key, value in amount.items() if value == max(amount.values())]

    return result