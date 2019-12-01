# -*- coding: utf-8 -*-
#
# Socratic - very simple question-answer dialogue system based on python generators.
#
# Daniil Volynkin
# foxezzz@gmail.com
#
# License: MIT
#

from socratic import Dialogue

say = print


def yes_or_no(user_message):
    if user_message.lower() == "yes":
        return True
    elif user_message.lower() == "no":
        return False
    else:
        user_message_ = yield "Please type 'yes' or 'no'"
        yield from yes_or_no(user_message_)


def ask_about_apples():
    user_message = yield "Do you like apples?"
    user_like_apples = yield from yes_or_no(user_message)
    return user_like_apples


def ask_abot_oranges():
    user_message = yield "Do you like oranges?"
    user_like_oranges = yield from yes_or_no(user_message)
    return user_like_oranges


def simple_dialogue(*_):
    user_like_apples = yield from ask_about_apples()

    if user_like_apples:
        say("I don't like it too!")
    else:
        say("Sorry to hear that. I very like it :c")

    user_like_oranges = yield from ask_abot_oranges()

    if user_like_oranges:
        say("Sorry to hear that. I hate it :c")
    else:
        say("I like it too!")

    yield from simple_dialogue()


def main():
    dialog = Dialogue(simple_dialogue)
    print("Please type something: ")

    while True:
        question = input("-- ")
        answer = dialog.say(question)
        print("--", answer)


if __name__ == '__main__':
    main()
