known_facts = [
    "the earth is round",
    "water freezes at 0 degrees celsius",
    "the sun is a star"
]

def add_fact(new_fact):
    known_facts.append(new_fact.lower())
    print(f"New fact added: '{new_fact}'")

def check_fact(statement):
    statement_lower = statement.lower()
    for fact in known_facts:
        if fact in statement_lower:
            return f"✅ This appears to be true: '{fact}'"
    return "⚠️ This statement could not be verified."

# Example usage:
print("Welcome to Skywatch!")

add_input = input("Would you like to add a new fact? (yes/no): ")
if add_input.lower() == "yes":
    new_fact = input("Enter the fact you want to add: ")
    add_fact(new_fact)

user_input = input("Enter a statement to check: ")
result = check_fact(user_input)
print("Fact-check result:", result)
