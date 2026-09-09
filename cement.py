class Cement():
    def __init__(self, registers: int) -> None:
        self.db: dict = {"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []}
        self.registers: int = registers

    def register_new_cement_mix(self) -> None:
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

    def calculate_average(self) -> dict:
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

        averages = {"cement": cement_average, "slag": slag_average, "ash": ash_average, "water": water_average, "superplastic": superplastic_average, "coarseagg": coarseagg_average, "fineagg": fineagg_average, "age": age_average, "strength": strength_average}

        # Print each average to the standard output
        return averages

    def print_averages(self) -> None:
        """Helper function to print the averages, call's self.calculate_average()"""
        averages: dict = self.calculate_average()
        current_size: int = len(self.db["cement"]) + 1

        print(f"Cimento médio dos {current_size} registros: {averages["cement"]:.4f}")
        print(f"Escória de alto-forno médio dos {current_size} registros: {averages["slag"]:.4f}")
        print(f"Cinzas volantes médio dos {current_size} registros: {averages["ash"]:.4f}")
        print(f"Água média dos {current_size} registros: {averages["water"]:.4f}")
        print(f"Aditivo superplastificante média dos {current_size} registros: {averages["superplastic"]:.4f}")
        print(f"Agregado graudo média dos {current_size} registros: {averages["coarseagg"]:.4f}")
        print(f"Agregado fino médio dos {current_size} registros: {averages["fineagg"]:.4f}")
        print(f"Idade média dos {current_size} registros: {averages["age"]:.4f}")
        print(f"Resistência média dos {current_size} registros: {averages["strength"]:.4f}")

    def filter_by_inter_strength(self) -> None:
        """Filter by strength from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())
        values: list = sorted(self.db["strength"])
        values: list = list(filter(lambda x: x >= low and x <= high, values))
        print(values)

    def filter_by_inter_age(self) -> None:
        """Filter by age from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())
        values = sorted(self.db["age"])
        # A função/método filter aplica uma determinada função (geralmente anonima) em torno de um iterable,
        # em particular ela retorna um iterator, que pode ser convertido para uma lista.
        values = list(filter(lambda x: x >= low and x <= high, values))
        print(values)

    def classification_by_choice(self, choices: list, by_percentage=False) -> None:
        """Classifies each mixture based on: average, if by_percentage=True, then calculate the percentage of each compound on the mixture"""
        averages = self.calculate_average()
        results: list = []
        if by_percentage:
            percentage: float = float(input("Qual porcentagem as escolhas devem satisfazer [0 ~ 100]? "))

        for index in range(0, len(self.db["cement"])):
            mixture: list = []
            if self.db[choice][index] > averages[choice]:
                results[index][1] += 1

        print("As seguintes entradas satisfazem a classificação.")
        for result in results:
            if result[1] > 0 and result[1] <= 5:
                print(f"Atendimento baixo: {result[0:2]}")
            elif result[1] > 5 and result[1] <= 10:
                print(f"Atendimento intermediario: {result[0]}")
            elif result[1] > 10 and result[1] <= 15:
                print(f"Atendimento alto: {result[0]}")
            else:
                print("Não categorizado.")

    # Método de debug; Remover após finalização
    def _debug_insert_registers(self) -> None:
        self.db = {"cement": [540,342,276,531,135], "slag": [0,38,116,0,0], "ash": [0,0,90,0,166], "water": [173,228,179,141,180], "superplastic": [0,0,8,28,10], "coarseagg": [1125,670,870,852,961], "fineagg": [225,698,0,141,0], "age": [12,36,25,1,29], "strength": [1,28,9,36,4]}

    # Método de debug; Remover após finalização
    def _debug_print_registers(self) -> None:
        for i in self.db:
            print(self.db[i])

