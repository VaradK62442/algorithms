"""
Set of utility functions for computability.
"""
from typing import Callable
from finite_state_automata import FiniteStateAutomata as DFA


def cartesian_product(set1: set, set2: set):
    return {(x, y) for x in set1 for y in set2}


def DFA_combine(dfa1: DFA, dfa2: DFA, op: Callable[[set, set], set]):
    Q = cartesian_product(dfa1._states, dfa2._states)
    Q = set(map(str, Q))
    
    transitions = {}
    for state in Q:
        for char in dfa1._input_alphabet:
            qa, qb = state.strip("()").split(", ")
            qa = qa.strip("'"); qb = qb.strip("'")
            transitions[(state, char)] = f"{(dfa1._transitions[(qa, char)], dfa2._transitions[(qb, char)])}"

    q0 = f"{(dfa1._initial_state, dfa2._initial_state)}"
    F = op(cartesian_product(dfa1._accepting_states, dfa2._states), cartesian_product(dfa1._states, dfa2._accepting_states))
    F = set(map(str, F))

    return DFA(
        input_alphabet=dfa1._input_alphabet,
        states=Q,
        initial_state=q0,
        accepting_states=F,
        transitions=transitions
    )


def DFA_union(dfa1: DFA, dfa2: DFA):
    return DFA_combine(dfa1, dfa2, lambda x, y: x.union(y))


def DFA_intersection(dfa1: DFA, dfa2: DFA):
    return DFA_combine(dfa1, dfa2, lambda x, y: x.intersection(y))


def main():
    alphabet = {'a', 'b'}

    dfa1 = DFA(
        input_alphabet=alphabet,
        states={'q1', 'q2', 'q3', 'q4'},
        initial_state='q1',
        accepting_states={'q4'},
        transitions={
            ('q1', 'a'): 'q2',
            ('q1', 'b'): 'q1',
            ('q2', 'a'): 'q3',
            ('q2', 'b'): 'q2',
            ('q3', 'a'): 'q4',
            ('q3', 'b'): 'q3',
            ('q4', 'a'): 'q4',
            ('q4', 'b'): 'q4'
        }
    )

    dfa2 = DFA(
        input_alphabet=alphabet,
        states={'q1', 'q2', 'q3'},
        initial_state='q1',
        accepting_states={'q3'},
        transitions={
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q3',
            ('q3', 'a'): 'q3',
            ('q3', 'b'): 'q3',
        }
    )

    M_u = DFA_union(dfa1, dfa2)
    M_i = DFA_intersection(dfa1, dfa2)

    M_u.set_string("abb")
    M_i.set_string("aaabb")
    print(M_u.run())
    print(M_i.run())


if __name__ == '__main__':
    main()