try:
    raise MyError("Some information about what went wrong")
except MyError as error:
    print("Situation:", error)