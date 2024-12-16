from finite_state_automata import FiniteStateAutomata
from pushdown_automata import PushdownAutomata
from turing_machine import TuringMachine


def test_dfa():
    input_alphabet = {'a', 'b'}
    states = {'q0', 'q1', 'q2', 'q3'}
    initial_state = 'q0'
    accepting_states = {'q2'}
    transitions = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q3',
        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3'
    }

    # dfa to recognise `aa*bb*`
    dfa = FiniteStateAutomata(
        input_alphabet=input_alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transitions
    )

    string = "aabbb"

    dfa.set_string(string)
    result = dfa.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by DFA")


def test_pda():
    input_alphabet = {'a', 'b'}
    states = {'q0', 'q1', 'q2', 'q3'}
    initial_state = 'q0'
    accepting_states = {'q0', 'q3'}
    transitions = {
        ('q0', 'e', 'e'): ('q1', '$'),
        ('q1', 'a', 'e'): ('q1', '1'),
        ('q1', 'b', '1'): ('q2', 'e'),
        ('q2', 'b', '1'): ('q2', 'e'),
        ('q2', 'e', '$'): ('q3', 'e'),
    }

    # pda to recognise `a^nb^n`
    pda = PushdownAutomata(
        input_alphabet=input_alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transitions
    )

    string = "aaaabbbb"

    pda.set_string(string)
    result = pda.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by PDA")


def test_tm():
    alphabet = {'a', 'b', '#'}
    states = {'s0', 's1', 's2', 's3', 's4', 's5', 'sY', 'sN'}
    initial_state = 's0'
    transition_function = {
        ('s0', 'a'): ('s1', '#', 'R'),
        ('s0', 'b'): ('s2', '#', 'R'),
        ('s0', '#'): ('sY', '#', 'R'),

        ('s1', 'a'): ('s1', 'a', 'R'),
        ('s1', 'b'): ('s1', 'b', 'R'),
        ('s1', '#'): ('s3', '#', 'L'),

        ('s2', 'a'): ('s2', 'a', 'R'),
        ('s2', 'b'): ('s2', 'b', 'R'),
        ('s2', '#'): ('s4', '#', 'L'),

        ('s3', 'a'): ('s5', '#', 'L'),
        ('s3', 'b'): ('sN', 'b', 'L'),

        ('s4', 'a'): ('sN', 'a', 'L'),
        ('s4', 'b'): ('s5', '#', 'L'),

        ('s5', 'a'): ('s5', 'a', 'L'),
        ('s5', 'b'): ('s5', 'b', 'L'),
        ('s5', '#'): ('s0', '#', 'R'),
    }

    # tm to recognise palindromes on {a, b}
    tm = TuringMachine(
        alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        transition_function=transition_function
    )

    string = "abba"

    tm.set_string(string)
    result = tm.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by TM")


def tm_add_one():
    alphabet = {'0', '1', '#'}
    states = {'s0', 's1', 's2', 'sY', 'sN'}
    initial_state = 's0'
    transition_function = {
        ('s0', '0'): ('s0', '0', 'R'),
        ('s0', '1'): ('s0', '1', 'R'),
        ('s0', '#'): ('s1', '#', 'L'),
        
        ('s1', '0'): ('s2', '1', 'R'),
        ('s1', '1'): ('s1', '1', 'L'),
        ('s1', '#'): ('s2', '1', 'R'),

        ('s2', '0'): ('sN', '0', 'R'),
        ('s2', '1'): ('s2', '0', 'R'),
        ('s2', '#'): ('sY', '#', 'L'),
    }

    # tm to add one to a binary number
    tm = TuringMachine(
        alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        transition_function=transition_function
    )

    string = "11111"

    tm.set_string(string)
    tm.run()

    print(tm.show_tape())


def tutorial5q1a():
    alphabet = {'a', 'b'}
    states = {'q0', 'q1', 'q2', 'q3'}
    initial_state = 'q0'
    accepting_states = {'q3'}
    transition = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q0',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q1',
        ('q2', 'a'): 'q3',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q3',
        ('q3', 'b'): 'q3'
    }

    dfa = FiniteStateAutomata(
        input_alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transition
    )

    string = "abbbbabaa"

    dfa.set_string(string)
    result = dfa.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by DFA")


def tutorial5q1b():
    alphabet = {'a', 'b'}
    states = {'q0', 'q1', 'q2', 'q3'} 
    initial_state = 'q0'
    accepting_states = {'q0', 'q3'}
    transition = {
        ('q0', 'a'): 'q0',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q2',
        ('q1', 'b'): 'q3',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2',
        ('q3', 'a'): 'q0',
        ('q3', 'b'): 'q3'
    }

    dfa = FiniteStateAutomata(
        input_alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transition
    )

    string = "abbbabb"

    dfa.set_string(string)
    result = dfa.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by DFA")


def tutorial5q1c():
    alphabet = {'a', 'b'}
    states = {'q0', 'q1', 'q2'}
    initial_state = 'q0'
    accepting_states = {'q0', 'q1'}
    transition = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q1',
        ('q1', 'a'): 'q0',
        ('q1', 'b'): 'q2',
        ('q2', 'a'): 'q2',
        ('q2', 'b'): 'q2'
    }

    dfa = FiniteStateAutomata(
        input_alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transition
    )

    string = "aaaaba"

    dfa.set_string(string)
    result = dfa.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by DFA")


