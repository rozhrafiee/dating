import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def build_fuzzy_system():
    # تعریف متغیرهای ورودی
    trust = ctrl.Antecedent(np.arange(0, 11, 1), 'trust')
    kindness = ctrl.Antecedent(np.arange(0, 11, 1), 'kindness')
    emotional = ctrl.Antecedent(np.arange(0, 11, 1), 'emotional_stability')
    financial = ctrl.Antecedent(np.arange(0, 11, 1), 'financial_stability')
    attention = ctrl.Antecedent(np.arange(0, 11, 1), 'attention')
    effort = ctrl.Antecedent(np.arange(0, 11, 1), 'effort')
    attraction = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_attraction')
    princess = ctrl.Antecedent(np.arange(0, 11, 1), 'princess_treatment')

    decision = ctrl.Consequent(np.arange(0, 101, 1), 'decision')

    # تابع عضویت استاندارد
    for var in [trust, kindness, emotional, financial, attention, effort, attraction, princess]:
        var['low'] = fuzz.trimf(var.universe, [0, 0, 5])
        var['medium'] = fuzz.trimf(var.universe, [2, 5, 8])
        var['high'] = fuzz.trimf(var.universe, [5, 10, 10])

    decision['dump'] = fuzz.trimf(decision.universe, [60, 100, 100])
    decision['maybe'] = fuzz.trimf(decision.universe, [30, 50, 70])
    decision['keep'] = fuzz.trimf(decision.universe, [0, 0, 40])

    # --- قوانین هوشمند فازی --- #
    rules = [
        # 💔 Dump
        ctrl.Rule(trust['low'] & emotional['low'] & effort['low'], decision['dump']),
        ctrl.Rule(kindness['low'] & attention['low'], decision['dump']),
        ctrl.Rule(princess['low'] & attraction['low'], decision['dump']),
        ctrl.Rule(trust['low'] & financial['low'], decision['dump']),
        ctrl.Rule(attraction['high'] & trust['low'] & kindness['low'], decision['dump']),
        ctrl.Rule(financial['low'] & effort['low'], decision['dump']),
        ctrl.Rule(princess['low'] & kindness['low'] & effort['low'], decision['dump']),
        ctrl.Rule(emotional['low'] & attention['low'], decision['dump']),
        ctrl.Rule(trust['low'] & princess['low'], decision['dump']),
        ctrl.Rule(attraction['low'] & attention['low'], decision['dump']),

        # 🤔 Maybe
        ctrl.Rule(trust['medium'] & kindness['medium'], decision['maybe']),
        ctrl.Rule(attention['high'] & trust['medium'], decision['maybe']),
        ctrl.Rule(financial['high'] & effort['low'], decision['maybe']),
        ctrl.Rule(attraction['high'] & princess['medium'], decision['maybe']),
        ctrl.Rule(emotional['high'] & trust['medium'], decision['maybe']),
        ctrl.Rule(kindness['medium'] & emotional['medium'], decision['maybe']),
        ctrl.Rule(princess['medium'] & attention['medium'], decision['maybe']),
        ctrl.Rule(effort['medium'] & attraction['medium'], decision['maybe']),
        ctrl.Rule(trust['medium'] & princess['high'], decision['maybe']),
        ctrl.Rule(effort['high'] & attention['low'], decision['maybe']),

        # 💖 Keep
        ctrl.Rule(trust['high'] & kindness['high'] & attention['high'], decision['keep']),
        ctrl.Rule(effort['high'] & princess['high'] & emotional['high'], decision['keep']),
        ctrl.Rule(trust['high'] & effort['high'] & princess['high'], decision['keep']),
        ctrl.Rule(kindness['high'] & emotional['high'] & effort['high'], decision['keep']),
        ctrl.Rule(trust['high'] & attraction['high'] & princess['high'], decision['keep']),
        ctrl.Rule(emotional['high'] & financial['high'] & trust['high'], decision['keep']),
        ctrl.Rule(princess['high'] & attention['high'] & kindness['high'], decision['keep']),
        ctrl.Rule(attraction['high'] & effort['high'] & kindness['high'], decision['keep']),
        ctrl.Rule(trust['high'] & kindness['high'] & emotional['high'], decision['keep']),
        ctrl.Rule(all(var['medium'] | var['high'] for var in [trust, kindness, emotional, financial, attention, effort, attraction, princess]), decision['keep']),
    ]

    system = ctrl.ControlSystem(rules)
    return ctrl.ControlSystemSimulation(system)

def get_decision(data: dict):
    sim = build_fuzzy_system()
    for key, value in data.items():
        sim.input[key] = value
    sim.compute()
    score = sim.output['decision']
    if score > 60:
        return 'Dump Him 💔'
    elif score < 40:
        return 'Keep Him 💖'
    else:
        return 'Maybe 🤔'
