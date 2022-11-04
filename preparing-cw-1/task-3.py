def if_brackets_are_correctly_placed_in(text: str) -> str:
    modified = "".join(filter(lambda symbol: (symbol == '(' or symbol == ')'), text))
    return "так" if text.count('(') == text.count(')') and modified.endswith(')') and modified.startswith('(') else "ні"

print(if_brackets_are_correctly_placed_in("sw(ss(sd)sd)"))