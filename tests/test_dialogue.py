from socratic import Dialogue
import pytest


def test_simple_dialog():
    def entry_point(first_question):
        second_question = yield first_question

        yield second_question

    dialog = Dialogue(entry_point)

    answer_1 = dialog.say("test_message_1")
    assert answer_1 == "test_message_1"

    answer_2 = dialog.say("test_message_2")
    assert answer_2 == "test_message_2"


def test_cycled_dialog():

    def entry_point(first_question):
        if first_question == "Hello!":
            second_question = yield "Hello!"

        elif first_question == "How are you?":
            second_question = yield "Awesome!"
        else:
            second_question = yield "I don't understand you :c!"

        yield from entry_point(second_question)

    dialog = Dialogue(entry_point)

    answer_1 = dialog.say("Hello!")
    assert answer_1 == "Hello!"

    answer_2 = dialog.say("How are you?")
    assert answer_2 == "Awesome!"

    answer_3 = dialog.say("How are you?")
    assert answer_3 == "Awesome!"

    answer_4 = dialog.say("test_message")
    assert answer_4 == "I don't understand you :c!"


def test_stop_iteration():
    def entry_point(_):
        _ = yield "test1"

        _ = yield "test2"

    dialog = Dialogue(entry_point)
    answer1 = dialog.say("test")
    assert answer1 == 'test1'
    answer2 = dialog.say("test")
    assert answer2 == 'test2'
    answer3 = dialog.say("test")
    assert answer3 == 'test1'


def test_stop_iteration_on_exception():
    class TestException(Exception):
        ...

    def entry_point(_):
        _ = yield "test1"

        raise TestException()

    dialog = Dialogue(entry_point)
    answer1 = dialog.say("test")
    assert answer1 == 'test1'
    with pytest.raises(TestException):
        dialog.say("test")

    answer3 = dialog.say("test")
    assert answer3 == 'test1'

        
    



