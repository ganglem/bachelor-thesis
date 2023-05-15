from difflib import SequenceMatcher

from functions import *
from io_func import *


def main():

    bus = "..\\buses\\buses.json"

    config1 = {'..\\graphs\\Architecture1.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture2.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture3.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture4.json': '..\\ecus\\ecus49.json',
            '..\\graphs\\Architecture5.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture6.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture7.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture8.json': '..\\ecus\\ecus8.json',
            '..\\graphs\\Architecture9.json': '..\\ecus\\ecus9.json',
            '..\\graphs\\Architecture10.json': '..\\ecus\\ecus10.json'
            }

    config2 = {'..\\graphspoc\\a.json': '..\\ecuspoc\\ecusA.json',
               '..\\graphspoc\\b.json': '..\\ecuspoc\\ecusB.json',
               '..\\graphspoc\\c.json': '..\\ecuspoc\\ecusC.json'}

    finals = {}

    for architecture, ecu in config2.items():

        print(architecture)

        architecture_name, architecture, ecus_config, buses_config = parse_files(architecture, ecu, bus)

        G, entry_ecus, target_ecus_names = generate_graph(architecture, ecus_config, buses_config)

        table = find_attack_path(G, entry_ecus, target_ecus_names)

        print_table(table, architecture_name)

        finals[architecture_name], weights = apply_criteria(entry_ecus, target_ecus_names, table, architecture)

    get_criteria(finals, weights)

if __name__ == "__main__":
    print_tapas()
    main()
