def map_maker():
    input_map = {}
    with open("code_map.txt", "r") as f:
        for line in f.readlines():
            line = line.split()
            input_map[line[1]] = line[0]
    return input_map

tunic_map = map_maker()

# parse tunic code into phonetic transcription
def parse(input: str) -> str:
    input = input.strip()
    if input in tunic_map.keys():
        return tunic_map[input]
    else:
        return "?"
    
# parse line of input (use "." as deliminator between each tunic character)
def parse_line(input: str) -> list[str]:
    word = []
    split_input: list[str] = input.split(".")
    for char in split_input:
        word.append(parse(char))
    return word
    
# parse file where each line is a tunic word
def parse_file(filename: str) -> list[list[str]]:
    with open(filename, "r") as f:
        return [parse_line(line) for line in f.readlines()]

# main repl
while True:
    words: list[list[str]] = []
    input_str = input()
    if ".txt" in input_str:
        words = parse_file(input_str)
    elif input_str in ["exit", "q", "quit"]:
        break
    else:
        words.append(parse_line(input_str))
    for word in words:
        for char in word:
            print(char, end="")
        print()
