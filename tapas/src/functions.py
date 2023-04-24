import networkx as nx

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

    #make lists unique
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

    ext_int = []

    for bus in architecture:
        if bus['type'] == 'wifi':
            ext_int.append(bus['ecus'])
        elif bus['type'] == 'gnss':
            ext_int.append( bus['ecus'])
        elif bus['type'] == 'bluetooth':
            ext_int.append(bus['ecus'])

    amt_interfaces = 0

    for i in ext_int:
        amt_interfaces += len(i)-1

    return amt_interfaces

def get_avg_ecus(architecture) -> int:

    """Retrieve the average amount of ecus on a bus in an architecture"""

    ecus_on_bus = []
    avg = 1

    for bus in architecture:
        ecus_on_bus.append((bus['ecus']))

    for bus in ecus_on_bus:
        avg += len(bus)

    avg = avg / len(ecus_on_bus)
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
        entry_point_name = entry_point["name"]
        table["feasibility"][entry_point_name] = {}
        table["shortest_path"][entry_point_name] = {}
        table["hops"][entry_point_name] = {}

        for target_ecu_name in target_ecus_names:
            feasibility = nx.bellman_ford_path_length(G, entry_point_name, target_ecu_name) + entry_point["feasibility"]
            shortest_path = nx.shortest_path(G, entry_point_name, target_ecu_name)
            table["feasibility"][entry_point_name][target_ecu_name] = feasibility
            table["shortest_path"][entry_point_name][target_ecu_name] = shortest_path
            table["hops"][entry_point_name][target_ecu_name] = max(len(shortest_path) - 2, 0)

    return table

def apply_criteria(entry_points: list, target_ecus_names: list, table: dict, architecture: dict) -> list:
    """
    Take each feasibility and sup it up for one path. then divide that result by the amount of hops.
    :param table:
    :return:
    """

    # total architecture feasibility
    architecture_feasibility = 0

    # total architecture hops
    total_hops = 0

    # average amount of ecus per bus
    isolation = get_avg_ecus(architecture)

    # amount of external interfaces
    interfaces = get_ext_int(architecture)

    # amount of total attack paths
    attack_paths = len(entry_points) * len(target_ecus_names)

    # debatable
    if "CGW" in architecture:
        cgw = 1
    else:
        cgw = 0.5


    for entry_ecu in entry_points:
        entry_ecu_name = entry_ecu["name"]
        for target_ecu_name in target_ecus_names:

            # get feasibility and hops for each path
            feasibility = table["feasibility"][entry_ecu_name][target_ecu_name]

            hops = table["hops"][entry_ecu_name][target_ecu_name]

            total_hops += hops

            hops = max(hops, 0.1)

            architecture_feasibility += feasibility*hops

    #try every combination and save
    feasibilities = []

    for weight_cgw in range (0,2):
        for  weight_attack in range (0,2):
            for weight_interfaces in range (0,2):
                for  weight_isolation in range (0,2):
                    for weight_hops in range (0,2):
                        for weight_arch in range (1,2):

                            architecture_feasibility = (architecture_feasibility*weight_arch + total_hops*weight_hops + isolation*weight_isolation + interfaces*weight_interfaces + attack_paths*weight_attack + cgw*weight_cgw) / (weight_arch + weight_hops + weight_isolation + weight_interfaces + weight_attack + weight_cgw)
                            architecture_feasibility = round(architecture_feasibility, 3)
                            feasibilities.append(architecture_feasibility)

    return feasibilities

# verbindungen und interfaces habe ich nicht in der survey berücksichtigt
# ergebnisse begründen
# LIN connected, targets, others
