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
        contact_data = {}
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for contact_element in root.findall('contact'):
                name_element = contact_element.find('name')

                if name_element is not None:
                    contact_name = name_element.text
                    messages = []
                    messages_element = contact_element.find('messages')

                    if messages_element is not None:
                        for message_element in messages_element.findall('message'):
                            if message_element.text:
                                messages.append(message_element.text.strip())
                    contact_data[contact_name] = messages
        except FileNotFoundError:
            print(f"Error: The file '{xml_file}' was not found.")
        except ET.ParseError as e:
            print(f"Error parsing XML file: {e}")
        return contact_data

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