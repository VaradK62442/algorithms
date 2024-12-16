DEBUG = False
dprint = print if DEBUG else lambda *args, **kwargs: None


class TuringMachine:

    def __init__(self, 
                 alphabet: set,
                 states: set,
                 initial_state: str,
                 transition_function: dict[(str, str), (str, str, str)],
                 tape_size: int = 10):
        """
        alphabet: set of strings
        states: set of strings
        initial_state: string
        transition_function: dictionary of (state, input) -> (state, output, direction)
        """
        assert 'sY' in states, "Accepting state not in states"
        assert 'sN' in states, "Rejecting state not in states"
        assert initial_state in states, "Initial state not in states"

        self._alphabet = alphabet
        self._states = states
        self._transition_function = transition_function

        self._current_state = initial_state
        self._string = None
        self._tape = None

        self._dir_map = {'L': -1, 'R': 1}

        self.TAPE_SIZE = tape_size


    def set_string(self, string):
        if not all(char in self._alphabet for char in string):
            raise ValueError("String contains characters not in alphabet")

        self._string = string
        self._tape = ['#' for _ in range(self.TAPE_SIZE // 2)] + list(string) + ['#' for _ in range(self.TAPE_SIZE // 2)]

    
    def run(self):
        if self._string is None:
            raise ValueError("No string set")
        
        i = self.TAPE_SIZE // 2 # start of string

        dprint(f"Initial state: {self._current_state}, Tape: {''.join(self._tape)}\n")

        while self._current_state not in {'sY', 'sN'}:
            char = self._tape[i]

            dprint(f"Current state: {self._current_state}, Input: {char}, Tape: {''.join(self._tape)}")

            if (self._current_state, char) not in self._transition_function:
                return False
            
            next_state, output, direction = self._transition_function[(self._current_state, char)]

            dprint(f"Next state: {next_state}, Output: {output}, Direction: {direction}")

            self._current_state = next_state
            self._tape[i] = output
            i += self._dir_map[direction]

        return self._current_state == 'sY'
    

    def show_tape(self):
        return ''.join([elt for elt in self._tape if elt != '#'])