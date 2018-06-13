import random
import re

YES_KEYWORDS = ("yes","yeah","ya","y","yup","s","yea",)
YES_RESPONSE = ["Don't worry , I am with you" , "lets kill it" , "let's see"]
NO_KEYWORDS = ("no","na","n")
NO_RESPONSE  = [ "sorry honey , my options are limited at this time BYE "]

def check_for_yes_no(yes_no_response):
    sentence_list = wordList = re.sub("[^\w]", " ", yes_no_response).split()
    for word in sentence_list:
        if word.lower() in YES_KEYWORDS or word.lower().startswith("y"):
            return random.choice(YES_RESPONSE)
        elif word.lower() in NO_KEYWORDS:
            return random.choice(NO_RESPONSE)
            return 0


def lookup_error_code(ret_code):

    if check_digits(ret_code) != 7:
        print("Uhh  return codes are 7 digits in length")

    ctrlr_ret_code_hash = {1000000 : "Test Controller failed to load. OS not Server 2016 or later",
                           1000001 :
                           "Test Controller failed to load. Missing User Files. Verify User File have been setup",
                           1000002 :
                           "Test Controller failed to load. Unknown exception. Review TestSuite-Transcript.log",
                           1000010 : "Run-WcsSuite syntax errors. Review TestSuite-Transcript.log",
                           1000011 : "Run-WcsSuite did not find Test Suite file. Verify file name.",
                           1000012 : "Run-WcsSuite did not find Server List file. Verify file name.",
                           1000013 :
                           "Run-WcsSuite unexpected exception loading Test Suite file.To view exception dot-source in PowerShell window",
                           1000014 :
                           "Run-WcsSuite unexpected exception loading Server List file.To view exception dot-source in PowerShell window",
                           1000020 :
                           "Test Suite aborted. Test Suite failed to access servers and/or WCS manager.Verify targets are powered on and "
                           "connected to network Verify target hostname or IPV4 address ",
                           1000021 : "Failed to map drives on servers",
                           1000022 :
                           "Failed to update toolkit files on servers. Verify directory is not locked on server.Recommend rebooting server to release locks.",
                           1000023 :
                           "Failed to update toolkit user files on servers. Verify directory is not locked on server.Recommend rebooting server to release locks.",
                           1000024 : "Failed to run toolkit command on servers",
                           5000000 : "Unknown exception occurred.Review Test Suite transcript file for details."}

    target_ret_code_hash = {2000001: "Test Controller could not connect to test server",
                            2000002: "Test Controller could not connect to test server at end of test",
                            2000003: "Test controller lost network connection to test server",
                            2000004: "Test controller denied access to test server",
                            2000005: "Command on test server return non-integer value",
                            2000006: "Not used",
                            2000007: "Command on test server timed out before completing",
                            2000008: "Unexpected PSEXEC error communicating with test server",
                            2000009: "Test Controller could not copy files after test",
                            2000010: "Post test command parse function failed",
                            5000001: "Command on test server unexpectedly failed with exception",

    }

    if ret_code  in ctrlr_ret_code_hash.keys():
        return ctrlr_ret_code_hash[ret_code]
    elif ret_code  in target_ret_code_hash.keys():
        return target_ret_code_hash[ret_code]
    else:
        return "not avalibale"


def check_digits(error_code):
    return len(str(error_code))



def tshoot():
    print("Did my developer left you some puzzled integer > ", end="")
    yes_no_response = input()
    print(check_for_yes_no(yes_no_response))
    quit_response = False
    print("Can you give me the error code  > ", end="")
    error_code = int(input())
    while not quit_response:
        if check_digits(error_code) != 7:
            print("uhh uhh :) error code is 7 digits , Try again or press 'q' to come back later >", end=" ")
            error_code = input()
        if error_code == 'q' or error_code == "Q":
            print("catch you later")
            return 0
        final_reponse = lookup_error_code(int(error_code))
        if (final_reponse != "not available"):
            print(final_reponse)
            print("Do you wanna check other error code, enter code number  or press 'q' to come back later >", end=" ")
            error_code = input()
            if error_code == 'q' or error_code == "Q":
                print("catch you later")

        else:
            print("provide valid Error code")
            error_code = input()
