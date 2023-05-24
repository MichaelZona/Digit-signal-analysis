import xml.dom.minidom as xm

dom = xm.parse("./new/data.xml")
root = dom.documentElement

print (root.nodeName)
print (root.nodeValue)
print (root.nodeType)
print (root.ELEMENT_NODE)