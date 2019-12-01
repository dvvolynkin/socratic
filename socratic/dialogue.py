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
from typing import Optional, Generator, Callable, Any
from inspect import getgeneratorstate, GEN_CLOSED

from socratic.utils import generator_start_wrapper


DialogueBranchState = Generator[Any, Any, None]
DialogueBranch = Callable[[Any], DialogueBranchState]


@dataclass
class Dialogue:
    entry_point: DialogueBranch
    _current_branch: Optional[DialogueBranchState] = None

    @property
    def current_branch_state(self) -> Optional[DialogueBranch]:
        if self._current_branch and self._is_current_branch_closed():
            return None

        return self._current_branch

    @current_branch_state.setter
    def current_branch_state(self, branch: DialogueBranch) -> None:
        self._current_branch = generator_start_wrapper(branch)
        next(self._current_branch)

    def reset_branch_state(self, question_message: Any) -> Optional[DialogueBranchState]:
        self.current_branch_state = self.entry_point(question_message)

        return self.current_branch_state

    def say(self, question_message: Any) -> Any:
        branch_state = self.current_branch_state

        if not branch_state:
            branch_state = self.reset_branch_state(question_message)

        try:
            answer = branch_state.send(question_message)
        except StopIteration:
            branch_state = self.reset_branch_state(question_message)
            answer = branch_state.send(question_message)

        return answer

    def _is_current_branch_closed(self) -> bool:
        return getgeneratorstate(self._current_branch) == GEN_CLOSED
