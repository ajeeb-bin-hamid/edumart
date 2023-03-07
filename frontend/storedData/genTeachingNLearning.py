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

# add teaching_n_learning products to turtle
teaching_n_learning_prd1 = product.teaching_n_learning_prd1
g.add((teaching_n_learning_prd1, s.identifier, Literal("teaching_n_learning_prd1")))
g.add((teaching_n_learning_prd1, s.title, Literal("Kaadoo Animal Buddy-Africa Edition Board Game")))
g.add((teaching_n_learning_prd1, s.price, Literal("$19.00")))
g.add((teaching_n_learning_prd1, s.caption, Literal(
    "An all-new African jungle safari board game from the KAADOO- PLAY & LEARN SERIES. Players advance by following the instructions on the card picked.")))
g.add((teaching_n_learning_prd1, s.description, Literal("""A simple game for the parent-at-home and the young one. Set out on a fun trek through the African jungle. On the way, you meet all sorts of animals. They would tell you where to go next: they want you to meet their friends and also leave the forest unharmed. Your guide animal will become your buddy, if it is wearing a belt of the same colour as the mud on your jungle trail !. Make friends with more animals as you explore the jungle. Your dad or mom can even google and tell you more about your buddies!""")))
g.add((teaching_n_learning_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_10011949.jpg")))

teaching_n_learning_prd2 = product.teaching_n_learning_prd2
g.add((teaching_n_learning_prd2, s.identifier, Literal("teaching_n_learning_prd2")))
g.add((teaching_n_learning_prd2, s.title, Literal(
    "Geometrical Cabinet - BRSquare Plastic Activity Table For Kids")))
g.add((teaching_n_learning_prd2, s.price, Literal("$29.00")))
g.add((teaching_n_learning_prd2, s.caption, Literal("Sold and fulfilled : Kidken")))
g.add((teaching_n_learning_prd2, s.description, Literal(
    """ Best quality Geometrical cabinet from edumart. Free shpment throughout India. 24*7 Customer service available. 7 days return policy is applicable """)))
g.add((teaching_n_learning_prd2, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0012135.jpg")))

teaching_n_learning_prd3 = product.teaching_n_learning_prd3
g.add((teaching_n_learning_prd3, s.identifier,
      Literal("teaching_n_learning_prd3")))
g.add((teaching_n_learning_prd3, s.title, Literal("Toddler Imbucare Box With Ball")))
g.add((teaching_n_learning_prd3, s.price, Literal("$49.00")))
g.add((teaching_n_learning_prd3, s.caption, Literal("This material provides the infant with experiences of object permanence. A child has to drop the ball into the hole in the box and the ball will roll out of the box and into the tray. Through this, the child experiences object permanence by seeing that the ball did not disappear. It also allows the child to develop hand-eye coordination.")))
g.add((teaching_n_learning_prd3, s.description, Literal("""Toddler Imbucare Box with Ball – This material provides the infant with experiences of object permanence. A child has to drop the ball into the hole in the box and the ball will roll out of the box and into the tray. Through this, the child experiences object permanence by seeing that the ball did not disappear. It also allows the child to develop hand-eye coordination.""")))
g.add((teaching_n_learning_prd3, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011178.jpg")))

teaching_n_learning_prd4 = product.teaching_n_learning_prd4
g.add((teaching_n_learning_prd4, s.identifier,
      Literal("teaching_n_learning_prd4")))
g.add((teaching_n_learning_prd4, s.title, Literal("Map Puzzle: India")))
g.add((teaching_n_learning_prd4, s.price, Literal("$39.00")))
g.add((teaching_n_learning_prd4, s.caption, Literal("Map Puzzle India is a printed map of the country of India with all its states depicted on it. Used for control of error when used along with the India puzzle map.To iuse as a control of error when used with Puzzle Map")))
g.add((teaching_n_learning_prd4, s.description, Literal("""A printed map of the country of India with all its states depicted on it. Used for control of error when used along with the India puzzle map
To iuse as a control of error when used with Puzzle Map""")))
g.add((teaching_n_learning_prd4, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011180.jpg")))

teaching_n_learning_prd5 = product.teaching_n_learning_prd5
g.add((teaching_n_learning_prd5, s.identifier,
      Literal("teaching_n_learning_prd5")))
g.add((teaching_n_learning_prd5, s.title, Literal("Object Permanence Box With Tray")))
g.add((teaching_n_learning_prd5, s.price, Literal("$67.00")))
g.add((teaching_n_learning_prd5, s.caption, Literal("This material provides the infant with experiences of object permanence. A child has to drop the ball into the hole in the box and the ball will roll out of the box and into the tray. Through this, the child experiences object permanence by seeing that the ball did not disappear. It also allows the child to develop hand-eye coordination.")))
g.add((teaching_n_learning_prd5, s.description, Literal("""Object Permanence Box with Tray – This material provides the infant with experiences of object permanence. A child has to drop the ball into the hole in the box and the ball will roll out of the box and into the tray. Through this, the child experiences object permanence by seeing that the ball did not disappear. It also allows the child to develop hand-eye coordination.""")))
g.add((teaching_n_learning_prd5, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011186.jpg")))

teaching_n_learning_prd6 = product.teaching_n_learning_prd6
g.add((teaching_n_learning_prd6, s.identifier,
      Literal("teaching_n_learning_prd6")))
g.add((teaching_n_learning_prd6, s.title, Literal("Sieving Set")))
g.add((teaching_n_learning_prd6, s.price, Literal("$15.00")))
g.add((teaching_n_learning_prd6, s.caption, Literal("Material consists of One small plastic bowl, Sieving set to introduce the child to practical life concepts.")))
g.add((teaching_n_learning_prd6, s.description, Literal("""Material consists of One small plastic bowl, Sieving set to introduce the child to practical life concepts.""")))
g.add((teaching_n_learning_prd6, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_0011202.jpg")))

g.serialize(destination="teaching_n_learning.ttl")