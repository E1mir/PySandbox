import xml.sax


class XMLHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.model = ""
        self.speed = ""
        super().__init__()

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "car":
            print("---CAR---")
            name = attributes["name"]
            print("Name:", name)

    def endElement(self, tag):
        if self.current_data == "model":
            print("Model:", self.model)
        elif self.current_data == "speed":
            print("Speed:", self.speed)
        self.current_data = ""

    def characters(self, content):
        if self.current_data == "model":
            self.model = content
        elif self.current_data == "speed":
            self.speed = content


if __name__ == '__main__':
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    Handler = XMLHandler()
    parser.setContentHandler(Handler)

    parser.parse("xml_data.xml")
