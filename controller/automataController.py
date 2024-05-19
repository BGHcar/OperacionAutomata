import model.automata as automata


def automataUnion(automata1: automata.Automata, automata2: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

    # Copiar el alfabeto de ambos autómatas
    newAutomata.alphabet = list(
        set(automata1.alphabet) & set(automata2.alphabet))

    # Asignar el estado inicial
    newAutomata.initial_state = automata1.initial_state + automata2.initial_state

    # Generar los estados de newAutomata
    for state1 in automata1.states:
        for state2 in automata2.states:
            newAutomata.states.append(state1 + state2)

    # Crear las transiciones de newAutomata
    for state1 in automata1.states:
        for state2 in automata2.states:
            for symbol in newAutomata.alphabet:
                next_state1 = ''
                for transition in automata1.transitions:
                    if transition.state == state1 and transition.symbol == symbol:
                        next_state1 = transition.next_state
                        break
                next_state2 = ''
                for transition in automata2.transitions:
                    if transition.state == state2 and transition.symbol == symbol:
                        next_state2 = transition.next_state
                        break
                next_state = next_state1 + next_state2
                new_state = state1 + state2
                newAutomata.transitions.append(
                    automata.Transition(new_state, symbol, next_state))

    # Asignar los estados finales de newAutomata
    for state1 in automata1.states:
        for state2 in automata2.states:
            if state1 in automata1.final_states or state2 in automata2.final_states:
                newAutomata.final_states.append(state1 + state2)

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataIntersection(automata1: automata.Automata, automata2: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

    # Copiar el alfabeto de ambos autómatas
    newAutomata.alphabet = list(
        set(automata1.alphabet) & set(automata2.alphabet))

    # Asignar el estado inicial
    newAutomata.initial_state = automata1.initial_state + automata2.initial_state

    # Generar los estados de newAutomata
    for state1 in automata1.states:
        for state2 in automata2.states:
            newAutomata.states.append(state1 + state2)

    # Crear las transiciones de newAutomata
    for state1 in automata1.states:
        for state2 in automata2.states:
            for symbol in newAutomata.alphabet:
                next_state1 = ''
                for transition in automata1.transitions:
                    if transition.state == state1 and transition.symbol == symbol:
                        next_state1 = transition.next_state
                        break
                next_state2 = ''
                for transition in automata2.transitions:
                    if transition.state == state2 and transition.symbol == symbol:
                        next_state2 = transition.next_state
                        break
                next_state = next_state1 + next_state2
                new_state = state1 + state2
                newAutomata.transitions.append(
                    automata.Transition(new_state, symbol, next_state))

    # Asignar los estados finales de newAutomata
    for state1 in automata1.final_states:
        for state2 in automata2.final_states:
            if state1 in automata1.final_states and state2 in automata2.final_states:
                newAutomata.final_states.append(state1 + state2)

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataComplement(automaton: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

    # Construir los estados y transiciones
    for state in automaton.states:
        newAutomata.states.append(state)
        if state == automaton.initial_state:
            # Si el estado original es inicial, será final
            newAutomata.initial_state = state
        if state in automaton.final_states:
            # Si el estado original es final, será final
            newAutomata.states.append(state)
        else:
            # Si no es ni inicial ni final, será final
            newAutomata.final_states.append(state)

    # Construir las transiciones
    for transition in automaton.transitions:
        newAutomata.transitions.append(automata.Transition(
            transition.state, transition.symbol, transition.next_state))

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def automataReverse(automaton: automata.Automata):
    newAutomata = automata.Automata([], [], [], '', [])

    # Construir los estados
    for state in automaton.states:
        newAutomata.states.append(state)
        if state == automaton.initial_state:
            # Si el estado original es inicial, será final
            newAutomata.final_states.append(state)
        elif state in automaton.final_states:
            newAutomata.initial_state = state  # Si el estado original es final, será inicial

    # Construir las transiciones invertidas
    for transition in automaton.transitions:
        newAutomata.transitions.append(automata.Transition(
            transition.next_state, transition.symbol, transition.state))
    
    DNFAtoDFA(newAutomata)

    newAutomata = validateTransitions(newAutomata)

    return newAutomata


def validateTransitions(automaton: automata.Automata):

    transitionstoDelete = []

    contador = 0
    for state in automaton.states:
        for transition in automaton.transitions:
            if state in transition.next_state:
                contador += 1

        if contador == 0 and state not in automaton.initial_state:
            print(f"El estado {state} no tiene transiciones")
            transitionstoDelete.append(state)
            automaton.states.remove(state)

        contador = 0

    print("Estos son los estados a eliminar", transitionstoDelete)

    # Eliminar transiciones asociadas a los estados a eliminar
    automaton.transitions = [transition for transition in automaton.transitions
                             if transition.state not in transitionstoDelete
                             and transition.next_state not in transitionstoDelete]
    
    print("Estas son las nuevas transiciones")
    for transition in automaton.transitions:
        print(f"Estado: {transition.state}, Simbolo: {transition.symbol}, Estado Siguiente: {transition.next_state}")

    return automaton

def isDFA(automaton: automata.Automata):
    seen_transitions = set()

    for transition in automaton.transitions:
        transition_tuple = (transition.state, transition.symbol)
        if transition_tuple in seen_transitions:
            return False
        seen_transitions.add(transition_tuple)

    return True


def DNFAtoDFA(automaton: automata.Automata):
    if isDFA(automaton):
        print("El autómata ya es DFA")
        return automaton

    alfabeto = automaton.alphabet
    initial_state = automaton.initial_state
    transitions = automaton.transitions
    

    #Evaluamos nuestro estado initial y vemos a donde nos lleva con cada simbolo del alfabeto

    # Creo una variable que almacene el estado inicial y la transicion que se hace con cada simbolo del alfabeto
    state_transitions = automata.Transition("", "", "")
    for symbol in alfabeto:
        for transition in automaton.transitions:
            if transition.state == initial_state and transition.symbol == symbol:
                state_transitions.state = initial_state
                state_transitions.symbol = symbol
                state_transitions.next_state = transition.next_state
                transitions.append(state_transitions)
    
        
        
    print("Estas son las nuevas transiciones")
    for transition in transitions:
        print(f"Estado: {transition.state}, Simbolo: {transition.symbol}, Estado Siguiente: {transition.next_state}")


    # Creo una lista que almacene los estados que se generan con cada simbolo del alfabeto




