import networkx as nx
import Levenshtein as lev


def generate_graph(architecture, ecus_config, buses_config):
    entry_points = []
    target_ecus = []
    G = nx.DiGraph()
    ecus_config_dict = {item['name']: item for item in ecus_config}
    buses_config_dict = {item['type']: item for item in buses_config}

    # go through graph
    for current_bus in architecture:
        ecu_types = {}

        # get current bus type
        bus_type = get_attribute(current_bus, "type")

        # get current bus feasibility
        bus_feasibility = get_attribute(buses_config_dict[bus_type], "feasibility")

        # get list of ecus on current bus
        ecus_on_current_bus = get_attribute(current_bus, "ecus")
        for ecu in ecus_on_current_bus:
            ecu_config = get_attribute(ecus_config_dict, ecu)
            ecu_type = get_attribute(ecu_config, "type")
            ecu_feasibility = get_attribute(ecu_config, "feasibility")

            ecu_types.setdefault(ecu_type, []).append(ecu)

            if ecu_type == "entry" or ecu_type == "both" or ecu_type == "interface":
                entry_points.append({"name": ecu, "feasibility": ecu_feasibility})
            if ecu_type == "target" or ecu_type == "both":
                target_ecus.append(ecu)

        for ecu in ecus_on_current_bus:
            for target_ecu in ecus_on_current_bus:
                if target_ecu == ecu:
                    continue
                target_ecu_config = get_attribute(ecus_config_dict, target_ecu)
                target_ecu_config_type = get_attribute(target_ecu_config, "type")
                if target_ecu_config_type == "interface":
                    if ecu in entry_points or target_ecu in entry_points:
                        feasibility = bus_feasibility
                        G.add_edge(u_of_edge=target_ecu_config_type, v_of_edge=target_ecu, weight=feasibility)
                elif target_ecu_config_type != "interface":
                    target_ecu_feasibility = get_attribute(target_ecu_config, "feasibility")
                    feasibility = bus_feasibility + target_ecu_feasibility
                    G.add_edge(u_of_edge=ecu, v_of_edge=target_ecu, weight=feasibility)

    # make lists unique
    entry_points = [dict(t) for t in {tuple(d.items()) for d in entry_points}]
    target_ecus = list(set(target_ecus))

    return G, entry_points, target_ecus


def get_config(obj: str, objects_config: list, object_param: str, query: str) -> any:
    """Retrieve the value of query parameter for the object configuration that matches the object parameter.

    Args:
        obj: The object for which to retrieve the configuration.
        objects_config: A list of dictionaries representing the configurations for multiple objects.
        object_param: The key of the dictionary representing the object parameter to match against.
        query: The key of the dictionary representing the query parameter to retrieve.

    Returns:
        The value of the query parameter for the object configuration that matches the object parameter.

    Raises:
        ValueError: If the object does not exist in the config list.
    """
    for item in objects_config:
        if item.get(object_param) == obj:
            return item.get(query)
    raise ValueError(f'Object {obj} does not exist in the config list')


def get_attribute(obj: any, attribute: any) -> any:
    """
    Retrieves the value of an attribute for a given object.

    Args:
        obj (Any): The object to access the attribute from.
        attribute (Any): The name or key of the attribute to access.

    Returns:
        Any: The value of the attribute for the object.

    Raises:
        ValueError: If the attribute is not found in the object or is not accessible.
    """
    try:
        return obj[attribute]
    except (KeyError, TypeError):
        raise ValueError(f"attribute: {attribute} not found in object or not accessible")


def get_ext_int(architecture: dict) -> int:
    """Retrieve amount of ecus on interface bus"""

    prep_arch = []
    prep_interfaces = []
    total_amount = 0

    for bus in architecture:
        if bus['type'] == 'wifi':
            prep_arch.append(bus['ecus'])
        elif bus['type'] == 'gnss':
            prep_arch.append(bus['ecus'])
        elif bus['type'] == 'bluetooth':
            prep_arch.append(bus['ecus'])

    for sub in prep_arch:
        prep_interfaces.append(sub[1:])

    #print("[DEBUG] PREP INTERFACES:", prep_interfaces)
    for sub in prep_interfaces:
        total_amount += len(sub)

    prep_set = [item for sublist in prep_interfaces for item in sublist]
    interfaces_set = set(prep_set)
    print("[DEBUG] INTERFACES SET:", interfaces_set)
    avg_interfaces = len(interfaces_set)

    print("[DEBUG] TOTAL AMOUNT", total_amount)
    return total_amount, prep_arch, avg_interfaces


def get_avg_ecus(architecture) -> int:
    """Retrieve the average amount of ecus on a bus in an architecture"""

    buses = []
    ecus = 0

    for bus in architecture:
        if bus["name"] == "wifi" or bus["name"] == "bluetooth" or bus["name"] == "gnss":
            continue
        else:
            buses.append((bus['ecus']))

    for bus in buses:
        if "wifi" in bus or "bluetooth" in bus or "gnss" in bus:
            ecus += len(bus)-1
        else:
            ecus += len(bus)

    #print("[DEBUG] ECUS:", ecus)
    #print("[DEBUG] BUSES:", len(buses))

    avg = ecus/len(buses)

    print("[DEBUG] ISOLATION:", avg)
    return round(avg)


