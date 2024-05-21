import graphviz as digraph
import model.automata as automata
from pyformlang.finite_automaton import DeterministicFiniteAutomaton

def showAutomata(automata: automata.Automata, type: str):
    dot = digraph.Digraph()
    dot.attr(rankdir='LR')
    dot.attr(size='8,5')
    dot.node('start', shape='point')

    if type != 'Reverso':
        for state in automata.states:
            if state == automata.initial_state:
                dot.node(str(state), shape='circle')
                dot.edge('start', str(state))
            if state in automata.final_states:
                dot.node(str(state), shape='doublecircle')
            else:
                dot.node(str(state), shape='circle')
        for transition in automata.transitions:
            dot.edge(str(transition.state), str(transition.next_state), label=str(transition.symbol))
    else:
        dfa = automata 
        initial_state = list(dfa.start_states)[0] if dfa.start_states else None
        
        for state in dfa.states:
            if state == initial_state:
                dot.node(str(state), shape='circle')
                dot.edge('start', str(state))
            if state in dfa.final_states:
                dot.node(str(state), shape='doublecircle')
            else:
                dot.node(str(state), shape='circle')
        
        for state in dfa.states:
            if state in dfa._transition_function._transitions:
                for symbol, next_state in dfa._transition_function._transitions[state].items():
                    dot.edge(str(state), str(next_state), label=str(symbol))
    
    dot.render('Data/automata'+type, format='pdf', view=True)
    return dot

