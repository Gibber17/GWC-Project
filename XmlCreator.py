import xml.etree.ElementTree as ET
import os

class XmlCreator:
    def __init__(self, file_name, root_name="Contacts"):
        self.file_name = file_name

        if os.path.exists(file_name):
            # Load existing XML
            self.tree = ET.parse(file_name)
            self.root = self.tree.getroot()
        else:
            # Create new XML
            self.root = ET.Element(root_name)
            self.tree = ET.ElementTree(self.root)

    def add_element(self, parent, tag, text=None, attributes=None):
        """Add a child element with optional text or attributes."""
        attributes = attributes or {}
        element = ET.SubElement(parent, tag, attrib=attributes)
        if text:
            element.text = text
        return element

    def write_to_xml(self, file_name=None):
        """Write XML to file."""
        file_name = file_name or self.file_name
        self.tree.write(file_name, encoding="utf-8", xml_declaration=True)

    @staticmethod
    def get_language_from_contact(contact_name):
        """Given bot_name (like 'French Bot'), return the language ('French')"""
        return contact_name.replace(" Bot", "")

    def language_exists_in_xml(language, xml_file="Contacts.xml"):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        return root.find(language) is not None

    @staticmethod
    def get_Messages(xml_file):
        """Read messages from XML file and return structured data."""
        lang_data = {}

        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for lang_el in root:
                language_name = lang_el.tag

                messages = {
                    "UserMessages": [],
                    "BotMessages": []
                }

                # Collect user messages
                for um in lang_el.findall("UserMessage"):
                    if um.text:
                        messages["UserMessages"].append(um.text.strip())

                # Collect bot messages
                for bm in lang_el.findall("BotMessage"):
                    if bm.text:
                        messages["BotMessages"].append(bm.text.strip())

                lang_data[language_name] = messages

        except FileNotFoundError:
            print(f"Error: The file '{xml_file}' was not found.")
        except ET.ParseError as e:
            print(f"Error parsing XML: {e}")

        return lang_data

    def add_user_message(self, language, message):
        tree = ET.parse(self.file_name)
        root = tree.getroot()

        lang_el = root.find(language)
        if lang_el is None:
            lang_el = ET.SubElement(root, language)

        msg_el = ET.SubElement(lang_el, "UserMessage")
        msg_el.text = message

        tree.write(self.file_name, encoding="utf-8", xml_declaration=True)
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
