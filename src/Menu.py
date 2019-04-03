from lxml import etree

class MenuList():
    def __init__(self):
        super().__init__()
        self.menuXML = '../docs/menu.xml'
        try:
            self.root = etree.parse(self.menuXML).getroot()
        except:
            self.__initList()
            print('no menu was found, an empty menu is created')


    def __initList(self):
        self.root = etree.Element("menu")
        tree = etree.ElementTree(self.root)
        tree.write(self.menuXML, xml_declaration=True, encoding='utf-8')


    def printMenu(self):
        for sort in self.root.findall("sort"):
            print(sort.attrib['name'])
            for dish in sort.findall("dish"):
                print(' |-->', dish.attrib['name'])


    def insert(self, name, sort, ingrediants):
        dishSort = self.root.find("sort[@name='" + sort + "']")
        if dishSort is None:
            dishSort = etree.SubElement(self.root, 'sort', name=sort)

        dish = etree.SubElement(dishSort, 'dish', name=name)
        for k, v in ingrediants.items():
            temp = etree.SubElement(dish, "ingrediant", name=k)
            temp.text = v

        tree = etree.ElementTree(self.root)
        tree.write(self.menuXML, xml_declaration=True, encoding='utf-8')


if __name__ == '__main__':
    menu = MenuList()
    menu.printMenu()
    # name = '测试'
    # sort = '种类2'
    # ingrediants = {'原料1':'1', '原料2':'1'}
    # menu.insert(name, sort, ingrediants)
