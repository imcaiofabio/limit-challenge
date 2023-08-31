from xml.etree import ElementTree


def convert_file(xml_file):
    try:
        tree = ElementTree.parse(xml_file)
        root = tree.getroot()

        def xml_to_dict(element):
            result = {}

            if len(element) == 0 and not element.text:
                return ""

            for child in element:
                child_data = xml_to_dict(child)
                if child_data is not None:
                    if child.tag in result:
                        if type(result[child.tag]) is list:
                            result[child.tag].append(child_data)
                        else:
                            result[child.tag] = [result[child.tag], child_data]
                    else:
                        result[child.tag] = child_data
                elif child.text:
                    result[child.tag] = child.text

            return result if result else element.text

        if len(root) < 2:
            json_data = {root.tag: xml_to_dict(root)}
        else:
            json_data = {root.tag: []}
            for child in root:
                json_data[root.tag].append({child.tag: [xml_to_dict(child)]})

        return json_data

    except Exception as e:
        return str(e)
