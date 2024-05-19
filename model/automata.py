class Transition:
    
    state: str
    symbol: str
    next_state: str

    def __init__(self, state: str, symbol: str, next_state: str):
        self.state = state
        self.symbol = symbol
        self.next_state = next_state

class Automata:
    
    states: list[str]
    alphabet: list[str]
    transitions: list[Transition]  # Fix: Change 'transitions' to 'Transition'
    initial_state: str
    final_states: list[str]

    def __init__(self, states: list[str], alphabet: list[str], transitions: list[Transition], initial_state: str, final_states: list[str]):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states



