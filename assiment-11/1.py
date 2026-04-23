
# Map Coloring with Print Output

graph = {
    "Kutch": ["Banaskantha", "Patan", "Surendranagar", "Jamnagar", "Rajkot"],

    "Banaskantha": ["Kutch", "Patan", "Mehsana", "Sabarkantha"],

    "Patan": ["Kutch", "Banaskantha", "Mehsana", "Surendranagar"],

    "Mehsana": ["Banaskantha", "Patan", "Sabarkantha", "Gandhinagar", "Ahmedabad", "Surendranagar"],

    "Sabarkantha": ["Banaskantha", "Mehsana", "Gandhinagar", "Panchmahal"],

    "Gandhinagar": ["Mehsana", "Sabarkantha", "Ahmedabad", "Kheda"],

    "Ahmedabad": ["Mehsana", "Gandhinagar", "Kheda", "Anand", "Bhavnagar", "Surendranagar"],

    "Surendranagar": ["Kutch", "Patan", "Mehsana", "Ahmedabad", "Rajkot"],

    "Kheda": ["Ahmedabad", "Gandhinagar", "Panchmahal", "Vadodara", "Anand"],

    "Anand": ["Ahmedabad", "Kheda", "Vadodara", "Bharuch"],

    "Panchmahal": ["Sabarkantha", "Kheda", "Dahod", "Vadodara"],

    "Dahod": ["Panchmahal", "Vadodara"],  

    "Vadodara": ["Kheda", "Anand", "Panchmahal", "Bharuch", "Narmada", "Dahod"],

    "Bharuch": ["Anand", "Vadodara", "Narmada", "Surat"],

    "Narmada": ["Vadodara", "Bharuch", "Surat"],

    "Surat": ["Bharuch", "Narmada", "Navsari"],

    "Navsari": ["Surat", "Dang", "Valsad"],

    "Valsad": ["Navsari", "Dang"],

    "Dang": ["Navsari", "Valsad"],

    "Rajkot": ["Surendranagar", "Kutch", "Jamnagar", "Porbandar", "Junagadh", "Amreli"],

    "Jamnagar": ["Kutch", "Rajkot", "Porbandar"],

    "Porbandar": ["Jamnagar", "Rajkot", "Junagadh"],

    "Junagadh": ["Porbandar", "Rajkot", "Amreli"],

    "Amreli": ["Junagadh", "Rajkot", "Bhavnagar"],

    "Bhavnagar": ["Amreli", "Ahmedabad"]
}
colors = ["Red", "Green", "Blue","yellow"]


def is_safe(node, color, assignment):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True


def solve(assignment):
    if len(assignment) == len(graph):
        return True

    node = list(graph.keys())[len(assignment)]

    for color in colors:
        print(f"Trying {color} for {node}")

        if is_safe(node, color, assignment):
            assignment[node] = color
            print(f"Assigned {node} = {color}")

            if solve(assignment):
                return True

            print(f"Backtracking on {node}")
            del assignment[node]

    return False


assignment = {}
solve(assignment)

print("\nFinal Coloring:")
for k, v in assignment.items():
    print(k, "->", v)