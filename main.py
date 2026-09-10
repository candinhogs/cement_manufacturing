from cement import Cement

def main():
    option: int = 0
    registers = int(input("Quantidade de registros: "))
    cement = Cement(registers)

    while option != -1:
        print("1 - Registrar nova mistura.")
        print("2 - Calcular Estátisticas.")
        print("3 - Classificar baseado em caracteristicas.")
        print("4 - Mostrar registros cadastrados")
        print("-1 - Sair.")
        option = int(input("Opção: "))
        if option == 1:
            cement.register_new_cement_mix()
        elif option == 2:
            print("1 - Cálcular Média.")
            print("2 - Filtrar por intervalo de resistência.")
            print("3 - Filtrar por intervalo de idade.")
            option = int(input("Opção: "))
            if option == 1:
                cement.print_averages()
            if option == 2:
                cement.filter_by_inter_strength()
            if option == 3:
                cement.filter_by_inter_age()
        elif option == 3:
            choices = input("Escolha quais colunas para classificar: ").split(" ")
            by_age = bool(int(input("Deseja classificar por idade? (0 = Não, 1 = Sim) ")))
            by_ash = bool(int(input("Deseja classificar por cinzas? (0 = Não, 1 = Sim) ")))
            by_water = bool(int(input("Deseja classificar por água? (0 = Não, 1 = Sim) ")))
            cement.classification_by_choice(choices, by_age, by_ash, by_water)
        elif option == 4:
            cement.print_mixtures()
        # grothendieck prime!
        elif option == 57:
            cement._debug_print_registers()
        elif option == 21:
            cement._debug_insert_registers()

if __name__ == "__main__":
    main()

