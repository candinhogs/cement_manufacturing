import pandas as pd
import numpy as np
from datetime import datetime

class Concrete():
    def __init__(self, registers: int, file_path: str) -> None:
        try:
            self.db = pd.read_csv(file_path, nrows=registers)
            pd.set_option("display.max_rows", registers)
        except FileNotFoundError:
            print("Arquivo não encontrado, iniciando um banco de dados vazio.")
            self.db = pd.DataFrame({"cement": [], "slag": [], "ash": [], "water": [], "superplastic": [], "coarseagg": [], "fineagg": [], "age": [], "strength": []})

        self.size = len(self.db)

    def print_mixtures(self) -> None:
        """Print to stdout every mixture of concrete."""
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
        """Register a new cement mix."""
        mix: dict = {}
        for element in self.db.columns:
            trying_input = True
            while trying_input:
                try:
                    value = float(input(f"Digite o valor para {element}: "))
                    mix[element] = value
                    # Além da verificação de trying_input para validar que foi dado um número,
                    # verificamos que o valor é de fato >= 0 antes de sair do laço while
                    if value >= 0:
                        trying_input = False
                except ValueError:
                    print(f"Digite um valor numérico para registro de {element}")
                    value = input(f"Digite o valor para {element}: ")
        self.db = pd.concat(
            [self.db, pd.DataFrame([mix])],
            ignore_index=True
        )
        self.size = len(self.db)
        pd.set_option("display.max_rows", self.size)

    def calculate_average(self) -> dict:
        """Calculate the overall average of each element on the analysis"""
        if self.size == 0:
            averages = {"cement": None, "slag": None, "ash": None, "water": None, "superplastic": None, "coarseagg": None, "fineagg": None, "age": None, "strength": None}
        else:
            # Calculate all the averages
            cement_average: float = sum(self.db["cement"]) / self.size
            slag_average: float = sum(self.db["slag"]) / self.size
            ash_average: float = sum(self.db["ash"]) / self.size
            water_average: float = sum(self.db["water"]) / self.size
            superplastic_average: float = sum(self.db["superplastic"]) / self.size
            coarseagg_average: float = sum(self.db["coarseagg"]) / self.size
            fineagg_average: float = sum(self.db["fineagg"]) / self.size
            age_average: float = sum(self.db["age"]) / self.size
            strength_average: float = sum(self.db["strength"]) / self.size

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

    def show_mean_min_max(self, column: str, summary: bool=False) -> dict:
        """Given a column, show the mean, min and max; Returns a dict with each value; If column isn't find return None"""
        values_mean_min_max: dict = {"mean": None, "min": None, "max": None}
        if column.isalpha() and column in self.db:
            values_mean_min_max["mean"] = self.db[column].mean()
            values_mean_min_max["min"] = self.db[column].min()
            values_mean_min_max["max"] = self.db[column].max()
            print(f"Para {column} são:")
            print(f"Média: {values_mean_min_max['mean']}")
            print(f"Mínimo: {values_mean_min_max['min']}")
            print(f"Máximo: {values_mean_min_max['max']}")
            if summary:
                return f"Para {column}: Média {values_mean_min_max['mean']} Mínimo: {values_mean_min_max['min']} Máximo: {values_mean_min_max['max']}\n"
        else:
            print("Coluna não encontrada")
            values_mean_min_max: dict = {"mean": None, "min": None, "max": None}
        return values_mean_min_max

    def print_averages(self) -> None:
        """Helper method to print the averages, call's self.calculate_average()"""
        averages: dict = self.calculate_average()

        if averages["cement"] == None:
            print("Não há registros para calcular a média")
        else:
            print(f"Cimento médio dos {self.size} registros: {averages['cement']:.4f}")
            print(f"Escória de alto-forno médio dos {self.size} registros: {averages['slag']:.4f}")
            print(f"Cinzas volantes médio dos {self.size} registros: {averages['ash']:.4f}")
            print(f"Água média dos {self.size} registros: {averages['water']:.4f}")
            print(f"Aditivo superplastificante média dos {self.size} registros: {averages['superplastic']:.4f}")
            print(f"Agregado graudo média dos {self.size} registros: {averages['coarseagg']:.4f}")
            print(f"Agregado fino médio dos {self.size} registros: {averages['fineagg']:.4f}")
            print(f"Idade média dos {self.size} registros: {averages['age']:.4f}")
            print(f"Resistência média dos {self.size} registros: {averages['strength']:.4f}")

    def filter_by_inter_strength(self) -> None:
        """Filter by strength from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())

        for i, strength in enumerate(self.db["strength"]):
            print(f"Indice: {i}: ", end="")
            if low <= strength <= high:
                print("[", end=" ")
                for column in self.db.keys():
                    print(f"{self.db[column][i]}", end=" ")
                    print("]")

    def sort_by_values(self, columns: list) -> None:
        print(self.db.sort_values(columns))

    def filter_by_inter_age(self) -> None:
        """Filter by age from the current input (dict), the values which satisfies the low, high pair"""
        low, high = map(float, input("Digite dois valores minimo e máximo para o intervalo: ").split())

        for i, age in enumerate(self.db["age"]):
            print(f"Indice: {i}: ", end="")
            if low <= age <= high:
                print("[", end=" ")
                for column in self.db:
                    print(f"{self.db[column][i]}", end=" ")
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
        low_result: list = [x[0] for x in results if x[1] > 0 and x[1] <= 15]
        medium_result: list = [x[0] for x in results if x[1] > 15 and x[1] <= 25]
        high_result: list = [x[0] for x in results if x[1] > 25]
        nc_result: list = [x[0] for x in results if x[1] == 0]
        print(f"Indices de baixo atendimento: {low_result}")
        print(f"Indices de médio atendimento: {medium_result}")
        print(f"Indices de alto atendimento: {high_result}")
        print(f"Indices não classificados: {nc_result}")
        return f"\nIndices de baixo atendimento: {low_result}\nIndices de médio atendimento: {medium_result}\nIndices de alto atendimento: {high_result} indices não classificados: {nc_result}\n"

    def _summary_section(self, title: str) -> str:
        """Return a formatted section header for the report."""
        return f"\n{'=' * 70}\n{title}\n{'=' * 70}\n"

    def _summary_fmt_df(self, df, precision: int = 4) -> str:
        """Return a DataFrame as a rounded string, safe against empty/None."""
        if df is None or (hasattr(df, "empty") and df.empty):
            return "  (no data)\n"
        return df.round(precision).to_string() + "\n"

    def _summary_valid_mask(self):
        """Return a boolean mask: True for rows with no NaN and no negative numeric values."""
        numeric = self.db.select_dtypes(include="number")
        if numeric.empty:
            return pd.Series([True] * len(self.db), index=self.db.index)
        no_nan = ~numeric.isna().any(axis=1)
        no_neg = (numeric >= 0).all(axis=1)
        return no_nan & no_neg

    def _summary_bins(self, column: str, bins: list, labels: list):
        """Cut a column into labeled bins and count occurrences per bin."""
        if column not in self.db.columns or self.db.empty:
            return pd.Series(dtype=int)
        cut = pd.cut(self.db[column], bins=bins, labels=labels, include_lowest=True)
        return cut.value_counts().sort_index()

    def _summary_group_means(self, column: str, bins: list, labels: list):
        """Group numeric columns by bins of `column` and return the mean per group."""
        numeric = self.db.select_dtypes(include="number")
        if column not in numeric.columns or numeric.empty:
            return pd.DataFrame()
        cut = pd.cut(numeric[column], bins=bins, labels=labels, include_lowest=True)
        return numeric.groupby(cut, observed=False).mean()

    def _summary_apply_filters(self, filters: list):
        """Apply a list of (column, low, high) filters, returning the filtered DataFrame."""
        df = self.db.copy()
        applied = []
        for col, lo, hi in filters or []:
            if col not in df.columns:
                continue
            if lo > hi:
                lo, hi = hi, lo
                df = df[(df[col] >= lo) & (df[col] <= hi)]
                applied.append(f"{col} in [{lo}, {hi}]")
                df.attrs["applied"] = applied
        return df

    def _summary_rules_classification(self, rules: dict = None,
                                      by_age: float = None,
                                      by_ash: float = None,
                                      by_water: float = None,
                                      low_max: int = 2,
                                      med_max: int = 4) -> dict:
        """Classify each row by rules, without input(); returns dict of index lists per class."""
        rules = rules or {}
        scores: list = []
        for i in range(len(self.db)):
            score = 0
            for col, limit in rules.items():
                if col in self.db.columns and self.db[col].iloc[i] > limit:
                    score += 1
            if by_age is not None and "age" in self.db.columns and self.db["age"].iloc[i] < by_age:
                score += 1
            if by_ash is not None and "ash" in self.db.columns and self.db["ash"].iloc[i] < by_ash:
                score += 1
            if by_water is not None and "water" in self.db.columns and self.db["water"].iloc[i] < by_water:
                score += 1
                scores.append((i, score))
        return {
            "low":            [i for i, s in scores if 0 < s <= low_max],
            "medium":         [i for i, s in scores if low_max < s <= med_max],
            "high":           [i for i, s in scores if s > med_max],
            "not classified": [i for i, s in scores if s == 0],
        }

    def generate_summary(self, output_path: str = "relatorio.txt", filters: list = None, rules: dict = None, rules_by_age: float = None, rules_by_ash: float = None, rules_by_water: float = None, age_bins: list = None, age_labels: list = None, strength_bins: list = None, strength_labels: list = None, cement_bins: list = None, cement_labels: list = None) -> None:
        """Generate the full text report covering every required item and write it to output_path."""
        age_bins = age_bins or [0, 7, 28, 90, 180, np.inf]
        age_labels = age_labels or ["0-7d", "8-28d", "29-90d", "91-180d", ">180d"]
        strength_bins = strength_bins or [0, 20, 35, 50, np.inf]
        strength_labels = strength_labels or ["<20 MPa", "20-35 MPa", "35-50 MPa", ">50 MPa"]
        cement_bins = cement_bins or [0, 200, 300, 400, np.inf]
        cement_labels = cement_labels or ["<200", "200-300", "300-400", ">400"]

        print("-" * 5, "Gerando relatório", "-" * 5)
        with open(output_path, "w", encoding="utf-8") as file:
            file.write("RELATÓRIO DE ANÁLISE DE CONCRETO\n")
            file.write(f"Gerado em: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write(f"Total de registros no banco: {self.size}\n")

            file.write(self._summary_section("QUANTIDADE TOTAL DE REGISTROS"))
            file.write(f"  Total: {len(self.db)}\n")

            file.write(self._summary_section("REGISTROS VÁLIDOS x INVÁLIDOS"))
            valid_mask = self._summary_valid_mask()
            n_valid = int(valid_mask.sum())
            n_invalid = int((~valid_mask).sum())
            file.write(f"  Válidos:   {n_valid}\n")
            file.write(f"  Inválidos: {n_invalid}\n")
            if n_invalid:
                file.write(f"  Índices inválidos: {list(self.db.index[~valid_mask])}\n")

            file.write(self._summary_section("MÉDIAS DAS VARIÁVEIS NUMÉRICAS"))
            numeric = self.db.select_dtypes(include="number")
            if numeric.empty:
                file.write("  (sem colunas numéricas)\n")
            else:
                for col, val in numeric.mean().items():
                    file.write(f"  {col:<15}: {val:.4f}\n")

            file.write(self._summary_section("MÍNIMO E MÁXIMO POR INDICADOR"))
            if numeric.empty:
                file.write("  (sem colunas numéricas)\n")
            else:
                min_max = pd.DataFrame({"min": numeric.min(), "max": numeric.max()})
                file.write(self._summary_fmt_df(min_max))

            file.write(self._summary_section("DISTRIBUIÇÃO POR FAIXAS DE IDADE"))
            dist_age = self._summary_bins("age", age_bins, age_labels)
            file.write(self._summary_fmt_df(dist_age.to_frame("count")))

            file.write(self._summary_section("DISTRIBUIÇÃO POR FAIXAS DE RESISTÊNCIA"))
            dist_strength = self._summary_bins("strength", strength_bins, strength_labels)
            file.write(self._summary_fmt_df(dist_strength.to_frame("count")))

            file.write(self._summary_section("MÉDIAS AGRUPADAS POR FAIXA DE IDADE"))
            file.write(self._summary_fmt_df(
                self._summary_group_means("age", age_bins, age_labels)
            ))

            file.write(self._summary_section("MÉDIAS AGRUPADAS POR FAIXA DE CIMENTO"))
            file.write(self._summary_fmt_df(
                self._summary_group_means("cement", cement_bins, cement_labels)
            ))

            file.write(self._summary_section("RANKING POR STRENGTH (top 10 / bottom 10)"))
            if "strength" in self.db.columns and not self.db.empty:
                ranked = self.db.sort_values("strength", ascending=False)
                file.write("  TOP 10 (maior strength):\n")
                file.write(self._summary_fmt_df(ranked.head(10)))
                file.write("  BOTTOM 10 (menor strength):\n")
                file.write(self._summary_fmt_df(ranked.tail(10)))
            else:
                file.write("  (coluna 'strength' ausente)\n")

            file.write(self._summary_section("RESULTADOS DOS FILTROS"))
            if not filters:
                file.write("  (nenhum filtro informado)\n")
            else:
                filtered = self._summary_apply_filters(filters)
                file.write(f"  Filtros aplicados: {filtered.attrs.get('applied', [])}\n")
                file.write(f"  Registros resultantes: {len(filtered)}\n")
                file.write(self._summary_fmt_df(filtered))

            file.write(self._summary_section("DADOS AUSENTES POR COLUNA"))
            missing = self.db.isna().sum()
            pct = (missing / max(len(self.db), 1)) * 100
            missing_df = pd.DataFrame({"ausentes": missing, "%": pct})
            file.write(self._summary_fmt_df(missing_df, precision=2))

            file.write(self._summary_section("COMPARAÇÃO DESCRITIVA ENTRE GRUPOS (por faixa de idade)"))
            if "age" not in self.db.columns or numeric.empty:
                file.write("  (coluna 'age' ausente ou sem colunas numéricas)\n")
            else:
                cut = pd.cut(self.db["age"], bins=age_bins, labels=age_labels, include_lowest=True)
                key_cols = [c for c in ["cement", "water", "strength"] if c in numeric.columns]
                if key_cols:
                    grouped = self.db.groupby(cut, observed=False)[key_cols].agg(
                        ["count", "mean", "std", "min", "max"]
                    )
                    file.write(self._summary_fmt_df(grouped))
                else:
                    file.write("  (sem colunas-chave para comparar)\n")

            file.write(self._summary_section("CLASSIFICAÇÃO BASEADA EM REGRAS"))
            classification = self._summary_rules_classification(
                rules=rules,
                by_age=rules_by_age,
                by_ash=rules_by_ash,
                by_water=rules_by_water,
            )

            file.write(f"  Critérios 'maior que': {rules or {}}\n")
            file.write(f"  Limites 'menor que': idade={rules_by_age}, "
                       f"cinzas={rules_by_ash}, água={rules_by_water}\n")

            for cls, indexes in classification.items():
                file.write(f"  {cls:<18}: {indexes}\n")

            file.write(self._summary_section("ARQUIVO GERADO"))
            file.write(f"  Relatório salvo em: {output_path}\n")

        print(f"Relatório gerado e salvo em {output_path}")
