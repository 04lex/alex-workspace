import xml.etree.ElementTree as ET 

# root element
root = ET.Element("filme")

# elemente film1
film1 = ET.Element("film")

nume1 = ET.Element("nume")
nume1.text = "Film 1"

an1 = ET.Element("an")
an1.text = "2022"

gen1 = ET.Element("gen")
gen1.text = "Comedie"

film1.append(nume1)
film1.append(an1)
film1.append(gen1)

# elemente film2
film2 = ET.Element("film")

nume2 = ET.Element("nume")
nume2.text = "Film 2"

an2 = ET.Element("an")
an2.text = "2001"

gen2 = ET.Element("gen")
gen2.text = "Actiune"

film2.append(nume2)
film2.append(an2)
film2.append(gen2)


# film -> root
root.append(film1)
root.append(film2)


# xml tree
tree = ET.ElementTree(root)

xml_string = ET.tostring(root, encoding="UTF-8")

print(xml_string.decode())
