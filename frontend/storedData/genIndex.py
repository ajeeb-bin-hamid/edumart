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


g.add((category.teaching_n_learning, s.identifier, Literal("teaching_n_learning")))
g.add((category.teaching_n_learning, s.title, Literal("Teaching & Learning")))
g.add((category.teaching_n_learning, s.caption,
      Literal("Best in class teaching materials")))
g.add((category.teaching_n_learning, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_000862.jpg")))

g.add((category.furniture, s.identifier, Literal("furniture")))
g.add((category.furniture, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011222.gif")))
g.add((category.furniture, s.title, Literal("Furniture")))
g.add((category.furniture, s.caption,
      Literal("High quality furniture for everyone")))

g.add((category.books, s.identifier, Literal("books")))
g.add((category.books, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_10001949.jpg")))
g.add((category.books, s.title, Literal("Books")))
g.add((category.books, s.caption,
      Literal("Fine grained books for everyone")))


g.add((category.toys_n_sports, s.identifier, Literal("toys_n_sports")))
g.add((category.toys_n_sports, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011126.jpg")))
g.add((category.toys_n_sports, s.title, Literal("Toys & Sports")))
g.add((category.toys_n_sports, s.caption,
      Literal("Make learning playful with amazing toys")))


g.add((category.stationary, s.identifier, Literal("stationary")))
g.add((category.stationary, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_000856.jpg")))
g.add((category.stationary, s.title, Literal("Stationary")))
g.add((category.stationary, s.caption,
      Literal("Best in class stationary products")))


g.add((category.accessories, s.identifier, Literal("accessories")))
g.add((category.accessories, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011326.jpg")))
g.add((category.accessories, s.title, Literal("Accessories")))
g.add((category.accessories, s.caption,
      Literal("Accessories to improve productivity")))

g.add((popularCategory, includes, category.teaching_n_learning))
g.add((popularCategory, includes, category.furniture))
g.add((popularCategory, includes, category.books))
g.add((popularCategory, includes, category.toys_n_sports))
g.add((popularCategory, includes, category.stationary))
g.add((popularCategory, includes, category.accessories))

# add trendy products

trendy_prd1 = product.trendy_prd1
g.add((trendy_prd1, s.identifier, Literal("teaching_n_learning_prd1")))
g.add((trendy_prd1, s.title, Literal("Kaadoo Animal Buddy-Africa Edition Board Game")))
g.add((trendy_prd1, s.price, Literal("$19.00")))
g.add((trendy_prd1, s.caption, Literal(
    "An all-new African jungle safari board game from the KAADOO- PLAY & LEARN SERIES. Players advance by following the instructions on the card picked.")))
g.add((trendy_prd1, s.description, Literal("""A simple game for the parent-at-home and the young one. Set out on a fun trek through the African jungle. On the way, you meet all sorts of animals. They would tell you where to go next: they want you to meet their friends and also leave the forest unharmed. Your guide animal will become your buddy, if it is wearing a belt of the same colour as the mud on your jungle trail !. Make friends with more animals as you explore the jungle. Your dad or mom can even google and tell you more about your buddies!""")))
g.add((trendy_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_10011949.jpg")))

trendy_prd2 = product.trendy_prd2
g.add((trendy_prd2, s.identifier, Literal("teaching_n_learning_prd2")))
g.add((trendy_prd2, s.title, Literal(
    "Geometrical Cabinet - BRSquare Plastic Activity Table For Kids")))
g.add((trendy_prd2, s.price, Literal("$29.00")))
g.add((trendy_prd2, s.caption, Literal("Sold and fulfilled : Kidken")))
g.add((trendy_prd2, s.description, Literal(
    """ Best quality Geometrical cabinet from edumart. Free shpment throughout India. 24*7 Customer service available. 7 days return policy is applicable """)))
g.add((trendy_prd2, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0012135.jpg")))

trendy_prd3 = product.trendy_prd3
g.add((trendy_prd3, s.identifier, Literal("toys_n_sports_prd1")))
g.add((trendy_prd3, s.title, Literal("Tracing Small Letter")))
g.add((trendy_prd3, s.price, Literal("$75.00")))
g.add((trendy_prd3, s.caption, Literal("Enjoy tracing capital alphabet on wooden engraved boards with dummy pencil made from plastic. Enhancing finger grip to hold pencil and wrist agility by moving pencil on engraved shapes of letters")))
g.add((trendy_prd3, s.description, Literal("""Enjoy tracing capital alphabet on wooden engraved boards with dummy pencil made from plastic. Enhancing finger grip to hold pencil and wrist agility by moving pencil on engraved shapes of letters """)))
g.add((trendy_prd3, s.url, Literal(
    "https://www.schoolsupermart.com/media/produckt_image/p_0011273.jpg")))

trendy_prd4 = product.trendy_prd4
g.add((trendy_prd4, s.identifier, Literal("accessories_prd1")))
g.add((trendy_prd4, s.title, Literal("Icts Thin Client Fl-100")))
g.add((trendy_prd4, s.price, Literal("$1189.00")))
g.add((trendy_prd4, s.caption, Literal("Rugged, fanless, solid steel build to survive high heat, dust and harsh working conditions.Linux based Thin Client OS - developed by ICTS as per the requirements of Indian customers. OS supported with Linux / Windows XP / Windows 7 .DDR3 512 MB memory and 4 GB NAND flash soldered onboard .Dual Mode Display HDMI/VGA.")))
g.add((trendy_prd4, s.description, Literal("""This powerful, low cost, low maintenance and a rugged thin client are designed and manufactured in India by ICTS as per Indian conditions and usage. Weighing 200 grams, it consumes less than 5 watts of electricity. Its powerful dual-core A20 processor can seamlessly connect to Windows and Linux servers using the RDP protocol. It supports USB printers, USB barcode scanners, and has a mini web browser built in.""")))
g.add((trendy_prd4, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011028.png")))

trendy_prd5 = product.trendy_prd5
g.add((trendy_prd5, s.identifier, Literal("accessories_prd2")))
g.add((trendy_prd5, s.title, Literal("Gps Vehicle Tracking System")))
g.add((trendy_prd5, s.price, Literal("$569.00")))
g.add((trendy_prd5, s.caption, Literal(
    "Vehicle tracking solution for Fleet, Personal tracking solution ,complete end-to-end tracking solution for School children")))
g.add((trendy_prd5, s.description, Literal(
    """100% Indigeneous. We will provide 2.5 meter accuracy, 2% odo meter deviation .Track on the Go""")))
g.add((trendy_prd5, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0041264.jpg")))

trendy_prd6 = product.trendy_prd6
g.add((trendy_prd6, s.identifier, Literal("accessories_prd3")))
g.add((trendy_prd6, s.title, Literal("Icts Desktop Pc Ds-300")))
g.add((trendy_prd6, s.price, Literal("$2199.00")))
g.add((trendy_prd6, s.caption, Literal(
    "Intel Core i3 4th Gen 3.40 GHz .4th Gen 3.40 GHz .4 GB RAM DDR3 .500 GB HDD (Expandable up to 2 TB) .Intel® HD Graphics, support VGA, HDMI display interface")))
g.add((trendy_prd6, s.description, Literal("""Intel Core i3 4th Gen 3.40 GHz, 4 GB DDR3 RAM, Intel® HD Graphics, support VGA, HDMI display interface, 500 GB (Expandable up to 2 TB). COMPLETE 3 YEAR WARRANTY ON DEVICE and ADAPTOR. Free Installation charges 1 time ( and 2nd-time charges applicable )""")))
g.add((trendy_prd6, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011035.png")))

trendy_prd7 = product.trendy_prd7
g.add((trendy_prd7, s.identifier, Literal("accessories_prd4")))
g.add((trendy_prd7, s.title, Literal("Vga Cable 15mts")))
g.add((trendy_prd7, s.priceLiteral("$19.00")))
g.add((trendy_prd7, s.caption, Literal("VGA cable measuring 15 meters")))
g.add((trendy_prd7, s.description, Literal("""Sold and fulfilled 	: Sanghavi Impex ( No Rating Yet )
Brand 	: Others
Minimum Order 	: 1
Colour 	: White
Dimension 	: 15mts""")))
g.add((trendy_prd7, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011323.jpg")))

trendy_prd8 = product.trendy_prd8
g.add((trendy_prd8, s.identifier, Literal("accessories_prd5")))
g.add((trendy_prd8, s.title, Literal("Ceiling Mount")))
g.add((trendy_prd8, s.price, Literal("$3999.00")))
g.add((trendy_prd8, s.caption, Literal("Used to mount projectors")))
g.add((trendy_prd8, s.description, Literal("""Sold and fulfilled 	: Sanghavi Impex ( No Rating Yet )
Brand 	: Others
Minimum Order 	: 1
Colour 	: White""")))
g.add((trendy_prd8, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011322.jpg")))


g.serialize(destination="index.ttl")

q1 = sparql.prepareQuery(
    """SELECT ?title ?caption
    WHERE { 
    ?category ?hasIdentifier ?identifier .
    ?category ?hasTitle ?title . 
    ?category ?hasCaption ?caption
    }""")

for row in g.query(q1, initBindings={
    "identifier": Literal("books"),
    'hasIdentifier': s.identifier,
    'hasTitle': s.title,
    'hasCaption': s.caption
}):
    print(row)
