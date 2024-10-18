import itertools
import random
import math

class MonteCarloSimulator:
    def __init__(self, arrays, rules, top_x=5, sampling_enabled=True, sampling_percentage=50):
        """
        Initializes the Monte Carlo Simulator with the given parameters.

        Parameters:
        - arrays (list of dict): A list of dictionaries representing variables and their values.
        - rules (list of dict): A list of rules to adjust scores based on combinations.
        - top_x (int): Number of top combinations to return.
        - sampling_enabled (bool): If True, uses random sampling based on percentage.
        - sampling_percentage (float): Percentage of possible combinations to generate (0-100).
        """
        self.arrays = arrays
        self.rules = rules
        self.top_x = top_x
        self.sampling_enabled = sampling_enabled
        self.sampling_percentage = sampling_percentage
        self.results = []

    def apply_rules(self, combination, base_score):
        """
        Applies the defined rules to adjust the base score of a combination.

        Parameters:
        - combination (tuple): The combination of elements.
        - base_score (float): The initial score before applying rules.

        Returns:
        - float: The total score after applying rules.
        """
        total_score = base_score
        for rule in self.rules:
            if all(element in combination for element in rule['elements']):
                operation = rule['operation']
                adjustment = rule['adjustment']
                if operation == 'addition':
                    total_score += adjustment
                elif operation == 'multiplication':
                    total_score *= adjustment
                elif operation == 'division':
                    if adjustment != 0:
                        total_score /= adjustment
                    else:
                        print("Error: Division by zero in rule:", rule)
        return total_score

    def generate_combinations(self):
        """
        Generates combinations and calculates their scores.
        """
        total_combinations = math.prod(len(arr.keys()) for arr in self.arrays)
        if self.sampling_enabled:
            num_samples = int((self.sampling_percentage / 100) * total_combinations)
            num_samples = min(num_samples, total_combinations)
            generated_combinations = set()
            
            while len(generated_combinations) < num_samples:
                combination = tuple(random.choice(list(arr.keys())) for arr in self.arrays)
                if combination not in generated_combinations:
                    generated_combinations.add(combination)
                    base_score = sum(self.arrays[i][combination[i]] for i in range(len(combination)))
                    total_score = self.apply_rules(combination, base_score)
                    self.results.append({'combination': combination, 'score': total_score})
        else:
            variable_lists = [list(arr.keys()) for arr in self.arrays]
            all_combinations = itertools.product(*variable_lists)
            
            for combination in all_combinations:
                base_score = sum(self.arrays[i][combination[i]] for i in range(len(combination)))
                total_score = self.apply_rules(combination, base_score)
                self.results.append({'combination': combination, 'score': total_score})

    def get_top_combinations(self):
        """
        Retrieves the top combinations based on their scores.

        Returns:
        - list of dict: The top combinations with their scores.
        """
        # Sort results based on score
        self.results.sort(key=lambda x: x['score'], reverse=True)
        # Get top x unique combinations
        top_combinations = []
        seen_combinations = set()
        for result in self.results:
            comb = result['combination']
            if comb not in seen_combinations:
                seen_combinations.add(comb)
                top_combinations.append(result)
            if len(top_combinations) == self.top_x:
                break
        return top_combinations

    def run(self):
        """
        Runs the Monte Carlo simulation and prints the top combinations.
        """
        self.generate_combinations()
        top_combinations = self.get_top_combinations()
        print(f"Top {self.top_x} combinations:")
        for result in top_combinations:
            print(f"Combination: {result['combination']}, Score: {result['score']}")

def main():
    arrays = [
        {'May': 1, 'June': 2, 'July': 3},
        {'vacation': 10, 'work': -1},
        {'sun': 5, 'rain': -2}
    ]

    rules = [
        {'type': 'penalty', 'elements': ['May', 'vacation'], 'adjustment': -2, 'operation': 'addition'},
        {'type': 'bonus', 'elements': ['July', 'sun'], 'adjustment': 3, 'operation': 'addition'},
        {'type': 'multiplication', 'elements': ['June', 'rain'], 'adjustment': 0.5, 'operation': 'multiplication'},
        {'type': 'division', 'elements': ['July', 'work'], 'adjustment': 2, 'operation': 'division'}
    ]

    simulator = MonteCarloSimulator(
        arrays=arrays,
        rules=rules,
        top_x=5,
        sampling_enabled=True,
        sampling_percentage=50
    )
    simulator.run()

if __name__ == "__main__":
    main()
