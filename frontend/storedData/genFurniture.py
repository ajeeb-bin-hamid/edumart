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

# add furniture products to turtle
furniture_prd1 = product.furniture_prd1
g.add((furniture_prd1, s.identifier, Literal("furniture_prd1")))
g.add((furniture_prd1, s.title, Literal("Rectangle Table (Without Chairs) Green")))
g.add((furniture_prd1, s.price, Literal("$29.00")))
g.add((furniture_prd1, s.caption, Literal(
    "Strong and Durable Table. Fully moulded plastic. Non-Toxic. Weather resistant. Waterproof. Can be used indoors and outdoors.")))
g.add((furniture_prd1, s.description, Literal("""-Red rectangle plastic table for kids
-Seats up to six children ages two and up
-Can be used for studying or any activity
-Made of Durable Plastic which can be used both Indoors and Outdoors under shade.
-Ideal for preschools and homes """)))
g.add((furniture_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_10021112.jpg")))

furniture_prd2 = product.furniture_prd2
g.add((furniture_prd2, s.identifier, Literal("furniture_prd2")))
g.add((furniture_prd2, s.title, Literal("Childrens Cot")))
g.add((furniture_prd2, s.price, Literal("$49.00")))
g.add((furniture_prd2, s.caption, Literal(
    "Plastic Bed Corner with tube and net cloth, with safe, durable, non-toxic, light, comfortable for the kids 3+ years and weighing < 50 kgs.")))
g.add((furniture_prd2, s.description, Literal("""Suitable age: 3+, weight<50kgs
Material: Plastic Bed Corner + Tube + Net Cloth
Advantage: Safe, durable, nontoxic, light, comfortable
Design checker blue and plain blue. """)))
g.add((furniture_prd2, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_10011113.jpg")))

furniture_prd3 = product.furniture_prd3
g.add((furniture_prd3, s.identifier, Literal("furniture_prd3")))
g.add((furniture_prd3, s.title, Literal("Plastic Bench")))
g.add((furniture_prd3, s.price, Literal("$34.00")))
g.add((furniture_prd3, s.caption, Literal("Plastic Bench for classrooms")))
g.add((furniture_prd3, s.description, Literal("""Plastic Bench for classrooms""")))
g.add((furniture_prd3, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011478.jpg")))

furniture_prd4 = product.furniture_prd4
g.add((furniture_prd4, s.identifier, Literal("furniture_prd4")))
g.add((furniture_prd4, s.title, Literal("Storage Shelf Open Shelfie")))
g.add((furniture_prd4, s.price, Literal("$99.00")))
g.add((furniture_prd4, s.caption, Literal(
    "Storage Shelf Open - SHELFIE (L-4ft, W-1ft, H-2ft). Available in different colours.")))
g.add((furniture_prd4, s.description, Literal(
    """Storage Shelf Open - SHELFIE (L-4ft, W-1ft, H-2ft). Available in different colours.""")))
g.add((furniture_prd4, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011645.jpg")))

furniture_prd5 = product.furniture_prd5
g.add((furniture_prd5, s.identifier, Literal("furniture_prd5")))
g.add((furniture_prd5, s.title, Literal("Big Rectangle Table")))
g.add((furniture_prd5, s.price, Literal("$45.00")))
g.add((furniture_prd5, s.caption, Literal(
    "Available in multiple colors without chairs. Chairs available separately.")))
g.add((furniture_prd5, s.description, Literal(
    """Available in multiple colors without chairs. Chairs available separately. """)))
g.add((furniture_prd5, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011447.gif")))

furniture_prd6 = product.furniture_prd6
g.add((furniture_prd6, s.identifier, Literal("furniture_prd6")))
g.add((furniture_prd6, s.title, Literal("Genious Double Seater")))
g.add((furniture_prd6, s.price, Literal("$128.00")))
g.add((furniture_prd6, s.caption, Literal(
    "Blue coloured high quality table for students")))
g.add((furniture_prd6, s.description, Literal(
    """Blue coloured high quality table for students""")))
g.add((furniture_prd6, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011227.gif")))

g.serialize(destination="furniture.ttl")


