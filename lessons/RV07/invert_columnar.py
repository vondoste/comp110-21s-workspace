from exercises.ex04.data_utils import columnar

def invert_columnar(table: dict[str, list[str]]) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for i in range(len(table.values())):
        member: dict[str,str] = {}
        for key in table:
            member[key] = table[key][i]
        result.append(member)
    return result


def main() -> None:
    list_dicts = [{'breed': 'pug', 'color': 'brown', 'name': 'Kris'},
                  {'breed': 'corgi', 'color': 'blue', 'name': 'Kaki'},
                  {'breed': 'beagle', 'color': 'pink', 'name': 'Mark'}]
    expected = {'breed': ['pug', 'corgi', 'beagle'], 
                'color': ['brown', 'blue', 'pink'],
                'name': ['Kris', 'Kaki', 'Mark']}
    print(list_dicts)
    print(columnar(list_dicts))
    print(expected)
    print(invert_columnar(expected))

# list of lists examples
pair_1: list[str] = ['Kaki', 'Will']
pair_2: list[str] = ['Marc', 'Marley']
pair_3: list[str] = ['Kris', 'San']

matchings: list[list[str]] = [pair_1, pair_2, pair_3]

print(matchings[0])
print(matchings[0][0] + ' - ' + matchings[1][1])

# lists of lists all in one
matchings: list[list[str]] = [['Kaki', 'Will'], ['Marc', 'Marley'], ['Kris', 'San']]
print(matchings[0])
print(matchings[0][0] + ' - ' + matchings[1][1])

# dictionary of dictionaries example
nested_dict: dict[int, dict[str, str]] = {1: {'A': 'UNC', 'B': 'ECU'}, 2: {'C': 'DUKE', 'D': 'APP'}}

# Add one element
nested_dict[2]['E'] = "UNCW"

# Add whole dictionary
nested_dict[3] = {'F': 'ELON', 'G': 'UNCG'}

print(nested_dict)


if __name__ == "__main__":
    main()

        
