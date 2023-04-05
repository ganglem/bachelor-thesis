import filecmp
import json


def compare():
    ecu1 = "..\\ecus\\ecus123567.json"
    ecu4 = "..\\ecus\\ecus49.json"
    ecu8 = "..\\ecus\\ecus8.json"
    ecu10 = "..\\ecus\\ecus10.json"

    file_paths = [ecu1, ecu4, ecu8, ecu10]


    for i in range(len(file_paths)):
        for j in range(i+1, len(file_paths)):
            result = filecmp.cmp(file_paths[i], file_paths[j])
            if result:
                print(f"Files: {file_paths[i]} and {file_paths[j]} are the same")
                print("\n")