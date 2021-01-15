#!/usr/bin/python

import pluggins

from machine.automata import Automaton

a = Automaton()

e1 = a.event_add('a', False, True)
e2 = a.event_add('b', True, True)
e3 = a.event_add('c', True, True)
s1 = a.state_add('q1', marked=True, initial=True)
s2 = a.state_add('q2', marked=True)

t1 = a.transition_add(s1, s2, e1)
t2 = a.transition_add(s2, s1, e2, probability=0.2)
a.transition_add(s1, s1, e2)
a.transition_add(s2, s2, e1)

t1.probability = 0.5

a.probabilitic_synchronization()

print(a)
print(t1.probabilistic_str())
print(t2.probabilistic_str())