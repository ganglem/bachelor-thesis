from functions import *
from io_func import *


def main():

    #architecture, ecu, bus = file_select()

    architecture = "C:\\Dev\\bachelor-thesis\\tapas\\graphspoc\\a.json"
    ecu = "C:\\Dev\\bachelor-thesis\\tapas\\ecuspoc\\ecusA.json"
    bus = "C:\\Dev\\bachelor-thesis\\tapas\\buses\\buses.json"

    print(architecture)

    architecture_name, architecture, ecus_config, buses_config = parse_files(architecture, ecu, bus)

    G, entry_ecus, target_ecus = generate_graph(architecture, ecus_config, buses_config)

    table = find_attack_path(G, entry_ecus, target_ecus)

    print_table(table, architecture_name)

    total_architecture_feasibility = apply_criteria(entry_ecus, target_ecus, table, architecture)

    export_to_excel(table, architecture_name, total_architecture_feasibility)


if __name__ == "__main__":
    print_tapas()
    main()
