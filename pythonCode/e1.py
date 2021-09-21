import xml.etree.ElementTree as ET
mytree = ET.parse('example.xml')
myroot = mytree.getroot()

for prices in myroot.iter('price'):
    prices.text = str(float(prices.text)+10)
    prices.set('newprices','yes')

ET.SubElement(myroot[0],"tasty")
for temp in myroot.iter('tasty'):
    temp.text = str("yes")
mytree.write("modified.xml")
