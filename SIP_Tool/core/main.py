import random
import re
from core.help import Help
from core.tshoot import tshoot
from core.run_suite import run_suite
from core.binaries_setup import binaries_setup
from core.controller_setup import controller_files_setup
from core.toolkit_setup import toolkit_files_setup
from core.server_list_setup import create_server_list
from __future__ import print_function
#this is for end = " "


GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)
GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]


def check_for_greeting(sentence):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    sentence_list = wordList = re.sub("[^\w]", " ",  sentence).split()
    for word in sentence_list:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
        else:
            return GREETING_RESPONSES[2]

def setup_controller():
    print("Location of test kit and binaries <eg : C:\\Users\\Desktop>", end ="")
    #kit_location = "C:\\Users\\Administrator\\Desktop\\binaries"
    kit_location = input()
    binaries_setup(kit_location)
    toolkit_files_setup()
    controller_files_setup(kit_location)
    create_server_list()

def break_out():
    print("press q to close")
    close = input()
    if close == 'q' or close == 'Q':
        return 0

def print_options():
    print("1.Setup New Controller")
    print("2.Troubleshoot")
    print("3.Run suite")
    print("4.First Time User ?")


def main():
    print( "Hello, >" , end = "")
    sentence = str(input())
    print(check_for_greeting(sentence))
    print("How can I help you today  , below options are available currently ")
    print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    print_options()

    print("enter selction number ", end = "")
    choice_out = int(input())
    out = True
    while(out):

        if choice_out == 1:
            setup_controller()
            print("press q to close or select other option")
            print_options()
            choice = input()
            choice_out = int(choice)
            if choice == 'q' or choice == 'Q':
                out = False
        elif choice_out == 2:
            tshoot()
            print("press q to close or select other option")
            print_options()
            choice = input()
            choice_out = int(choice)
            if choice == 'q' or choice == 'Q':
                out = False
        elif choice_out == 3:
            run_suite()
            print("press q to close or select other option")
            print_options()
            choice = input()
            choice_out = int(choice)
            if choice == 'q' or choice == 'Q':
                out = False
        elif choice_out == 4:
            Help()
            print("press q to close or select other option")
            print_options()
            choice = input()
            choice_out = int(choice)
            if choice == 'q' or choice == 'Q':
                out = False
        else:
            print("snap !  available options are 1,2,3")

            out = False



if __name__ == "__main__":
    main()