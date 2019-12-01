# -*- coding: utf-8 -*-
#
# Socratic - very simple question-answer dialogue system based on python generators.
#
# Daniil Volynkin
# foxezzz@gmail.com
#
# License: MIT
#

from dataclasses import dataclass
from typing import List, Optional

from socratic import Dialogue


@dataclass
class AnswerWithOptions:
    message: str
    options: Optional[List[str]] = None


def simple_dialogue(first_question):

    if first_question == "Hello!":
        second_question = yield AnswerWithOptions(
            message="Hello!",
        )
    elif first_question == "How are you?":
        second_question = yield AnswerWithOptions(
            "Awesome!",
        )
    else:
        second_question = yield AnswerWithOptions(
            "I don't understand you :c!",
            options=['Hello!', 'How are you?']
        )

    yield from simple_dialogue(second_question)


def main():
    dialog = Dialogue(simple_dialogue)
    print("Please type something: ")

    while True:
        user_replic = input('-- ')
        answer = dialog.say(user_replic)
        print("--", answer.message)
        if answer.options:
            print(answer.options)


if __name__ == '__main__':
    main()
