import json
from vsdx import VisioFile

# Open the Visio file
filename = "C:\\Dev\\bachelor-thesis\\BR192_NetworkDiagram_v1.vsdx"
doc = VisioFile(filename)

# Loop through all the shapes in the file
ecus = []
buses = []

# Loop through all the shapes in the file
for page in doc.pages:
    for shape in page.child_shapes:
        # Check if the shape is a box or a rounded box
        if shape.shape_type == "Box":
            # Check if the box has any Round cells
            if "Round" in shape.cells:
                # Add the box to the ECUs list
                ecus.append(shape)
        # Check if the shape is a line
        elif shape.shape_type == "Line":
            # Add the line to the Buses list
            buses.append(shape)


# Print the number of ECUs and Buses found
print(f"Found {len(ecus)} ECUs and {len(buses)} Buses.")

print(ecus)

