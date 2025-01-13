import time

while True:
    with open("user_feedback.txt", "r") as f:     # Reading and writing
        contents = f.read()

    if contents != "":
        time.sleep(5)
        with open("user_feedback.txt", "w"):
            pass
        with open("stored_feedback.txt", "a") as f:
            f.write(contents + "\n")
