class Cement():
    def __init__(self, registers: int) -> None:
        self.db = {"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []}
        self.registers = registers

    def register_new_cement_mix(self -> None):
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

    def calculate_average(self) -> None:
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

    def filter_by_inter_strength(self) -> None:
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: "))
        values = sorted(self.db["strength"])
        values = list(filter(lambda x: x >= low and x <= high, values))
        print(values)

    def filter_by_inter_age(self) -> None:
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: "))
        values = sorted(self.db["age"])
        # A função/método filter aplica uma determinada função (geralmente anonima) em torno de um iterable,
        # em particular ela retorna um iterator, que pode ser convertido para uma lista.
        values = list(filter(lambda x: x >= low and x <= high, values))
        print(values)

    def classification_by_choice(self, choices: list) -> None:
        averages = self.calculate_average()

        print(f"As seguintes entradas satisfazem a classificação: {results}")

    # Método de debug; Remover após finalização
    def _debug_insert_registers(self) -> None:
        self.db = {"cement": [540,342,276,531,135], "slag": [0,38,116,0,0], "ash": [0,0,90,0,166], "water": [173,228,179,141,180], "superplastic": [0,0,8,28,10], "coarseagg": [1125,670,870,852,961], "fineagg": [225,698,0,141,0], "age": [12,36,25,1,29], "strength": [1,28,9,36,4]}

    # Método de debug; Remover após finalização
    def _debug_print_registers(self) -> None:
        for i in self.db:
            print(self.db[i])

