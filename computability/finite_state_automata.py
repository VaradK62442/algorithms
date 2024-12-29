"""
Class to implement a finite state automata.
"""

class FiniteStateAutomata:
    def __init__(self, 
                 input_alphabet: set,
                 states: set,
                 initial_state: str,
                 accepting_states: set,
                 transitions: dict[(str, str), str]):
        """
        Input alphabet: set of strings
        States: set of strings
        Initial state: string
        Accepting states: set of strings
        Transitions: dictionary of (state, input) -> state
        """
        assert initial_state in states, "Initial state not in states"
        assert all(state in states for state in accepting_states), "Accepting states not in states"

        self._input_alphabet = input_alphabet
        self._states = states
        self._initial_state = initial_state
        self._accepting_states = accepting_states
        self._transitions = transitions

        self._current_state = initial_state
        self._string = None

    
    def __str__(self):
        res = f"""
        Input alphabet: {self._input_alphabet}
        States: 
            {', '.join([s for s in self._states])}
        Initial state: {self._initial_state}
        Accepting states: {self._accepting_states}
        Transitions: 
        """
        res += "\n\t".join([f"""({state}, {char}) -> {self._transitions[(f'{state}', char)]}""" for state in self._states for char in self._input_alphabet])
        return res

    
    def set_string(self, string):
        if not all(char in self._input_alphabet for char in string):
            raise ValueError("String contains characters not in input alphabet")

        self._string = string
        self._current_state = self._initial_state

    
    def run(self):
        if self._string is None:
            raise ValueError("No string set")
        
        for char in self._string:
            if (self._current_state, char) not in self._transitions:
                return False

            self._current_state = self._transitions[(self._current_state, char)]

        return self._current_state in self._accepting_states