def check_fact(statement):
    known_facts = [
        "the earth is round",
        "water freezes at 0 degrees celsius",
        "the sun is a star"
    ]

    statement_lower = statement.lower()
    for fact in known_facts:
        if fact in statement_lower:
            return f"✅ This appears to be true: '{fact}'"

    return "⚠️ This statement could not be verified."

# Example usage:
user_input = "Did you know that the sun is a star?"
print("User said:", user_input)
result = check_fact(user_input)
print("Fact-check result:", result)
