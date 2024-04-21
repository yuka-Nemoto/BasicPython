text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = text.replace(",", "").replace(".", "")
list_text = text.split()
L_int = list(map(len,list_text))
L = [str(A) for A in L_int]
L = "".join(L)
print(L)