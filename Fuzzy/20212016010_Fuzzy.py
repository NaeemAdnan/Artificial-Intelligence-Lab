# Import necessary libraries
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the fuzzy logic system for food recommendation based on hunger and time of day
def food_recommendation_system(hunger_level, time_of_day_input):
    # Define the universe of discourse for each variable
    hunger = ctrl.Antecedent(np.arange(0, 11, 1), 'hunger')  # 0 (not hungry) to 10 (very hungry)
    time = ctrl.Antecedent(np.arange(0, 24, 1), 'time')  # 0 to 23 hours (renamed from `time_of_day`)
    food_recommendation = ctrl.Consequent(np.arange(0, 101, 1), 'food_recommendation')  # 0 to 100% probability

    # Define fuzzy sets for hunger
    hunger['not_hungry'] = fuzz.trimf(hunger.universe, [0, 0, 5])
    hunger['somewhat_hungry'] = fuzz.trimf(hunger.universe, [3, 5, 7])
    hunger['very_hungry'] = fuzz.trimf(hunger.universe, [6, 10, 10])

    # Define fuzzy sets for time of day
    time['breakfast'] = fuzz.trimf(time.universe, [0, 6, 10])
    time['lunch'] = fuzz.trimf(time.universe, [11, 14, 16])
    time['dinner'] = fuzz.trimf(time.universe, [17, 21, 23])

    # Define fuzzy sets for food recommendation
    food_recommendation['snack'] = fuzz.trimf(food_recommendation.universe, [0, 0, 50])
    food_recommendation['light_meal'] = fuzz.trimf(food_recommendation.universe, [25, 50, 75])
    food_recommendation['full_meal'] = fuzz.trimf(food_recommendation.universe, [50, 100, 100])

    # Define fuzzy rules
    rule1 = ctrl.Rule(hunger['not_hungry'] & time['breakfast'], food_recommendation['snack'])
    rule2 = ctrl.Rule(hunger['not_hungry'] & time['lunch'], food_recommendation['snack'])
    rule3 = ctrl.Rule(hunger['not_hungry'] & time['dinner'], food_recommendation['snack'])
    rule4 = ctrl.Rule(hunger['somewhat_hungry'] & time['breakfast'], food_recommendation['light_meal'])
    rule5 = ctrl.Rule(hunger['somewhat_hungry'] & time['lunch'], food_recommendation['light_meal'])
    rule6 = ctrl.Rule(hunger['somewhat_hungry'] & time['dinner'], food_recommendation['full_meal'])
    rule7 = ctrl.Rule(hunger['very_hungry'], food_recommendation['full_meal'])

    # Create the control system and simulation
    food_control = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7])
    food_simulation = ctrl.ControlSystemSimulation(food_control)

    # Ensure input values are floats
    food_simulation.input['hunger'] = float(hunger_level)
    food_simulation.input['time'] = float(time_of_day_input)  # Use `time` as the key here

    # Perform the computation
    food_simulation.compute()

    # Output the results
    recommendation_score = food_simulation.output['food_recommendation']
    print(f"Hunger Level: {hunger_level}/10")
    print(f"Time of Day: {time_of_day_input} hours")
    print(f"Food Recommendation Score: {recommendation_score:.2f}%")

# Example usage
if __name__ == "__main__":
    food_recommendation_system(hunger_level=8, time_of_day_input=12)  # Change these values to test different scenarios
