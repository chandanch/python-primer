def fizz_buzz(number):
    result = ""
    if number % 3 == 0:
        result += "Fizz"
    if number % 5 == 0:
        result += "Buzz"
    if not result:
        result = number

    return result


print(fizz_buzz(3))
