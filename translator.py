def map_maker():
    input_map = {}
    with open("code_map.txt", "r") as f:
        for line in f.readlines():
            line = line.split()
            input_map[line[1]] = line[0]
    return input_map

tunic_map = map_maker()

def parse(input):
    if input in tunic_map.keys():
        return tunic_map[input]
    else:
        return "?"

while True:
    split_input = input().split(".")
    for a in split_input:
        print(parse(a), end="")
    print()

