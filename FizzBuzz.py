def fizzBuzz((int)nombre):
    if nombre % 3 == 0 and nombre % 5 == 0:
        return "FizzBuzz"
    elif nombre % 3 == 0:
        return "Fizz"
    elif nombre % 5 == 0:
        return "Buzz"
    else:
        return str(nombre)
