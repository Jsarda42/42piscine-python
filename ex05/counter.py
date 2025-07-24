import string
def counter(text : str):
    total = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())

    print(f"The text contains {total} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")

