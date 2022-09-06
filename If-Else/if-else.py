def WeirdOrNot(n):
    if (float(n) / 2).is_integer(): # Checks if n is even.
        if (n >= 2) and (n <=5):
            return "Not Weird"
        elif (n >= 6) and (n <= 20):
            return "Weird"
        else:
            return "Not Weird"
    else:
        return "Weird" # Odd

print(WeirdOrNot())