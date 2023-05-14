import json
from vsdx import VisioFile

# Open the Visio file
filename = "C:\\bachelor-thesis\\BR192_NetworkDiagram_v1.vsdx"
doc = VisioFile(filename)

# Loop through all the shapes in the file
ecus = []
buses = []

with VisioFile(filename) as vis:
    page = vis.pages[0]
    shapes_with_red_label = page.find_shapes_by_property_label_value()
    ecus.append(shapes_with_red_label)

# Print the number of ECUs and Buses found
print(f"Found {len(ecus)} ECUs and {len(buses)} Buses.")

print(ecus)

