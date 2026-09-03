class Cement():
    def __init__(self, registers: int):
        self.db = {"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []}
        self.registers = registers

    def register_new_cement_mix(self):
        value: float = 0
        for element in self.db:
            value = float(input(f"Digite o valor para {element}: "))
            while value < 0:
                print("Valor digitado inválido; Apenas entradas maiores ou iguais a zero são válidas.")
                value = float(input(f"Digite o valor para {element}: "))
            self.db[element].append(value)

    def calculate_average(self):
        """Calculate the overall average of each element on the analysis"""
        cement_average: float = sum(self.db["cement"]) / self.registers
        slag_average: float = sum(self.db["slag"]) / self.registers
        ash_average: float = sum(self.db["ash"]) / self.registers
        water_average: float = sum(self.db["water"]) / self.registers
        superplastic_average: float = sum(self.db["superplastic"]) / self.registers
        coarseagg_average: float = sum(self.db["coarseagg"]) / self.registers
        fineagg_average: float = sum(self.db["fineagg"]) / self.registers
        age_average: float = sum(self.db["age"]) / self.registers
        strength_average: float = sum(self.db["strength"]) / self.registers

        print(f"Cimento médio dos {self.registers} registros: {cement_average:.4f}")
        print(f"Escória de alto-forno médio dos {self.registers} registros: {slag_average:.4f}")
        print(f"Cinzas volantes médio dos {self.registers} registros: {ash_average:.4f}")
        print(f"Água média dos {self.registers} registros: {water_average:.4f}")
        print(f"Aditivo superplastificante média dos {self.registers} registros: {superplastic_average:.4f}")
        print(f"Agregado graudo média dos {self.registers} registros: {coarseagg_average:.4f}")
        print(f"Agregado fino médio dos {self.registers} registros: {fineagg_average:.4f}")
        print(f"Idade média dos {self.registers} registros: {age_average:.4f}")
        print(f"Resistência média dos {self.registers} registros: {strength_average:.4f}")
    
    # Método de debug; Remover após finalização
    def _debug_print_registers(self):
        for i in self.bd:
            print(self.bd[i])
        