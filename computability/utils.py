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


def DFA_complement(dfa: DFA):
    return DFA(
        input_alphabet=dfa._input_alphabet,
        states=dfa._states,
        initial_state=dfa._initial_state,
        accepting_states=dfa._states - dfa._accepting_states,
        transitions=dfa._transitions
    )


def main():
    alphabet = {'a', 'b'}

    dfa = DFA(
        input_alphabet=alphabet,
        states={'q0', 'q1', 'q2'},
        initial_state='q0',
        accepting_states={'q2'},
        transitions={
            ('q0', 'a'): 'q1',
            ('q0', 'b'): 'q0',
            ('q1', 'a'): 'q1',
            ('q1', 'b'): 'q2',
            ('q2', 'a'): 'q2',
            ('q2', 'b'): 'q2'
        }
    )

    dfa_complement = DFA_complement(dfa)

    dfa.set_string("aaaba")
    dfa_complement.set_string("aaaba")

    assert dfa.run() != dfa_complement.run()

if __name__ == '__main__':
    main()