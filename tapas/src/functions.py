import networkx as nx


def generate_graph(architecture, ecus_config, buses_config):
    entry_ecus = []
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
                entry_ecus.append({"name": ecu, "feasibility": ecu_feasibility})
            if ecu_type == "target" or ecu_type == "both":
                target_ecus.append(ecu)

        for ecu in ecus_on_current_bus:
            for target_ecu in ecus_on_current_bus:
                if target_ecu == ecu:
                    continue
                target_ecu_config = get_attribute(ecus_config_dict, target_ecu)
                target_ecu_config_type = get_attribute(target_ecu_config, "type")
                if target_ecu_config_type == "interface":
                    if ecu in entry_ecus or target_ecu in entry_ecus:
                        feasibility = bus_feasibility
                        G.add_edge(u_of_edge=target_ecu_config_type, v_of_edge=target_ecu, weight=feasibility)
                elif target_ecu_config_type != "interface":
                    target_ecu_feasibility = get_attribute(target_ecu_config, "feasibility")
                    feasibility = bus_feasibility + target_ecu_feasibility
                    G.add_edge(u_of_edge=ecu, v_of_edge=target_ecu, weight=feasibility)

    return G, entry_ecus, target_ecus


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


def find_attack_path(G: nx.DiGraph, entry_ecus: list, target_ecus_names: list) -> dict:
    """
    Finds the distance and shortest path from each entry ecu to each target ecu in a graph.

    Args:
        G: A NetworkX graph representing the system architecture.
        entry_ecus: A list of dictionaries representing the entry ECUs.
        target_ecus_names: A list of strings representing the target ECUs.

    Returns:
        A table containing the distance and shortest path from each entry ECU to each target ECU.
    """
    table = {"distance": {}, "shortest_path": {}, "hops": {}}

    for entry_ecu in entry_ecus:
        entry_ecu_name = entry_ecu["name"]
        table["distance"][entry_ecu_name] = {}
        table["shortest_path"][entry_ecu_name] = {}
        table["hops"][entry_ecu_name] = {}

        for target_ecu_name in target_ecus_names:
            distance = nx.bellman_ford_path_length(G, entry_ecu_name, target_ecu_name) + entry_ecu["feasibility"]
            shortest_path = nx.shortest_path(G, entry_ecu_name, target_ecu_name)
            table["distance"][entry_ecu_name][target_ecu_name] = distance
            table["shortest_path"][entry_ecu_name][target_ecu_name] = shortest_path
            table["hops"][entry_ecu_name][target_ecu_name] = max(len(shortest_path) - 2, 1)

    return table


def table_evaluation(entry_ecus: list, target_ecus_names: list, table: dict):
    """
    Take each distance and sup it up for one path. then divide that result by the amount of hops.
    :param table:
    :return:
    """
    total = 0
    total_hops = 0

    for entry_ecu in entry_ecus:
        entry_ecu_name = entry_ecu["name"]
        for target_ecu_name in target_ecus_names:
            distance = table["distance"][entry_ecu_name][target_ecu_name]
            hops = table["hops"][entry_ecu_name][target_ecu_name]
            distance = distance / hops
            total += distance

    print("The feasibility of this architecture is: ", round(total))
    print()

    return round(total)