import pandas as pd

class Concrete():
    def __init__(self, registers: int, file_path: str) -> None:
        try:
            self.db = pd.read_csv(file_path, nrows=registers)
            pd.set_option("display.max_rows", registers)
        except FileNotFoundError:
            print("Arquivo não encontrado, iniciando um banco de dados vazio.")
            self.db = pd.DataFrame({"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []})
            self.size = len(db)
            
    def print_mixtures(self) -> None:
        """Print to stdout every mixture of concrete, not fancy."""
        print(self.db.loc[:,:])

    def print_by_range(self) -> None:
        """Given a range [a,b] print all rows in that range"""
        try:
            low = int(input("Digite o indece da primeira linha: "))
            high = int(input("Digite o indece da última linha: "))
        except ValueError:
            raise ValueError("Por favor, digite um número inteiro para o indíce")
        print(self.db.loc[low:high,:])
        
    def register_new_cement_mix(self) -> None:
        """Register a new element iff there's 'space' for a new element (defined by registers)"""
        value: float = 0
        for element in self.db:
            value = float(input(f"Digite o valor para {element}: "))
            while value < 0:
                print("Valor digitado inválido; Apenas entradas maiores ou iguais a zero são válidas.")
                value = float(input(f"Digite o valor para {element}: "))
                self.db[element].append(value)
                self.size = len(db)

    def calculate_average(self) -> dict:
        """Calculate the overall average of each element on the analysis"""
        if self.size == 0:
            averages = {"cement": None, "slag": None, "ash": None, "water": None, "superplastic": None, "coarseagg": None, "fineagg": None, "age": None, "strength": None}
        else:
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

        return averages

    def calculate_row_percent(self, index: int) -> dict:
        """Calculate the percent of each element"""
        total = sum(self.db.iloc[index])
        element_percent = {
            "cement": (self.db.iloc[index]["cement"] * 100) / total,
            "slag": (self.db.iloc[index]["slag"] * 100) / total,
            "ash": (self.db.iloc[index]["ash"] * 100) / total,
            "water": (self.db.iloc[index]["water"] * 100) / total,
            "superplastic": (self.db.iloc[index]["superplastic"] * 100) / total,
            "coarseagg": (self.db.iloc[index]["coarseagg"] * 100) / total,
            "fineagg": (self.db.iloc[index]["fineagg"] * 100) / total,
            "age": (self.db.iloc[index]["age"] * 100) / total,
            "strength": (self.db.iloc[index]["strength"] * 100) / total
        }
        return element_percent

    def show_percent_of_element_by_row(self) -> None:
        """Helper method, print's a given row percentage of each element"""
        index: int = int(input("Digite qual indíce deseja visualizar a porcentagem de cada elemento: "))
        element_percentage: dict = self.calculate_row_percent(index)
        for column in element_percentage.keys():
            print(f"A porcentagem de {column} na mistura é: {element_percentage[column]:.2f}%")
    
    def show_mean_min_max(self, column: str) -> dict:
        """Given a column, show the mean, min and max; Returns a dict with each value"""
        values_mean_min_max: dict = {"mean": None, "min": None, "max": None}
        values_mean_min_max["mean"] = self.db[column].mean()
        values_mean_min_max["min"] = self.db[column].min()
        values_mean_min_max["max"] = self.db[column].max()
        print(f"Para {column} são:")
        print(f"Média: {values_mean_min_max['mean']}")
        print(f"Mínimo: {values_mean_min_max['min']}")
        print(f"Máximo: {values_mean_min_max['max']}")
        return values_mean_min_max
    
    def print_averages(self) -> None:
        """Helper method to print the averages, call's self.calculate_average()"""
        averages: dict = self.calculate_average()
        
        if averages["cement"] == None:
            print("Não há registros para calcular a média")
        else:
            print(f"Cimento médio dos {self.size} registros: {averages["cement"]:.4f}")
            print(f"Escória de alto-forno médio dos {self.size} registros: {averages["slag"]:.4f}")
            print(f"Cinzas volantes médio dos {self.size} registros: {averages["ash"]:.4f}")
            print(f"Água média dos {self.size} registros: {averages["water"]:.4f}")
            print(f"Aditivo superplastificante média dos {self.size} registros: {averages["superplastic"]:.4f}")
            print(f"Agregado graudo média dos {self.size} registros: {averages["coarseagg"]:.4f}")
            print(f"Agregado fino médio dos {self.size} registros: {averages["fineagg"]:.4f}")
            print(f"Idade média dos {self.size} registros: {averages["age"]:.4f}")
            print(f"Resistência média dos {self.size} registros: {averages["strength"]:.4f}")

    def filter_by_inter_strength(self) -> None:
        """Filter by strength from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())

        for i, strength in enumerate(self.db["strength"]):
            if low <= strength <= high:
                print("Registros: [", end=" ")
                for column in self.db.keys():
                    print(f"{self.db[column][i]},", end=" ")
                    print("]")

    def filter_by_inter_age(self) -> None:
        """Filter by age from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())

        for i, age in enumerate(self.db["age"]):
            if low <= age <= high:
                print("Registros: [", end=" ")
                for column in self.db:
                    print(f"{self.db[column][i]},", end=" ")
                    print("]")
                    
    def classification_by_choice(self, choices: list, by_age: bool, by_ash: bool, by_water: bool) -> None:
        """Classifies each mixture based on: average, if by_percentage=True, then calculate the percentage of each compound on the mixture"""
        averages = self.calculate_average()
        results: list = []

        age = 0
        ash = 0
        water = 0

        if by_age:
            age: float = float(input("Qual idade máxima? "))
        if by_ash:
            ash: float = float(input("Qual a quantidade de cinzas máxima? "))
        if by_water:
            water: float = float(input("Qual a quantidade máxima de água? "))
            
        for index in range(0, len(self.db["cement"])):
            results.append([index, 0])
            for choice in choices:
                if self.db[choice][index] > averages[choice]:
                    results[index][1] += 1
                if self.db["age"][index] < age:
                    results[index][1] += 1
                if self.db["ash"][index] < ash:
                    results[index][1] += 1
                if self.db["water"][index] < water:
                    results[index][1] += 1

        print("As seguintes entradas satisfazem a classificação de acordo com os críterios.")
        low_result: list = [x[0] for x in results if x[1] > 0 and x[1] <= 10]
        medium_result: list = [x[0] for x in results if x[1] > 10 and x[1] <= 20]
        high_result: list = [x[0] for x in results if x[1] > 20]
        nc_result: list = [x[0] for x in results if x[1] == 0]
        print(f"Indices de baixo atendimento: {low_result}")
        print(f"Indices de médio atendimento: {medium_result}")
        print(f"Indices de alto atendimento: {high_result}")
        print(f"Indices não classificados: {nc_result}")
        
    # Método de debug; Remover após finalização
    def _debug_insert_registers(self) -> None:
        self.db = {"cement": [540,342,276,531,135], "slag": [0,38,116,0,0], "ash": [0,0,90,0,166], "water": [173,228,179,141,180], "superplastic": [0,0,8,28,10], "coarseagg": [1125,670,870,852,961], "fineagg": [225,698,0,141,0], "age": [12,36,25,1,29], "strength": [1,28,9,36,4]}
        self.size = len(db)
        
    # Método de debug; Remover após finalização
    def _debug_print_registers(self) -> None:
        for i in self.db:
            print(self.db[i])
