import json
from vsdx import VisioFile
import xml.etree.ElementTree as ET

def parse_visio():
    # Open the Visio file
    #filename = "C:\\Dev\\bachelor-thesis\\BR192_NetworkDiagram_v1.vsdx"
    filename = "tapas/visio/visio/pages/page1.xml"

    # Load the XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Define the XML namespace
    ns = {'v': 'http://schemas.microsoft.com/office/visio/2012/main'}

    # Iterate over all Shape elements
    for shape in root.findall('v:Shapes/v:Shape', ns):
        # Extract the ID and Type attributes
        shape_id = shape.get('ID')
        shape_type = shape.get('Type')
        print(f'Shape ID: {shape_id}, Type: {shape_type}')

        # Extract the values of selected cells
        for cell in shape.findall('v:Cell[@N="PinX" or @N="PinY" or @N="Width" or @N="Height"]', ns):
            cell_name = cell.get('N')
            cell_value = cell.get('V')
            print(f'  {cell_name}: {cell_value}')

        # Extract the text content
        text = shape.find('v:Text', ns).text.strip()
        print(f'  Text: {text}\n')
