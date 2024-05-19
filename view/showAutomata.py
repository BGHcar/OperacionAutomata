import graphviz as digraph
import model.automata as automata

def showAutomata(automata: automata.Automata, type: str):
    dot = digraph.Digraph()
    dot.attr(rankdir='LR')
    dot.attr(size='8,5')
    dot.node('start', shape='point')
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
    dot.render('Data/automata'+type, format='pdf', view=True)
    return dot


