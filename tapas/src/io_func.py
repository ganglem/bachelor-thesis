import glob
import json
import os
from tkinter.filedialog import askopenfilename
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
          "Tool for Automatic Attack Path Analysis in Automotive Architectures\n")


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
        #for file_path in file_paths:
            #print(f"Successfully saved file from file path: {file_path}")
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
            #print(f"Successfully loaded JSON file: {file_name}")
            return j
    except FileNotFoundError as e:
        raise FileNotFoundError(f'Error loading JSON file {file_name} : {e}')
    except json.decoder.JSONDecodeError as e:
        raise ValueError(f'Error decoding JSON file {file_name} : {e}')


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
        raise f'An error occurred: {e}'


def process_tables(table: dict):
    """
    Processes the feasibility table, shortest path table, and hops table.

    Args:
        table (dict): The dictionary containing the feasibility, shortest path, and hops tables

    Returns:
        (pd.DataFrame, pd.DataFrame, pd.DataFrame): A tuple of DataFrames for feasibility, shortest path, and hops tables
    """
    feasibility_table = table["feasibility"]
    path_table = table["shortest_path"]
    hops_table = table["hops"]

    feasibility_df = pd.DataFrame.from_dict(feasibility_table, orient="index").sort_index().T
    path_df = pd.DataFrame.from_dict(path_table, orient="index").sort_index().T
    hops_df = pd.DataFrame.from_dict(hops_table, orient="index").sort_index().T

    return feasibility_df, path_df, hops_df


def print_table(table: dict, architecture_name: str):
    """
    Prints the feasibility table and shortest path table of a dictionary of tables and the architecture name.

    Args:
        table (dict): The dictionary containing the feasibility, shortest path, and hops tables
        architecture_name (str): The name of the architecture
    """
    try:
        string = "Architecture: " + architecture_name
        print("\n" + string)

        feasibility_df, path_df, hops_df = process_tables(table)

        print(feasibility_df)

        for entry in path_df.columns:
            for target in path_df.index:
                hops = hops_df.loc[target, entry]
                path = path_df.loc[target, entry][1:]
                if not pd.isna(hops):
                    print(entry, "->", target, f": [{hops} hop(s)]", path)

    except KeyError as e:
        raise KeyError(f'KeyError: {e}')

    except Exception as e:
        raise Exception(f'An error occurred: {e}')


def export_to_excel(table: dict, architecture_name: str, total_evaluation: float):
    """
    Exports the feasibility table, shortest path table, and hops table to an Excel file in the "results" directory.

    Args:
        table (dict): The dictionary containing the feasibility, shortest path, and hops tables
        architecture_name (str): The name of the architecture and the file name
    """

    try:
        feasibility_df, path_df, hops_df = process_tables(table)

        metadata = {"ARCHITECTURE NAME": architecture_name, "TOTAL EVALUATION": total_evaluation}
        metadata_df = pd.DataFrame.from_dict(metadata, orient="index").sort_index().T

        os.makedirs("results", exist_ok=True)
        with pd.ExcelWriter(f'results/{architecture_name}.xlsx') as writer:

            print("Exporting to Excel...")

            metadata_df.to_excel(writer, sheet_name='Metadata', index=False)
            feasibility_df.to_excel(writer, sheet_name='Feasibility Table', index=True)
            path_df.to_excel(writer, sheet_name='Shortest Path', index=True)
            hops_df.to_excel(writer, sheet_name='Hops', index=True)

            print("Exported to Excel successfully!")

    except KeyError as e:
        print(f'KeyError: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')


def file_select():
    """
    This function opens a file dialog and returns the selected files

    Returns:
        A tuple containing the architecture, ecu and bus file names
    """

    arch_in = askopenfilename(filetypes = [("JSON files", "*.json")], title = "Select the architecture file")
    print("[INFO]", arch_in)

    ecu_in = askopenfilename(filetypes = [("JSON files", "*.json")], title = "Select the ecu file")
    print("[INFO]", ecu_in)

    bus_in = askopenfilename(filetypes = [("JSON files", "*.json")], title = "Select the bus file")
    print("[INFO]", bus_in)

    return arch_in, ecu_in, bus_in
