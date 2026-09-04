class Cement():
    def __init__(self, registers: int):
        self.db = {"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []}
        self.registers = registers

    def register_new_cement_mix(self):
        """Register a new element iff there's 'space' for a new element (defined by registers)"""
        value: float = 0
        if len(self.db["cement"]) >= self.registers:
            print("Quantidade máxima de registros alcançada.\nNão é possível registrar uma nova mistura.")
        else:
            for element in self.db:
                value = float(input(f"Digite o valor para {element}: "))
                while value < 0:
                    print("Valor digitado inválido; Apenas entradas maiores ou iguais a zero são válidas.")
                    value = float(input(f"Digite o valor para {element}: "))
                self.db[element].append(value)

    def calculate_average(self):
        """Calculate the overall average of each element on the analysis"""
        # Get the current length of the database, since we can have a maximum length
        # and a request to calculate the average before we are given all the inputs.
        current_size: int = len(self.db["cement"]) + 1 # Python start's counting from 0

        # Calculate all the averages
        cement_average: float = sum(self.db["cement"]) / current_size
        slag_average: float = sum(self.db["slag"]) / current_size
        ash_average: float = sum(self.db["ash"]) / current_size
        water_average: float = sum(self.db["water"]) / current_size
        superplastic_average: float = sum(self.db["superplastic"]) / current_size
        coarseagg_average: float = sum(self.db["coarseagg"]) / current_size
        fineagg_average: float = sum(self.db["fineagg"]) / current_size
        age_average: float = sum(self.db["age"]) / current_size
        strength_average: float = sum(self.db["strength"]) / current_size

        # Print each average to the standard output
        print(f"Cimento médio dos {current_size} registros: {cement_average:.4f}")
        print(f"Escória de alto-forno médio dos {current_size} registros: {slag_average:.4f}")
        print(f"Cinzas volantes médio dos {current_size} registros: {ash_average:.4f}")
        print(f"Água média dos {current_size} registros: {water_average:.4f}")
        print(f"Aditivo superplastificante média dos {current_size} registros: {superplastic_average:.4f}")
        print(f"Agregado graudo média dos {current_size} registros: {coarseagg_average:.4f}")
        print(f"Agregado fino médio dos {current_size} registros: {fineagg_average:.4f}")
        print(f"Idade média dos {current_size} registros: {age_average:.4f}")
        print(f"Resistência média dos {current_size} registros: {strength_average:.4f}")

    def filter_by_inter_strength(self):
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: "))
        values = sorted(self.db["strength"])
        values = list(filter(lambda x: x >= 0 and x <= 1, values))
        print(values)

    def filter_by_inter_age(self):
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: "))
        values = sorted(self.db["age"])
        # A função/método filter aplica uma determinada função (geralmente anonima) em torno de um iterable,
        # em particular ela retorna um iterator, que pode ser convertido para uma lista.
        values = list(filter(lambda x: x >= 0 and x <= 1, values))
        print(values)

    # Método de debug; Remover após finalização
    def _debug_print_registers(self):
        for i in self.bd:
            print(self.bd[i])
        