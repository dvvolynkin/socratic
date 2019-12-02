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


def simple_dialogue(first_question):
    if first_question == "Hello!":
        second_question = yield "Hello!"

    elif first_question == "How are you?":
        second_question = yield "Awesome!"
    else:
        second_question = yield (
            "I don't understand you. I answer only for next questions: "
            "['Hello!', 'How are you?']"
        )

    yield from simple_dialogue(second_question)


def main():
    dialog = Dialogue(simple_dialogue)
    print("Please type something: ")

    while True:
        question = input("-- ")
        answer = dialog.say(question)
        print("--", answer)


if __name__ == '__main__':
    main()


