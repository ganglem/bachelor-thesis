from functions import *
from io_func import *


def main():
    fext = "json"
    architectures = load_files("..\\graphs", fext)
    ecus = load_files("..\\ecus", fext)
    buses = load_files("..\\buses", fext)

    for architecture in architectures:
        for ecu in ecus:
            for bus in buses:
                architecture_name, architecture, ecus_config, buses_config = parse_files(architecture, ecu, bus)

                G, entry_ecus, target_ecus_names = generate_graph(architecture, ecus_config, buses_config)

                table = find_attack_path(G, entry_ecus, target_ecus_names)

                print_table(table, architecture_name)

                print_evaluation(table)

                save_graph(G)

                export_to_excel(table, architecture_name)


if __name__ == "__main__":
    print_tapas()
    main()
