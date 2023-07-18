import xml.etree.ElementTree as ET

def validate_tag(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        expected_tag = ['style','office', 'config', 'draw', 'style:name' ]

        for tag in expected_tag:
            if root.find(tag) is None:
                missing_tag.append(tag)
                return False

        return True
    except ET.ParseError:
        return False


missing_tag = []
xml_file = "my-draw_EPC.xml"

if validate_tag(xml_file):
    print("All Tags")
else:
    print("Miss Some Tags")
    print(missing_tag)