def tutorial5q1d():
    alphabet = {'a', 'b', 'c'}
    states = {'q0', 'q1', 'q2', 'q3', 'q4'}
    initial_state = 'q0'
    accepting_states = {'q3'}
    transition = {
        ('q0', 'a'): 'q1',
        ('q0', 'b'): 'q4',
        ('q0', 'c'): 'q4',

        ('q1', 'a'): 'q1',
        ('q1', 'b'): 'q2',
        ('q1', 'c'): 'q4',
        
        ('q2', 'a'): 'q4',
        ('q2', 'b'): 'q2',
        ('q2', 'c'): 'q3',
        
        ('q3', 'a'): 'q4',
        ('q3', 'b'): 'q4',
        ('q3', 'c'): 'q3',
        
        ('q4', 'a'): 'q4',
        ('q4', 'b'): 'q4',
        ('q4', 'c'): 'q4'
    }

    dfa = FiniteStateAutomata(
        input_alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        accepting_states=accepting_states,
        transitions=transition
    )

    string = "abbccc"

    dfa.set_string(string)
    result = dfa.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by DFA")


def tutorial5q2a():
    alphabet = {'0', '1', '#'}
    states = {'s0', 's1', 's2', 's3', 'sY', 'sN'}
    initial_state = 's0'
    transition_function = {
        ('s0', '0'): ('s0', '0', 'R'),
        ('s0', '1'): ('s0', '1', 'R'),
        ('s0', '#'): ('s1', '#', 'L'),
        
        ('s1', '0'): ('s2', '0', 'L'),
        ('s1', '1'): ('sY', '0', 'R'),

        ('s2', '0'): ('s2', '0', 'L'),
        ('s2', '1'): ('s3', '0', 'R'),
        ('s2', '#'): ('sN', '#', 'L'),

        ('s3', '0'): ('s3', '1', 'R'),
        ('s3', '#'): ('sY', '#', 'R'),
    }

    tm = TuringMachine(
        alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        transition_function=transition_function
    )

    string = "100100"

    tm.set_string(string)
    tm.run()

    print(tm.show_tape())


def tutorial5q2b():
    alphabet = {'0', '1', '#'}
    states = {'s0', 's1', 'sY', 'sN'}
    initial_state = 's0'
    transition_function = {
        ('s0', '0'): ('s0', '0', 'R'),
        ('s0', '1'): ('s1', '0', 'L'),
        ('s0', '#'): ('sY', '#', 'R'),

        ('s1', '0'): ('s0', '1', 'R'),
        ('s1', '#'): ('s0', '1', 'R'),
    }

    tm = TuringMachine(
        alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        transition_function=transition_function
    )

    string = "10100"

    tm.set_string(string)
    tm.run()

    print(tm.show_tape())


def tutorial5q3():
    # INCORRECT
    # this recognises a^n b^k c^n
    # not a^n b^n c^n

    alphabet = {'a', 'b', 'c', '#'}
    states = {'s0', 's1', 's2', 's3', 's4', 's5', 's6', 'sY', 'sN'}
    initial_state = 's0'
    transition_function = {
        ('s0', 'a'): ('s1', '#', 'R'),
        ('s0', '#'): ('sY', '#', 'R'),

        ('s1', 'a'): ('s1', 'a', 'R'),
        ('s1', 'b'): ('s2', 'a', 'L'),
        ('s1', 'c'): ('s3', 'c', 'R'),

        ('s2', 'a'): ('s2', 'a', 'L'),
        ('s2', '#'): ('s0', '#', 'R'),

        ('s3', 'c'): ('s3', 'c', 'R'),
        ('s3', '#'): ('s4', '#', 'L'),

        ('s4', 'c'): ('s5', '#', 'L'),

        ('s5', 'a'): ('s5', 'a', 'L'),
        ('s5', 'c'): ('s5', 'c', 'L'),
        ('s5', '#'): ('s6', '#', 'R'),

        ('s6', 'a'): ('s1', '#', 'R'),
        ('s6', '#'): ('sY', '#', 'R'),
    }

    tm = TuringMachine(
        alphabet=alphabet,
        states=states,
        initial_state=initial_state,
        transition_function=transition_function
    )

    string = "aabbbcc"

    tm.set_string(string)
    result = tm.run()

    print(f"String `{string}` is {'accepted' if result else 'rejected'} by TM")


def main():
    # test_dfa()
    # test_pda()
    # test_tm()
    # tm_add_one()

    # tutorial5q1a() # at least 3 a's
    # tutorial5q1b() # no singleton b's
    # tutorial5q1c() # every odd position is a
    # tutorial5q1d() # aa*bb*cc*

    # tutorial5q2a() # f(k) = k - 1
    # tutorial5q2b() # f(k) = 2k

    tutorial5q3() # should be a^nb^nc^n, but is a^nb^kc^n


if __name__ == "__main__":
    main()