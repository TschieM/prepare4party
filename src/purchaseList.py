from lxml import etree
import os

class PurchaseList():
    def __init__(self, date):
        super().__init__()
        self.date = date
        self.cookXML = '../docs/' + self.date + '/cookList.xml'
        self.buyTXT = '../docs/' + self.date + '/purchaseList.txt'
        os.makedirs(os.path.dirname(self.cookXML), exist_ok=True)
        try:
            self.cookList = etree.parse(self.cookXML).getroot()
        except:
            print("Please create a cook list first")


    def printList(self, cnt=1):
        pList = self.generateList()
        file = open(self.buyTXT, "w")
        file.write("********************************" + '\n')
        file.write("Purchase List for Date " + self.date + '\n')
        file.write("********************************" + '\n\n')
        for k, v in pList.items():
            file.write('%-2s %0s %2s %2s\n' % (str(cnt), '-', k, str(v)))
            cnt += 1
        file.close()



    def generateList(self):
        pList = {}
        for i in self.cookList.findall("./sort/dish/ingrediant"):
            k = i.attrib['name']
            v = int(i.text)
            if k in pList:
                pList[k] += v
            else:
                pList[k] = v
        return pList


if __name__ == '__main__':
    pList = PurchaseList("2019-04-03")
    pList.printList()
