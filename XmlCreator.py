import xml.etree.ElementTree as ET
import os
from fileinput import filename


# Create root element
class XmlCreator:
    def __init__(self, file_name, root_name="Contacts"):
        self.file_name = file_name

        if os.path.exists(file_name):
            # Load existing XML file
            tree = ET.parse(file_name)
            self.root = tree.getroot()
        else:
            # Create new XML file
            self.root = ET.Element(root_name)

    def add_element(self, parent, tag, text=None, attributes=None):
        # Add a child element to the specified parent
        attributes = attributes or {}
        element = ET.SubElement(parent, tag, attrib=attributes)
        if text:
            element.text = text
        return element

    def write_to_xml(self, file_name):
        # Write to file
        tree = ET.ElementTree(self.root)
        with open(file_name, "wb") as file:
            tree.write(file, encoding="utf-8", xml_declaration=True)

    def get_Messages(xml_file):
        lang_data = {}

        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            # Loop through each language tag
            for lang_el in root:
                language_name = lang_el.tag
                messages = {
                    "UserMessages": [],
                    "BotMessages": []
                }

                # Get all <UserMessage>
                for um in lang_el.findall("UserMessage"):
                    if um.text:
                        messages["UserMessages"].append(um.text.strip())

                # Get all <BotMessage>
                for bm in lang_el.findall("BotMessage"):
                    if bm.text:
                        messages["BotMessages"].append(bm.text.strip())

                lang_data[language_name] = messages

        except FileNotFoundError:
            print(f"Error: The file '{xml_file}' was not found.")
        except ET.ParseError as e:
            print(f"Error parsing XML file: {e}")

        return lang_data

'''
example of how to create the xml file and add information to it

def main():
    xml_creator = XmlCreator("Contacts")
    contact1 = xml_creator.add_element(xml_creator.root, "French")
    xml_creator.add_element(contact1, "UserMessages", text="Bonjour")
    xml_creator.add_element(contact1, "BotMessages", text="Oui, Bonjour")
    xml_creator.write_to_xml("Contacts.xml")

if __name__ == "__main__":
    main()

'''
