from finite_state_automata import FiniteStateAutomata

DEBUG = False
dprint = print if DEBUG else lambda *args, **kwargs: None


class PushdownAutomata(FiniteStateAutomata):
    def __init__(self, 
                 input_alphabet: set,
                 states: set,
                 initial_state: str,
                 accepting_states: set,
                 transitions: dict[str, ((str, str), (str, str))]):
        """
        Input alphabet: set of strings
        States: set of strings
        Initial state: string
        Accepting states: set of strings
        Transitions: dictionary of (state, input, stack_top) -> (state, stack_push)
        """
        super().__init__(input_alphabet, states, initial_state, accepting_states, transitions)

        self._stack = []
        self._string = None


    def _stack_peek(self):
        return self._stack[-1] if self._stack else 'e'
    

    def _stack_empty(self):
        return self._stack_peek() == 'e'
    

    def _stack_pop(self):
        return self._stack.pop()
    

    def _stack_push(self, char):
        self._stack.append(char) if char != 'e' else None


    def run(self):
        if self._string is None:
            raise ValueError("No string set")
        
        if self._string == "":
            return self._current_state in self._accepting_states
        
        if self._stack_empty() and (self._current_state, 'e', 'e') in self._transitions:
            next_state, stack_push = self._transitions[(self._current_state, 'e', self._stack_peek())]
            self._current_state = next_state
            self._stack_push(stack_push)
        
        i = 0
        while i < len(self._string):
            char = self._string[i]
            dprint(f"Current state: {self._current_state}, Input: {char}, Stack: {self._stack}")
            
            if (self._current_state, char, self._stack_peek()) not in self._transitions:
                if (self._current_state, char, 'e') not in self._transitions:
                    return False
                next_state, stack_push = self._transitions[(self._current_state, char, 'e')]
                pop = False
            else:
                next_state, stack_push = self._transitions[(self._current_state, char, self._stack_peek())]
                pop = True

            dprint(f"Next state: {next_state}, Stack push: {stack_push}")
            dprint(f"New stack: {self._stack if not pop else self._stack[:-1]}")
            dprint()

            self._current_state = next_state
            i += 1
            self._stack_pop() if pop else None
            self._stack_push(stack_push)

        if (self._current_state, 'e', self._stack_peek()) in self._transitions:
            next_state, stack_push = self._transitions[(self._current_state, 'e', self._stack_peek())]
            self._current_state = next_state
            self._stack_push(stack_push)

        return self._current_state in self._accepting_states

