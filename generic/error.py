try:
    x = 10 / 0
except ZeroDivisionError:
    print("Division by zero is not allowed.")
finally:
    print("Finished!")
