import json
import os
import glob
from typing import Tuple

import networkx as nx
import pandas as pd
from matplotlib import pyplot as plt


def print_tapas():
    print("                         Welcome to\n"
          "                    ╔════╦═══╦═══╦═══╦═══╗\n"
          "                    ║╔╗╔╗║╔═╗║╔═╗║╔═╗║╔═╗║\n"
          "                    ╚╝║║╚╣╚═╝║╚═╝║╚═╝║╚══╗\n"
          "                      ║║ ║╔═╗║╔══╣╔═╗╠══╗║\n"
          "                      ║║ ║║ ║║║  ║║ ║║╚═╝║\n"
          "                      ╚╝ ╚╝ ╚╩╝  ╚╝ ╚╩═══╝\n"
          "Tool for Automatic Path Analysis in Automotive Architectures\n")


def parse_files(architecture_file: str, ecu_file: str, bus_file: str) -> Tuple[str, dict, dict, dict]:
    """
    This function takes three file names, loads their JSON contents, and returns the architecture name, architecture, ecus_config and buses_config as tuple
    Parameters:
        architecture_file: The name of the architecture file
        ecu_file: The name of the ecu file
        bus_file: The name of the bus file
    Returns:
        A tuple containing the architecture name, architecture, ecus_config and buses_config
    Raises:
        FileNotFoundError: If any of the files is not found
    """
    try:
        architecture_name = load_json(architecture_file)["a_name"]
        architecture = load_json(architecture_file)["buses"]
        ecus_config = load_json(ecu_file)["ecus"]
        buses_config = load_json(bus_file)["buses"]
        return architecture_name, architecture, ecus_config, buses_config
    except KeyError as e:
        raise ValueError(f'Error parsing JSON file, {e}')


def load_files(folder_path: str, file_extension: str) -> list:
    """
    This function takes a folder path and file extension and returns all file paths with the given extension in the folder.
    If the folder path is invalid, the function raises a FileNotFoundError.
    Parameters:
        folder_path (str): The path of the folder where the files are located
    Raises:
        FileNotFoundError: If folder path is not provided or invalid
    Returns:
        A list of file paths
    """
    while True:
        if not folder_path:
            raise FileNotFoundError("Folder path is not provided.")

        # check if the folder exists
        if not os.path.exists(folder_path):
            raise FileNotFoundError("Invalid path, please try again.")

        # save the file paths in a list
        file_paths = glob.glob(os.path.join(folder_path, f"*.{file_extension}"))
        for file_path in file_paths:
            print(f"Successfully saved file from file path: {file_path}")
        break

    return file_paths


def load_json(file_name: str) -> dict:
    """
    Returns a dictionary of its JSON contents from file name.

    Args:
        file_name: The name of the file to be loaded
    Returns:
        A dictionary containing the JSON contents of the file
    Raises:
        FileNotFoundError: If file is not found

    """
    try:
        with open(file_name) as json_file:
            j = json.load(json_file)
            print(f"Successfully loaded JSON file: {file_name}")
            return j
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Error loading JSON file {file_name} : {e}')
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f'Error decoding JSON file {file_name} : {e}')


def print_table(table: dict, architecture_name: str):
    """
    prints the distance table and shortest path table of dictionary of tables and the architecture name.

    Args:
        table (dict): The dictionary containing the distance and shortest path tables
        architecture_name (str): The name of the architecture
    """
    try:
        string = "Architecture: "+architecture_name
        print("\n"+string)

        distance_table = table["distance"]
        path_table = table["shortest_path"]

        print(pd.DataFrame.from_dict(distance_table, orient = "index").sort_index())

        for entry in path_table:
            for target in path_table[entry]:
                print("Shortest path from "+entry+" to "+target+":"+str(path_table[entry][target]))
    except KeyError as e:
        print(f'KeyError: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')



def save_graph(G: nx.DiGraph):
    """
    Saves directed graph `G` and as a png image.

    Args:
         G: a directed graph of type `nx.DiGraph`
    """
    try:
        f = plt.figure()
        f.tight_layout()
        nx.draw(G, ax = f.add_subplot(), with_labels = True, node_size = 200, node_color = "skyblue", node_shape = "s")
        f.savefig("graph.png")
    except Exception as e:
        print(f'An error occurred: {e}')

