from lxml import etree
import os

class CookList():
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.cookXML = '../docs/' + self.date + '/cookList.xml'
        self.cookTXT = '../docs/' + self.date + '/cookList.txt'
        os.makedirs(os.path.dirname(self.cookXML), exist_ok=True)
        try:
            self.cookList = etree.parse(self.cookXML).getroot()
        except:
            self.__initCookList()
        self.menuXML = '../docs/menu.xml'
        try:
            self.menu = etree.parse(self.menuXML).getroot()
        except:
            print('no menu was found')


    def __initCookList(self):
        self.cookList = etree.Element("cookList")
        tree = etree.ElementTree(self.cookList)
        tree.write(self.cookXML, xml_declaration=True, encoding='utf-8')


    def printCookList(self, cnt=1):
        file = open(self.cookTXT, "w")
        file.write("*****************************" + '\n')
        file.write("Cook List for Date " + self.date + '\n')
        file.write("*****************************" + '\n\n')
        for cs in self.cookList.findall("sort"):
            file.write(cs.attrib['name'] + '\n')
            file.write("----------------------" + '\n')
            for cd in cs.findall("dish"):
                file.write(str(cnt) + " - " + cd.attrib['name'] + '\n')
                cnt += 1
            file.write("----------------------" + '\n')
        file.close()


    def selectDish(self, name):
        dm = self.findDish(name, self.menu)
        if dm[0] is None:
            print("so sad, desired dish is currently not servable :(")
        else:
            dc = self.findDish(name, self.cookList)
            if dc[0] is None:
                self.insertDish(name, dm[0], dm[1])
            else:
                print(name + " already selected")


    def findDish(self, name, root):
        sort = None
        ing = {}
        for s in root.findall("sort"):
            for d in s.findall("dish"):
                if d.attrib['name'] == name:
                    sort = s.attrib['name']
                    for i in d.findall("ingrediant"):
                        ing.update({i.attrib['name']: i.text})
        return [sort, ing]


    def insertDish(self, name, sort, ingrediants):
        dishSort = self.cookList.find("sort[@name='" + sort + "']")
        if dishSort is None:
            dishSort = etree.SubElement(self.cookList, 'sort', name=sort)
        dish = etree.SubElement(dishSort, 'dish', name=name)
        for k, v in ingrediants.items():
            temp = etree.SubElement(dish, "ingrediant", name=k)
            temp.text = v
        tree = etree.ElementTree(self.cookList)
        tree.write(self.cookXML, xml_declaration=True, encoding='utf-8')



if __name__ == '__main__':
    cookList = CookList("2019-04-03")
    cookList.selectDish("测试")
    # cookList.printCookList()
