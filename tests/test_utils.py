from socratic.utils import generator_start_wrapper


def test_generator_start_wrapper():
    def test_generator():
        yield 10

    wrapped_generator = generator_start_wrapper(
        test_generator()
    )

    assert next(wrapped_generator) is None
    assert next(wrapped_generator) == 10