def find_attack_path(G: nx.DiGraph, entry_points: list, target_ecus_names: list) -> dict:
    """
    Finds the feasibility and shortest path from each entry ecu to each target ecu in a graph.

    Args:
        G: A NetworkX graph representing the system architecture.
        entry_points: A list of dictionaries representing the entry points.
        target_ecus_names: A list of strings representing the target ECUs.

    Returns:
        A table containing the feasibility and shortest path from each entry ECU to each target ECU.
    """
    table = {"feasibility": {}, "shortest_path": {}, "hops": {}}

    for entry_point in entry_points:
        entry_point_name = get_attribute(entry_point, "name")
        table["feasibility"][entry_point_name] = {}
        table["shortest_path"][entry_point_name] = {}
        table["hops"][entry_point_name] = {}

        for target_ecu_name in target_ecus_names:
            feasibility = nx.bellman_ford_path_length(G, entry_point_name, target_ecu_name) + entry_point["feasibility"]
            shortest_path = nx.shortest_path(G, entry_point_name, target_ecu_name, method='bellman-ford')
            table["feasibility"][entry_point_name][target_ecu_name] = feasibility
            table["shortest_path"][entry_point_name][target_ecu_name] = shortest_path
            table["hops"][entry_point_name][target_ecu_name] = max(len(shortest_path) - 2, 0)

    return table


def apply_criteria(entry_points: list, target_ecus_names: list, table: dict, architecture: dict):

    # total architecture feasibility
    architecture_feasibility = 0

    # total architecture hops
    total_hops = 0

    # average amount of ecus per bus
    isolation = get_avg_ecus(architecture)

    # interfaces
    amt_interfaces, interfaces, abs_interfaces = get_ext_int(architecture)


    print("[DEBUG] NO INTERFACES:", abs_interfaces)

    cgw_count = 0

    # debatable
    cgw = 1
    if "CGW" not in architecture:
        cgw -= 0.15

    for interface in interfaces:
        if cgw_count == 0:
            if "CGW" in interface:
                cgw -= 0.1
                cgw_count = 1

    if "CGW" in target_ecus_names:
        cgw -= 0.05

    print("[DEBUG] CGW:", cgw)

    for entry_ecu in entry_points:
        entry_ecu_name = entry_ecu["name"]
        for target_ecu_name in target_ecus_names:
            # get feasibility and hops for each path
            feasibility = table["feasibility"][entry_ecu_name][target_ecu_name]

            hops = table["hops"][entry_ecu_name][target_ecu_name]

            total_hops += hops

            architecture_feasibility += feasibility * hops

    # save the original value of architecture_feasibility
    original_architecture_feasibility = architecture_feasibility

    # try every combination and save

    feasibilities = []
    weights = []

    w1 = 1
    w2 = 4
    w3 = 32

    numerator = (100 * (original_architecture_feasibility * cgw))
    denominator = (total_hops * w1 + (isolation ** w2) + abs_interfaces * w3)

    total_architecture_feasibility = round(numerator / denominator, 2)

    print("[DEBUG] TOTAL HOPS:", total_hops)

    print("\nTOTAL ARCHITECTURE EVALUATION:", total_architecture_feasibility)
    return total_architecture_feasibility


def get_criteria(finals, weights):
    ranking = dict(sorted(finals.items(), key=lambda item: item[1], reverse=True))

    #output_file = "../data/highw3.txt"

    #with open(output_file, 'w') as f:

    survey_ranking = ["Architecture 3", "Architecture 8", "Architecture 6", "Architecture 10", "Architecture 2",
                      "Architecture 1", "Architecture 5", "Architecture 7", "Architecture 9", "Architecture 4"]
    num_options = len(finals["Architecture A"])  # assume all architectures have same number of options
    dist_cmp = {}

    for i in range(num_options):

        ranked_list_for_distance = []
        ranked_options = sorted(finals.items(), key=lambda item: item[1][i], reverse=True)

        #f.write(f"\nRanking for Option {i}\n")
        #f.write(f"Weights: {weights[i]}\n")
        print(f"\nRanking for Option {i}\n")
        print(f"Weights: {weights[i]}\n")

        for rank, (architecture, options) in enumerate(ranked_options):
            #f.write(f"{str(rank + 1)}. {architecture}: {options[i]}\n")
            print(f"{str(rank + 1)}. {architecture}: {options[i]}\n")
            ranked_list_for_distance.append(architecture)

        distance = lev.distance(survey_ranking, ranked_list_for_distance)
        dist_cmp[i] = round(distance, )

    #for key, value in sorted(dist_cmp.items(), key=lambda item: item[1], reverse=True):
        #f.write(f"Option {key}: {value}\n")
        #print(f"Option {key}: {value}\n")

    #print(f"Results written to {os.path.abspath(output_file)}")
