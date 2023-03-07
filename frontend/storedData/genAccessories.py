from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD
from rdflib import Namespace
from rdflib.plugins import sparql
g = Graph()

# donna = URIRef("http://example.org/donna")

s = Namespace("https://schema.org/")

popularCategory = URIRef("https://schema.org/category/popular")
includes = URIRef("http://purl.org/goodrelations/v1#includes")
category = Namespace("https://schema.org/category/")
product = Namespace("https://schema.org/Product/")



# add accessories products to turtle
accessories_prd1 = product.accessories_prd1
g.add((accessories_prd1, s.identifier, Literal("accessories_prd1")))
g.add((accessories_prd1, s.title, Literal("Icts Thin Client Fl-100")))
g.add((accessories_prd1, s.price, Literal("$1189.00")))
g.add((accessories_prd1, s.caption, Literal("Rugged, fanless, solid steel build to survive high heat, dust and harsh working conditions.Linux based Thin Client OS - developed by ICTS as per the requirements of Indian customers. OS supported with Linux / Windows XP / Windows 7 .DDR3 512 MB memory and 4 GB NAND flash soldered onboard .Dual Mode Display HDMI/VGA.")))
g.add((accessories_prd1, s.description, Literal("""This powerful, low cost, low maintenance and a rugged thin client are designed and manufactured in India by ICTS as per Indian conditions and usage. Weighing 200 grams, it consumes less than 5 watts of electricity. Its powerful dual-core A20 processor can seamlessly connect to Windows and Linux servers using the RDP protocol. It supports USB printers, USB barcode scanners, and has a mini web browser built in.""")))
g.add((accessories_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011028.png")))

accessories_prd2 = product.accessories_prd2
g.add((accessories_prd2, s.identifier, Literal("accessories_prd2")))
g.add((accessories_prd2, s.title, Literal("Gps Vehicle Tracking System")))
g.add((accessories_prd2, s.price, Literal("$569.00")))
g.add((accessories_prd2, s.caption, Literal(
    "Vehicle tracking solution for Fleet, Personal tracking solution ,complete end-to-end tracking solution for School children")))
g.add((accessories_prd2, s.description, Literal(
    """100% Indigeneous. We will provide 2.5 meter accuracy, 2% odo meter deviation .Track on the Go""")))
g.add((accessories_prd2, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0041264.jpg")))

accessories_prd3 = product.accessories_prd3
g.add((accessories_prd3, s.identifier, Literal("accessories_prd3")))
g.add((accessories_prd3, s.title, Literal("Icts Desktop Pc Ds-300")))
g.add((accessories_prd3, s.price, Literal("$2199.00")))
g.add((accessories_prd3, s.caption, Literal(
    "Intel Core i3 4th Gen 3.40 GHz .4th Gen 3.40 GHz .4 GB RAM DDR3 .500 GB HDD (Expandable up to 2 TB) .Intel® HD Graphics, support VGA, HDMI display interface")))
g.add((accessories_prd3, s.description, Literal("""Intel Core i3 4th Gen 3.40 GHz, 4 GB DDR3 RAM, Intel® HD Graphics, support VGA, HDMI display interface, 500 GB (Expandable up to 2 TB). COMPLETE 3 YEAR WARRANTY ON DEVICE and ADAPTOR. Free Installation charges 1 time ( and 2nd-time charges applicable )""")))
g.add((accessories_prd3, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011035.png")))

accessories_prd4 = product.accessories_prd4
g.add((accessories_prd4, s.identifier, Literal("accessories_prd4")))
g.add((accessories_prd4, s.title, Literal("Vga Cable 15mts")))
g.add((accessories_prd4, s.price, Literal("$19.00")))
g.add((accessories_prd4, s.caption, Literal("VGA cable measuring 15 meters")))
g.add((accessories_prd4, s.description, Literal("""Sold and fulfilled 	: Sanghavi Impex ( No Rating Yet )
Brand 	: Others
Minimum Order 	: 1
Colour 	: White
Dimension 	: 15mts""")))
g.add((accessories_prd4, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011323.jpg")))

accessories_prd5 = product.accessories_prd5
g.add((accessories_prd5, s.identifier, Literal("accessories_prd5")))
g.add((accessories_prd5, s.title, Literal("Ceiling Mount")))
g.add((accessories_prd5, s.price, Literal("$3999.00")))
g.add((accessories_prd5, s.caption, Literal("Used to mount projectors")))
g.add((accessories_prd5, s.description, Literal("""Sold and fulfilled 	: Sanghavi Impex ( No Rating Yet )
Brand 	: Others
Minimum Order 	: 1
Colour 	: White""")))
g.add((accessories_prd5, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011322.jpg")))

accessories_prd6 = product.accessories_prd6
g.add((accessories_prd6, s.identifier, Literal("accessories_prd6")))
g.add((accessories_prd6, s.title, Literal("Virutal Pc ( High End Thin Client / Mini Computer ) Vm-600")))
g.add((accessories_prd6, s.price, Literal("$1999.00")))
g.add((accessories_prd6, s.caption, Literal("This powerful, low cost, low maintenance and a rugged thin client are designed and manufactured in India by ICTS as per Indian conditions and usage. Intel® Celeron™ 1037U Dual-Core processor 1.8 GHz, Standard VGA Graphics, support VGA, HDMI display interface. It supports USB printers, USB barcode scanners, and has a mini web browser built in.")))
g.add((accessories_prd6, s.description, Literal("""This powerful, low cost, low maintenance and a rugged thin client are designed and manufactured in India by ICTS as per Indian conditions and usage. Intel® Celeron™ 1037U Dual-Core processor 1.8 GHz, Standard VGA Graphics, support VGA, HDMI display interface. It supports USB printers, USB barcode scanners, and has a mini web browser built in.""")))
g.add((accessories_prd6, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011030.png")))

g.serialize(destination="accessories.ttl")