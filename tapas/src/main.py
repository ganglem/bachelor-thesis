from functions import *
from io_func import *


def main():

    #arch_number = int(input('How many architectures are there gonna be?: >'))
    bus = "..\\buses\\buses.json"

    config = {'..\\graphs\\Architecture1.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture2.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture3.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture4.json': '..\\ecus\\ecus49.json',
            '..\\graphs\\Architecture5.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture6.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture7.json': '..\\ecus\\ecus123567.json',
            '..\\graphs\\Architecture8.json': '..\\ecus\\ecus8.json',
            '..\\graphs\\Architecture9.json': '..\\ecus\\ecus9.json',
            '..\\graphs\\Architecture10.json': '..\\ecus\\ecus10.json',
            }

    finals = {}

    for architecture, ecu in config.items():

        print(architecture)
        #architecture = input('Select architecture file path: > ')
        #ecu = input('Select ECU config file path: > ')

        architecture_name, architecture, ecus_config, buses_config = parse_files(architecture, ecu, bus)

        G, entry_ecus, target_ecus_names = generate_graph(architecture, ecus_config, buses_config)

        table = find_attack_path(G, entry_ecus, target_ecus_names)

        print_table(table, architecture_name)

        finals[architecture_name] = table_evaluation(entry_ecus, target_ecus_names, table)

        #save_graph(G)

        #export_to_excel(table, architecture_name)

    ranking = dict(sorted(finals.items(), key=lambda item: item[1], reverse=True))

    print('Ranking: ')
    for key, value in ranking.items():
        print(key, value)


if __name__ == "__main__":
    print_tapas()
    main()
