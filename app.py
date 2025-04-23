def check_fact(statement):
    known_facts = [
        "the earth is round",
        "water freezes at 0 degrees celsius",
        "the sun is a star"
    ]

    if statement.lower() in known_facts:
        return "✅ This statement is known to be true."
    else:
        return "⚠️ This statement could not be verified."

# Example usage:
user_input = "The earth is round"
print("User said:", user_input)
result = check_fact(user_input)
print("Fact-check result:", result)
