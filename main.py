import json
import run_case

if __name__ == '__main__':
    with open('password.json', 'r') as f:
        a = json.load(f)
        com = a["com"]
        username = a["username"]
        password = a["password"]
        f.close()
    number_of_tests = input("Please enter the number of tests:\n")
    while True:
        if number_of_tests.isdigit():
            break
        number_of_tests = input("Invalid value, please re-enter:\n")

    with open('cases.json', 'r') as f:
        cases = json.load(f)
        f.close()
    for case in cases.keys():
        print(case)
    while True:
        key = input("please choose case:\n")
        if key in cases.keys():
            break
    run_case.run(com, username, password, number_of_tests, cases[key])
    # run_case.run(com, username, password, "10", cases["apn2"])
    # run_case.run(com, username, password, "10", cases["cfun"])
    # run_case.run(com, username, password, "10", cases["flymode"])
    # run_case.run(com, username, password, "10", cases["hardkey"])
    # run_case.run(com, username, password, "10", cases["softkey"])
    # run_case.run(com, username, password, "10", cases["reboot"])
