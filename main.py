import sys

default_map: dict[str, str] = {
    # Substituições de palavras ou abreviações
    "and": "&",
    "at": "@",
    "percent": "%",
    "number": "#",
    
    # Símbolos tipográficos e matemáticos
    "...": "…",
    "-->": "→",
    "<--": "←",
    "+-": "±",
    "1/2": "½",
    "1/4": "¼",
    "3/4": "¾",
    "x": "×",
    "->": "→",
    
    # Letras com acentos e modificadores
    "a^": "â",
    "e^": "ê",
    "i^": "î",
    "o^": "ô",
    "u^": "û",
    "c,": "ç",
    "n~": "ñ",
    "e:`": "ë",
    
    # Unidades e medidas
    "degree": "°",
    "ohm": "Ω",
    "micro": "µ",
    "+/-": "±",
    
    # Representações de letras antigas
    "ae": "æ",
    "oe": "œ",
    "AA": "Å",
    "aa": "å",
    "ss": "ß",
    
    # Setas e direções
    "<=>": "⇔",
    "=>": "⇒",
    "<=": "⇐",
    "v": "↓",
    "^": "↑",
    
    # Figuras e símbolos
    "smiley": "☺",
    "heart": "♥",
    "star": "★",
    "check": "✔",

    # Substituições de ligaduras
    "ae": "Æ",
    "oe": "Œ",
    "ss": "ß",
    "ffi": "ﬃ",
    "ffl": "ﬄ",
    "fi": "ﬁ",
    "fl": "ﬂ",
    "ff": "ﬀ",
    
    # Acentos e contrações
    "a'": "á",
    "e'": "é",
    "i'": "í",
    "o'": "ó",
    "u'": "ú",
    "n~": "ñ",
    
    # Representações de combinações em alfabetos antigos
    "th": "Þ",
    "dh": "Ð",
    "hv": "ƕ",
    
    # Símbolos matemáticos
    "sum": "∑",
    "sqrt": "√",
    "infinity": "∞",
}

def main():
    file, map_file = get_cli_options()
    text, map = perform_options(file, map_file, default_map)

    result = transform(text, map)
    print(result, end="")

# ---

def perform_options(file: str, map_file: str, default_map: dict[str, str]) -> (str, dict[str, str]):
    text: str = ""
    map: dict[str, str] = default_map

    if file == "":
        if sys.stdin.isatty():
            eprint("Empty stdin. Pipe some data into the program to use it properly.")
            sys.exit(1)
        
        text = get_stdin_text()
    else:
        try:
            with open(file) as f:
                for line in f.readlines():
                    text += line # can keep '\n'
        except Exception:
            eprint(f"File '{file}' doesn't exist.")
            sys.exit(1)

    # if it was "", it already has the correct value
    if map_file != "":
        try:
            with open(map_file) as f:
                map = {}

                for line in f.readlines():
                    tokens = line.split(" ")
                    
                    if len(tokens) != 2:
                        eprint("Malformed map file.")
                        sys.exit(1)

                    key, value = tokens

                    value = value.strip()
                    map[key] = value
        except Exception:
            eprint(f"Map file '{map_file}' doesn't exist.")
            sys.exit(1)


    return text, map

def get_cli_options() -> (str, str):
    file = ""
    map_file = ""

    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]

        if i == len(sys.argv) - 1:
            eprint(f"No arguments to '{arg}' specifier")
            sys.exit(1)

        if arg == "-i":
            file = sys.argv[i + 1]
            i += 1
        elif arg == "-m":
            map_file = sys.argv[i + 1]
            i += 1

        i += 1

    return file, map_file

def get_stdin_text() -> str:
    text = ""
    for line in sys.stdin:
        text += line

    return text

def transform(text: str, map: dict[str, str]) -> str:
    for key, value in map.items():
        text = text.replace(key, value)

    return text

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# ---

if __name__ == "__main__":
    main()

