
environment = {
    "inbound_sensor": False,     # Train approaching
    "outbound_sensor": False,    # Train leaving
    "obstacle": False,           # Vehicle / animal stuck
    "emergency_lever": "Neutral" # Neutral / Active
}

# -------- LEVEL CROSSING AGENT --------    
def level_crossing_agent(percept):
    # Rule 1: Manual Emergency Override (Highest Priority)
    if percept["emergency_lever"] == "Active":
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Red"
        }

    # Rule 2: Obstacle detected
    if percept["obstacle"] == True:
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Red"
        }

    # Rule 3: Train approaching or passing
    if percept["inbound_sensor"] == True or percept["outbound_sensor"] == True:
        return {
            "Gate": "Lower",
            "Siren": "On",
            "Train_Signal": "Green"
        }

    # Rule 4: Normal safe condition
    return {
        "Gate": "Raise",
        "Siren": "Off",
        "Train_Signal": "Green"
    }


# -------- SIMULATION --------
print("PERCEPTS ------------------------> ACTIONS")

scenarios = [
    {
        "inbound_sensor": True,
        "outbound_sensor": False,
        "obstacle": False,
        "emergency_lever": "Neutral"
    },
    {
        "inbound_sensor": True,
        "outbound_sensor": False,
        "obstacle": True,
        "emergency_lever": "Neutral"
    },
    {
        "inbound_sensor": False,
        "outbound_sensor": True,
        "obstacle": False,
        "emergency_lever": "Neutral"
    },
    {
        "inbound_sensor": False,
        "outbound_sensor": False,
        "obstacle": False,
        "emergency_lever": "Neutral"
    }
]

for step, percept in enumerate(scenarios, start=1):
    action = level_crossing_agent(percept)
    print(f"\nStep {step}")
    print("Percept:", percept)
    print("Action :", action)
