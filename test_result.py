import os


def start_write(number_of_tests, operation):
    with open(os.getcwd() + r"\\result.txt", "a") as f:
        f.write("number_of_tests:" + number_of_tests + "\n")
        print("number_of_tests:" + number_of_tests)
        for line in operation:
            print(line)
            f.write(str(line) + "\n")
        text = "\n-----------------Start the test ------------------\n"
        f.write(text)
        f.close()
        print(text)


def write(result, i, current_system_time):
    with open(os.getcwd() + "\\result.txt", "a") as f:
        text = "The " + str(i + 1) + " time " + result + "----case start time : " + current_system_time + "\n"
        f.write(text)
        f.close()
        print(text)


def end_write(count):
    with open(os.getcwd() + "\\result.txt", "a") as f:
        text = "-----------------end the test pass " + str(count) + " times-----------------\n"
        f.write(text)
        f.close()
        print(text)


def error_write(text):
    with open(os.getcwd() + "\\result.txt", "a") as f:
        f.write(text)
        f.close()
        print(text)
