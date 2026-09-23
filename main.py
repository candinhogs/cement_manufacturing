import os
from concrete import Concrete

def main():
    option: int = 0
    file_path = input("Digite o nome do arquivo com extensão: ")
    try:
        registers = int(input("Quantas entradas deseja ler: "))
    except ValueError:
        return "Valor incorreto, digite um número para a quantidade de entradas"
        
    concrete = Concrete(registers, file_path)
    
    while option != -1:
        print("1 - Registrar nova mistura.")
        print("2 - Calcular Estátisticas.")
        print("3 - Classificar baseado em caracteristicas.")
        print("4 - Mostrar registros cadastrados")
        print("-1 - Sair.")
        option = int(input("Opção: "))
        if option == 1:
            concrete.register_new_cement_mix()
        elif option == 2:
            print("-"*100)
            print("1 - Cálcular Média.")
            print("2 - Filtrar por intervalo de resistência.")
            print("3 - Filtrar por intervalo de idade.")
            option = int(input("Opção: "))
            if option == 1:
                concrete.print_averages()
            if option == 2:
                concrete.filter_by_inter_strength()
            if option == 3:
                concrete.filter_by_inter_age()
        elif option == 3:
            print("-"*100)
            choices = input("Escolha quais colunas para classificar: ").split(" ")
            by_age = bool(int(input("Deseja classificar por idade? (0 = Não, 1 = Sim) ")))
            by_ash = bool(int(input("Deseja classificar por cinzas? (0 = Não, 1 = Sim) ")))
            by_water = bool(int(input("Deseja classificar por água? (0 = Não, 1 = Sim) ")))
            concrete.classification_by_choice(choices, by_age, by_ash, by_water)
        elif option == 4:
            print("-"*100)
            print("1 - Todas as entradas.")
            print("2 - Entradas por intervalo.")
            option = int(input("Opção: "))
            if option == 1:
                concrete.print_mixtures()
            elif option == 2:
                concrete.print_by_range()
        # grothendieck prime!
        elif option == 57:
            concrete._debug_print_registers()
        elif option == 21:
            concrete._debug_insert_registers()

    return "Programa finalizado com sucesso."
            
if __name__ == "__main__":
    print(main())

