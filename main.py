from cement import Cement

def main():
    option: int = 0
    registers = int(input("Quantidade de registros: "))
    cement = Cement(registers)

    while option != -1:
        print("1 - Registrar nova mistura.")
        print("2 - Calcular Estátisticas.")
        print("-1 - Sair.")
        option = int(input("Opção: "))
        if option == 1:
            cement.register_new_cement_mix()
        elif option == 2:
            print("1 - Cálcular Média")
            option = int(input("Opção: "))
            if option == 1:
                cement.calculate_average()
        # grothendieck prime!
        elif option == 57:
            cement._debug_print_registers()

if __name__ == "__main__":
    main()