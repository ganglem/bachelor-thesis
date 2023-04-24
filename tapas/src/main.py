from difflib import SequenceMatcher

from functions import *
from io_func import *
import Levenshtein as lev

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

        finals[architecture_name] = apply_criteria(entry_ecus, target_ecus_names, table, architecture)
        # save_graph(G)

        # export_to_excel(table, architecture_name)


    ranking = dict(sorted(finals.items(), key=lambda item: item[1], reverse=True))
    for key, value in ranking.items():
        print(key, value)

    survey_ranking = ["Architecture 3", "Architecture 8", "Architecture 6", "Architecture 10", "Architecture 2", "Architecture 1", "Architecture 5", "Architecture 7", "Architecture 9", "Architecture 4"]

    num_options = len(finals["Architecture 1"])  # assume all architectures have same number of options

    dist_cmp = {}

    for i in range(num_options):

        ranked_list_for_distance = []
        ranked_options = sorted(finals.items(), key=lambda item: item[1][i], reverse=True)

        print("Ranking for Option", i)
        for rank, (architecture, options) in enumerate(ranked_options):
            print(str(rank+1) + ". ", architecture + ":", options[i])
            ranked_list_for_distance.append(architecture)

        distance = lev.distance(survey_ranking, ranked_list_for_distance)
        dist_cmp[i] = round(distance,)


    #print sorted dist_cmp according to value
    print("Distance Comparison")
    for key, value in sorted(dist_cmp.items(), key=lambda item: item[1], reverse=True):
        print("Option", key, ":", value, "")




if __name__ == "__main__":
    print_tapas()
    main()
