---

## What is a Monte Carlo Simulation?

A Monte Carlo simulation is a computational algorithm that relies on repeated random sampling to obtain numerical results. It allows you to model the probability of different outcomes in processes that are uncertain due to the influence of random variables.

---

## How Does This Simulator Work?

The Monte Carlo Simulator:

- **Defines variables**: you specify different categories (variables) and their possible options with associated values.
- **Applies rules**: you set up rules that adjust the outcomes based on specific combinations of variables.
- **Generates combinations**: the simulator creates possible combinations of variables, either exhaustively or through random sampling.
- **Calculates scores**: it computes a score for each combination based on the variables and applied rules.
- **Provides top results**: the simulator outputs the top combinations with the highest scores to help you make the best decision.

---

## Getting Started

### Requirements

- **Python 3.x** installed on your system.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/monte-carlo-simulator.git
   
2.  **Navigate to the Directory**:

    ```bash
    cd monte-carlo-simulator

3.  **(Optional) Create a Virtual Environment**:

    ```bash
    python -m venv venv source venv/bin/activate  # On Windows use 'venv\Scripts\activate'

### Running the Simulator

Run the script using Python:

  ```bash
    python monte_carlo_simulator.py
   ``` 

* * * * *

Configuring the Simulator
-------------------------

You can customize the simulator to suit your needs by defining variables, setting up rules, and adjusting parameters.

### Defining Variables

Variables are the different categories you want to consider in your simulation. Each variable has options with associated values.

**Example:**

  ```python
    arrays = [
        {'May': 1, 'June': 2, 'July': 3},            # Months
        {'vacation': 10, 'work': -1},                # Activities
        {'sun': 5, 'rain': -2}                       # Weather conditions
    ]
  ```

-   **Months**: 'May', 'June', 'July' with values indicating preference or importance.
-   **Activities**: 'vacation' and 'work' with values representing the desirability.
-   **Weather**: 'sun' and 'rain' with values showing the impact on plans.

### Setting Up Rules

Rules modify the total score based on specific combinations of variables. Each rule has:

-   **Type**: A label for the rule (e.g., 'penalty', 'bonus').
-   **Elements**: A list of variables that trigger the rule when they appear together.
-   **Adjustment**: The value to adjust the score.
-   **Operation**: The mathematical operation to apply ('addition', 'multiplication', 'division').

**Example:**

```python
rules = [
    {
        'type': 'penalty',
        'elements': ['May', 'vacation'],
        'adjustment': -2,
        'operation': 'addition'
    },
    {
        'type': 'bonus',
        'elements': ['July', 'sun'],
        'adjustment': 3,
        'operation': 'addition'
    },
    {
        'type': 'multiplication',
        'elements': ['June', 'rain'],
        'adjustment': 0.5,
        'operation': 'multiplication'
    },
    {
        'type': 'division',
        'elements': ['July', 'work'],
        'adjustment': 2,
        'operation': 'division'
    }
]
```

### Adjusting Parameters

When initializing the simulator, you can adjust:

-   **top_x**: Number of top combinations to display.
-   **sampling_enabled**: Set to `True` to enable random sampling.
-   **sampling_percentage**: Percentage of total combinations to sample (only used if sampling is enabled).

**Example:**

```python
simulator = MonteCarloSimulator(
    arrays=arrays,
    rules=rules,
    top_x=5,
    sampling_enabled=True,
    sampling_percentage=50
)
```

* * * * *

Examples and Use Cases
----------------------

### Example 1: Event planning

**Scenario:** you're organizing a summer event and need to decide on the best month, activity, and expected weather to maximize attendance and enjoyment.

**Variables:**

```python
`arrays = [
    {'June': 2, 'July': 3, 'August': 4},        # Months
    {'concert': 8, 'festival': 10},             # Event types
    {'sunny': 5, 'cloudy': 2}                   # Weather forecasts
]`
```
**Rules:**

-   **Bonus** if the event is a festival in August during sunny weather.
-   **Penalty** if the event is a concert in July during cloudy weather.

```python
rules = [
    {
        'type': 'bonus',
        'elements': ['festival', 'August', 'sunny'],
        'adjustment': 5,
        'operation': 'addition'
    },
    {
        'type': 'penalty',
        'elements': ['concert', 'July', 'cloudy'],
        'adjustment': -3,
        'operation': 'addition'
    }
]
```

**Running the simulator:**

```python
simulator = MonteCarloSimulator(
    arrays=arrays,
    rules=rules,
    top_x=3,
    sampling_enabled=False
)
simulator.run()
```

**Sample Output:**

```css
Top 3 combinations:
Combination: ('August', 'festival', 'sunny'), Score: 19
Combination: ('August', 'concert', 'sunny'), Score: 17
Combination: ('July', 'festival', 'sunny'), Score: 15
```

**Interpretation:** the highest score is for holding a festival in August during sunny weather.

* * * * *

### Example 2: Business Strategy

**Scenario:** a company wants to decide the best combination of market, product, and promotion strategy to maximize profit.

**Variables:**

```python
arrays = [
    {'domestic': 5, 'international': 7},       # Market
    {'basic': 3, 'premium': 6},                # Product type
    {'online': 4, 'offline': 2}                # Promotion strategy
]
```

**Rules:**

-   **Bonus** for selling a premium product internationally with online promotion.
-   **Penalty** for selling a basic product domestically with offline promotion.

```python
rules = [
    {
        'type': 'bonus',
        'elements': ['international', 'premium', 'online'],
        'adjustment': 10,
        'operation': 'addition'
    },
    {
        'type': 'penalty',
        'elements': ['domestic', 'basic', 'offline'],
        'adjustment': -5,
        'operation': 'addition'
    }
]
```

**Running the Simulator:**

```python
simulator = MonteCarloSimulator(
    arrays=arrays,
    rules=rules,
    top_x=2,
    sampling_enabled=False
)
simulator.run()
```

**Sample Output:**

```css
Top 2 combinations:
Combination: ('international', 'premium', 'online'), Score: 27
Combination: ('international', 'premium', 'offline'), Score: 17
```

**Interpretation:** the optimal strategy is to sell a premium product internationally with online promotion.

* * * * *

Tips for Effective Use
----------------------

-   **Be specific with variables**: clearly define your variables and their values to reflect real-world scenarios accurately.
-   **Create neaningful rules**: establish rules that represent actual influences on outcomes to enhance the simulation's relevance.
-   **Consider sampling for large combinations**: if you have many variables and options, enable sampling to reduce computation time.
-   **Analyze results holistically**: Use the scores as guidance but consider other qualitative factors in your decision-making.

* * * * *

Troubleshooting
---------------

-   **Division by Zero Errors**: Ensure that any 'division' operations in your rules do not have an adjustment value of zero.
-   **Unexpected Results**: Double-check your variables and rules for typos or logical errors.
-   **Script Not Running**: Verify that you have Python 3.x installed and that all code dependencies are met.
