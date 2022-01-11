__author__ = 'liuketong'

import time
import datetime

import test_result
from com_driver import tbox_control_class


def run(com, username, password, number_of_tests, operations):
    # operations = []
    # while True:
    #     test_step_select = input("*****************Main Menu!********************\n"
    #                              " *  input 0  is: start test                        *\n"
    #                              " *  input 1  is: Set adapter_test_command          *\n"
    #                              " *  input 2  is: check network ok                  *\n"
    #                              " *  input 3  is: check network fail                *\n"
    #                              " *  input 4  is: Set wait time                     *\n"
    #                              " *  input 5  is: send command                      *\n"
    #                              " *  input 6  is: reboot                            *\n")
    #     if test_step_select == "0":
    #         print("number_of_tests:" + number_of_tests)
    #         for line in operations:
    #             print(line)
    #         input("Please check test step and enter any key to start test:\n")
    #         break
    #     elif test_step_select == "1":
    #         parameter = input("Please enter the adapter test command:\n")
    #         if parameter.replace(",", "").isdigit():
    #             operations.append({"Action": "adapter_test_command", "Parameter": parameter})
    #         else:
    #             print("Invalid value, please re-enter")
    #     elif test_step_select == "2":
    #         parameter = input("Please enter the ping command:\n")
    #         operations.append({"Action": "check_network_pass", "Parameter": parameter})
    #     elif test_step_select == "3":
    #         parameter = input("Please enter the ping command:\n")
    #         operations.append({"Action": "check_network_fail", "Parameter": parameter})
    #     elif test_step_select == "4":
    #         parameter = input("Please enter the wait time:\n")
    #         if parameter.isdigit():
    #             operations.append({"Action": "wait", "Parameter": parameter})
    #         else:
    #             print("Invalid value, please re-enter")
    #     elif test_step_select == "5":
    #         parameter = input("Please enter the command:\n")
    #         operations.append({"Action": "send_command", "Parameter": parameter})
    #     elif test_step_select == "6":
    #         print("set reboot ok")
    #         operations.append({"Action": "reboot", "Parameter": ""})
    #     else:
    #         print("Invalid value, please re-enter")

    count = 0
    test_result.start_write(number_of_tests, operations)

    tbox_control = tbox_control_class(port=com,
                                      username=username,
                                      password=password)

    for i in range(int(number_of_tests)):
        result = "pass"
        current_system_time = str(datetime.datetime.now()).replace(" ", "-").replace(":", "-")[0:19]
        print(current_system_time)
        tbox_control.time = current_system_time

        tbox_control.login()
        tbox_control.get_time()
        for operating in operations:
            if operating["Action"] == "adapter_test_command":
                tbox_control.adaptertest_option(operating["Parameter"])
            elif operating["Action"] == "check_network_pass":
                check = tbox_control.check_network_pass(operating["Parameter"])
                if not check:
                    result = "fail"
            elif operating["Action"] == "check_network_fail":
                check = tbox_control.check_network_fail(operating["Parameter"])
                if not check:
                    result = "fail"
            elif operating["Action"] == "wait":
                time.sleep(int(operating["Parameter"]))
            elif operating["Action"] == "send_command":
                tbox_control.send_command(operating["Parameter"])
            elif operating["Action"] == "reboot":
                tbox_control.send_command("reboot")
                print("start reboot,please wait about 220 second")
                time.sleep(int(operating["Parameter"]))
                tbox_control.login()
            else:
                print("start")
        if result == "pass":
            count += 1
        test_result.write(result, i, current_system_time)
        tbox_control.get_time()
        time.sleep(5)
    tbox_control.s_close()
    test_result.end_write(count)
    input("Please enter any key to exit and check the result in 'result.txt':\n")
