def arrangeCoins(n):
    row_length = 1
    num_rows = 0
    coins = n
    while coins >= 0:
        if coins - row_length == 0:
            num_rows += 1
            return num_rows
        elif coins - row_length > 0:
            num_rows += 1
            coins -= row_length
            row_length += 1
        elif coins - row_length < 0:
            return num_rows

print(arrangeCoins(8))