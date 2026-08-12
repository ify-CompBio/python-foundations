# --- Test data ---
number = 42
text = "ACTGACTG"
values = [1, 2, 3, 4]
records = {"gene": "TP53", "length": 2000}
nested = [{"id": 1}, {"id": 2}]

#--- Inspection ---
def inspect(obj, name):
    print(f"\nInspecting: {name}")

    print(f"Type: {type(obj)}")

    if hasattr(obj,"__len__"):
        print(f"Length: {len(obj)}")
    else:
        print(f"Length: Not applicable")

    print(f"Value = {obj}")


#--- Run inspections ---
inspect(number, "number")
inspect(text, "text")
inspect(values, "values")
inspect(records, "records")
inspect(nested, "nested")

#--- Notes ---

# Length is number of characters in strings, and number of entries in a list
# Dictionaries report length as number of keys
# Inspection prevents incorrect assumptions later