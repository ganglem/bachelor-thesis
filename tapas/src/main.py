from functions import *
from io_func import *


def main():

    architecture, ecu, bus = file_select()

    print(architecture)

    architecture_name, architecture, ecus_config, buses_config = parse_files(architecture, ecu, bus)

    G, entry_ecus, target_ecus_names = generate_graph(architecture, ecus_config, buses_config)

    table = find_attack_path(G, entry_ecus, target_ecus_names)

    print_table(table, architecture_name)

    architecture = apply_criteria(entry_ecus, target_ecus_names, table, architecture)


if __name__ == "__main__":
    print_tapas()
    main()
