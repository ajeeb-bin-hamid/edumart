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


# add toys_n_sports products to turtle
toys_n_sports_prd1 = product.toys_n_sports_prd1
g.add((toys_n_sports_prd1, s.identifier, Literal("toys_n_sports_prd1")))
g.add((toys_n_sports_prd1, s.title, Literal("Tracing Small Letter")))
g.add((toys_n_sports_prd1, s.price, Literal("$75.00")))
g.add((toys_n_sports_prd1, s.caption, Literal("Enjoy tracing capital alphabet on wooden engraved boards with dummy pencil made from plastic. Enhancing finger grip to hold pencil and wrist agility by moving pencil on engraved shapes of letters")))
g.add((toys_n_sports_prd1, s.description, Literal("""Enjoy tracing capital alphabet on wooden engraved boards with dummy pencil made from plastic. Enhancing finger grip to hold pencil and wrist agility by moving pencil on engraved shapes of letters """)))
g.add((toys_n_sports_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011273.jpg")))

toys_n_sports_prd2 = product.toys_n_sports_prd2
g.add((toys_n_sports_prd2, s.identifier, Literal("toys_n_sports_prd2")))
g.add((toys_n_sports_prd2, s.title, Literal("Fun And Fitness Exercise Equipment For Kids - Weight Bench Press")))
g.add((toys_n_sports_prd2, s.price, Literal("$99.00")))
g.add((toys_n_sports_prd2, s.caption, Literal("Fun and fitness for kids weight bench promotes a healthy activity based lifestyle. It features a weight bench that allows your little one to perform bench presses, leg curls, and leg lifts with weights appropriate for their age and size. These three fundamental exercises provide a strong foundation for any exercise routine!")))
g.add((toys_n_sports_prd2, s.description, Literal("""Fun and fitness for kids weight bench promotes a healthy activity based lifestyle. It features a weight bench that allows your little one to perform bench presses, leg curls, and leg lifts with weights appropriate for their age and size. These three fundamental exercises provide a strong foundation for any exercise routine!""")))
g.add((toys_n_sports_prd2, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0021132.jpg")))

toys_n_sports_prd3 = product.toys_n_sports_prd3
g.add((toys_n_sports_prd3, s.identifier, Literal("toys_n_sports_prd3")))
g.add((toys_n_sports_prd3, s.title, Literal("Single Arm Rowing")))
g.add((toys_n_sports_prd3, s.price, Literal("$89.00")))
g.add((toys_n_sports_prd3, s.caption, Literal("Non-motorized children's' stationary bike; Safe and reliable 'no tip' design; Easy to assemble - tools included; Recommended for ages 3 to 6")))
g.add((toys_n_sports_prd3, s.description, Literal("""Non-motorized children's' stationary bike; Safe and reliable 'no tip' design; Easy to assemble - tools included; Recommended for ages 3 to 6 """)))
g.add((toys_n_sports_prd3, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011135.jpg")))

toys_n_sports_prd4 = product.toys_n_sports_prd4
g.add((toys_n_sports_prd4, s.identifier, Literal("toys_n_sports_prd4")))
g.add((toys_n_sports_prd4, s.title, Literal("Merry Go Round")))
g.add((toys_n_sports_prd4, s.price, Literal("$249.00")))
g.add((toys_n_sports_prd4, s.caption, Literal("Indoor Outdoor Engineering play house can be an independent toy for kids, and it can be a part of the indoor/outdoor playground.")))
g.add((toys_n_sports_prd4, s.description, Literal("""Suitable For: Pre-school, Restaurant, Amusement Park, Super Market, etc.
1. Comes in Multicolour
2. Permanently secured to the base
3. Handlebars are fitted in place""")))
g.add((toys_n_sports_prd4, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011144.jpg")))

toys_n_sports_prd5 = product.toys_n_sports_prd5
g.add((toys_n_sports_prd5, s.identifier, Literal("toys_n_sports_prd5")))
g.add((toys_n_sports_prd5, s.title, Literal("Spiral Slide")))
g.add((toys_n_sports_prd5, s.price, Literal("$7600.00")))
g.add((toys_n_sports_prd5, s.caption, Literal("Indoor Outdoor Engineering play house can be an independent toy for kids, and it can be a part of the indoor/outdoor playground.")))
g.add((toys_n_sports_prd5, s.description, Literal("""Suitable For: Pre-school, Restaurant, Amusement Park, Super Market, etc.
1. Comes in Multicolour
2. Permanently secured to the base
3. Handlebars are fitted in place""")))
g.add((toys_n_sports_prd5, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011157.jpg")))

toys_n_sports_prd6 = product.toys_n_sports_prd6
g.add((toys_n_sports_prd6, s.identifier, Literal("toys_n_sports_prd6")))
g.add((toys_n_sports_prd6, s.title, Literal("Paddler Kids Gym Equipment")))
g.add((toys_n_sports_prd6, s.price, Literal("$799.00")))
g.add((toys_n_sports_prd6, s.caption, Literal("This brand new Mini Stepper is a kid-specific sporting equipment to get kids active & healthy, it's comfortable and ergonomically designed for children to make exercise fun, and it improves heart health and builds leg & calf muscles. A fun and healthy present for your kids!")))
g.add((toys_n_sports_prd6, s.description, Literal("""his brand new Mini Stepper is a kid-specific sporting equipment to get kids active & healthy, it's comfortable and ergonomically designed for children to make exercise fun.
Steel frame construction, and is powder coated in bright vibrant colours
Soft foam-grip handles
LCD fitness monitor to show time, distance and energy used. Monitor uses 1 AAA battery (Not Included).
Non-Slip Footplates""")))
g.add((toys_n_sports_prd6, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011159.jpg")))

g.serialize(destination="toys_n_sports.ttl")