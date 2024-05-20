import model.automata as automata
import view.showAutomata as showAutomata
import controller.automataController as automataController

def main():
    while True:
        isValidInput = True
        while isValidInput:
            states = input("Ingrese los estados del automata 1 separados por coma: ").split(",")
            if len(states) > 4:
                print("El automata solo puede tener 4 estados")
            else:
                isValidInput = False
        isValidInput = True
        alphabet = input("Ingrese el alfabeto del automata 1 separados por coma: ").split(",")
        transitions = []
        for state in states:
            for symbol in alphabet:
                isValidInput = True
                while isValidInput:
                    next_state = input(f"Ingrese el estado siguiente del estado {state} con el simbolo {symbol}: ")
                    if next_state not in states:
                        print("El estado no pertenece al automata")
                    else:
                        isValidInput = False
                        transitions.append(automata.Transition(state, symbol, next_state))

        isValidInput = True

        while isValidInput:
            initial_state = input("Ingrese el estado inicial del automata 1: ")
            if initial_state not in states:
                print("El estado no pertenece al automata")
            else:
                isValidInput = False
        isValidInput = True

        while isValidInput:
            final_states = input("Ingrese los estados finales del automata 1 separados por coma: ").split(",")
            for state in final_states:
                if state not in states:
                    print("El estado no pertenece al automata")
                    break
            else:
                isValidInput = False
        
        isValidInput = True

        automata1 = automata.Automata(states, alphabet, transitions, initial_state, final_states)

        while isValidInput:
            states = input("Ingrese los estados del automata 2 separados por coma: ").split(",")
            if len(states) > 4:
                print("El automata solo puede tener 4 estados")
            else:
                isValidInput = False

        
        alphabet = input("Ingrese el alfabeto del automata 2 separados por coma: ").split(",")
        transitions = []
        for state in states:
            for symbol in alphabet:
                isValidInput = True
                while isValidInput:
                    next_state = input(f"Ingrese el estado siguiente del estado {state} con el simbolo {symbol}: ")
                    if next_state not in states:
                        print("El estado no pertenece al automata")
                    else:
                        isValidInput = False
                        transitions.append(automata.Transition(state, symbol, next_state))

        isValidInput = True
        while isValidInput:
            initial_state = input("Ingrese el estado inicial del automata 2: ")
            if initial_state not in states:
                print("El estado no pertenece al automata")
            else:
                isValidInput = False
        isValidInput = True

        while isValidInput:
            final_states = input("Ingrese los estados finales del automata 2 separados por coma: ").split(",")
            for state in final_states:
                if state not in states:
                    print("El estado no pertenece al automata")
                    break
                else:
                    isValidInput = False

        automata2 = automata.Automata(states, alphabet, transitions, initial_state, final_states)

        print ("Desea ingresar un tercer automata? (s : si, cualquier otra letra : no)")

        option = input("Ingrese una opcion: ")

        automata3 = None
        if option.lower() == "s":
            isValidInput = True
            while isValidInput:
                states = input("Ingrese los estados del automata 3 separados por coma: ").split(",")
                if len(states) > 4:
                    print("El automata solo puede tener 4 estados")
                else:
                    isValidInput = False

            alphabet = input("Ingrese el alfabeto del automata 3 separados por coma: ").split(",")
            transitions = []
            for state in states:
                for symbol in alphabet:
                    isValidInput = True
                    while isValidInput:
                        next_state = input(f"Ingrese el estado siguiente del estado {state} con el simbolo {symbol}: ")
                        if next_state not in states:
                            print("El estado no pertenece al automata")
                        else:
                            isValidInput = False
                            transitions.append(automata.Transition(state, symbol, next_state))

            isValidInput = True
            while isValidInput:
                initial_state = input("Ingrese el estado inicial del automata 3: ")
                if initial_state not in states:
                    print("El estado no pertenece al automata")
                else:
                    isValidInput = False
            isValidInput = True

            while isValidInput:
                final_states = input("Ingrese los estados finales del automata 3 separados por coma: ").split(",")
                for state in final_states:
                    if state not in states:
                        print("El estado no pertenece al automata")
                        break
                    else:
                        isValidInput = False

            automata3 = automata.Automata(states, alphabet, transitions, initial_state, final_states)

        print("Que automata desea usar para el complemento? (1 : Union, 2 : Interseccion)")

        option = input("Ingrese una opcion: ")

        if automata3 == None:
            automataUnion = automataController.automataUnion(automata1, automata2)
            showAutomata.showAutomata(automataUnion, "Union")
            automataIntersection = automataController.automataIntersection(automata1, automata2)
            showAutomata.showAutomata(automataIntersection, "Interseccion")

            automataComplement = None
            if option == "1":
                automataComplement = automataController.automataComplement(automataUnion)
            else:
                automataComplement = automataController.automataComplement(automataIntersection)
            showAutomata.showAutomata(automataComplement, "Complemento")
            automataReverse = automataController.automataReverse(automataIntersection)
            showAutomata.showAutomata(automataReverse[1], "SimpleReverse")
            showAutomata.showAutomata(automataReverse[0], "Reverso")

        else:
            automataUnion = automataController.automataUnion(automataController.automataUnion(automata1, automata2), automata3)
            showAutomata.showAutomata(automataUnion, "Union")
            automataIntersection = automataController.automataIntersection(automataController.automataIntersection(automata1, automata2), automata3)
            showAutomata.showAutomata(automataIntersection, "Interseccion")

            automataComplement = None
            if option == "1":
                automataComplement = automataController.automataComplement(automataUnion)
            else:
                automataComplement = automataController.automataComplement(automataIntersection)
            showAutomata.showAutomata(automataComplement, "Complemento")
            automataReverse = automataController.automataReverse(automataIntersection)
            showAutomata.showAutomata(automataReverse[1], "SimpleReverse")
            showAutomata.showAutomata(automataReverse[0], "Reverso")

        print ("Este es el estado inicial del automata union", automataUnion.initial_state)
        print ("Este es el estado inicial del automata interseccion", automataIntersection.initial_state)

        print ("Desea continuar? (s : si, cualquier otra letra : no)")

        option = input("Ingrese una opcion: ")

        if option.lower() != "s":
            break

if __name__ == "__main__":
    main()
