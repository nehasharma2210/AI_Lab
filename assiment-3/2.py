environment = [
    ["inbound_sensor",False],
    ["outbound_sensor",False],
    ["obstacle",False],
    ["emergency_lever","Neutral"]
]
dict={
    "inbound_sensor":0,
    "outbound_sensor":1,
    "obstacle":2,
    "emergency_lever":3,
    True:1,
    False:0,
    "Neutral":0,
    "Active":1

}
actions=[["inbound_sensor",[False,"Raise","Off","Green"],[True,"Lower","On","Red"]],
        ["outbound_sensor",[False,"Raise","Off","Green"],[True,"Lower","On","Red"]],
        ["obstacle",[False,"Raise","Off","Green"],[True,"Lower","On","Red"]],
        ["emergency_lever",["Neutral","Raise","Off","Green"],["Active","Lower","On","Red"]]]

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

print("PERCEPTS ------------------------> ACTIONS")

for step, percept in enumerate(scenarios, start=1):

    print(f"\nStep {step}")
    print("Percept:", percept)

    for rule in actions:
        sensor = rule[0]

        env_value = percept[sensor]        # True / False / Neutral / Active
        value_index = dict[env_value]

        selected_action = rule[value_index + 1][1:]
        print(['Gate','Siren','train_Signal'])
        print("Action :", selected_action)
        break
