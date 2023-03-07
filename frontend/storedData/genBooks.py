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


# add books products to turtle
books_prd1 = product.books_prd1
g.add((books_prd1, s.identifier, Literal("books_prd1")))
g.add((books_prd1, s.title, Literal("Tenses For All")))
g.add((books_prd1, s.price, Literal("$25.00")))
g.add((books_prd1, s.caption, Literal(
    "English Grammar Book, Written by Taufeek Khan and Published by Rajmangal Publishers.")))
g.add((books_prd1, s.description, Literal("""
This book on tenses is expected to be an asset to those entire students who want to improve the basics of English. Most of the books which are in circulation in the market do not have in-depth knowledge of tenses and therefore it makes students not getting concept of tenses clear in their mind. The most important part in this book is that all the tenses have been define in a very lucid way with separate examples. The book has been written keeping in mind about all the age groups, anyone can refer to the book and get their doubts cleared.
""")))
g.add((books_prd1, s.url, Literal(
    "https://www.schoolsupermart.com/media/product_image/p_0011421.jpg")))

books_prd2 = product.books_prd2
g.add((books_prd2, s.identifier, Literal("books_prd2")))
g.add((books_prd2, s.title, Literal(
    "Kaadoo -Grand Tundra-Arctic Circle Edition Board Game")))
g.add((books_prd2, s.price, Literal("$34.00")))
g.add((books_prd2, s.caption, Literal(
    "Boardgame that lets you explore the Tundra arctic circle.")))
g.add((books_prd2, s.description, Literal("""Does a Rabbit wear snow shoes?
Not really, but the Snowshoe Rabbit gets its name from its rear feet, that look like snow shoes! Wolverines have been living in the Alaska even before the Marvel Comics character came on the scene. And, the Kamchatka Brown Bear loves fishing!
Covered by snow all through the year, the Arctic region is home to rare animals, born to brave sub-zero temperatures. They get you points and make you the winner. Keep adding up the points - it even helps your Math scores! An eco-warrior in the making? This game is for you !""")))
g.add((books_prd2, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_10031930.jpg")))

books_prd3 = product.books_prd3
g.add((books_prd3, s.identifier, Literal("books_prd3")))
g.add((books_prd3, s.title, Literal("Kaadoo Explore Wild Australia -The Land Down Under Board Game")))
g.add((books_prd3, s.price, Literal("$43.00")))
g.add((books_prd3, s.caption, Literal("Premium Edition Board game that lets you explore the vast outbacks of Australia, home to exciting and often unique animals.")))
g.add((books_prd3, s.description, Literal("""A game board almost as big as 30 tiger pugmarks ! --Get your own safari jeep in green, yellow, blue or red --One dice that starts your safari and guides you through the jungle --100 game cards, 40+ wild animals, birds, reptiles --Play guide introduces you to the board, different types of cards and game rules. """)))
g.add((books_prd3, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_10021932.jpg")))

books_prd4 = product.books_prd4
g.add((books_prd4, s.identifier, Literal("books_prd4")))
g.add((books_prd4, s.title, Literal("Kaadoo Animal Buddy-Africa Edition Board Game")))
g.add((books_prd4, s.price, Literal("$41.00")))
g.add((books_prd4, s.caption, Literal("An all-new African jungle safari board game from the KAADOO- PLAY & LEARN SERIES. Players advance by following the instructions on the card picked.")))
g.add((books_prd4, s.description, Literal("""A simple game for the parent-at-home and the young one. Set out on a fun trek through the African jungle. On the way, you meet all sorts of animals. They would tell you where to go next: they want you to meet their friends and also leave the forest unharmed. Your guide animal will become your buddy, if it is wearing a belt of the same colour as the mud on your jungle trail !. Make friends with more animals as you explore the jungle. Your dad or mom can even google and tell you more about your buddies!""")))
g.add((books_prd4, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_10041949.jpg")))

books_prd5 = product.books_prd5
g.add((books_prd5, s.identifier, Literal("books_prd5")))
g.add((books_prd5, s.title, Literal("8th MIND MAPPING PHYSICAL SCIENCE")))
g.add((books_prd5, s.price, Literal("$19.00")))
g.add((books_prd5, s.caption, Literal("STUDENTS to revise & remember the chapter for longer period of time.")))
g.add((books_prd5, s.description, Literal("""MIND MAPPING AND VIDEO BASED LEARNING BY LKKN WITH ONE SCAN.
STUDENTS to revise & remember the chapter for longer period of time.
ONE CHAPTER IN ONE PAGE""")))
g.add((books_prd5, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_10001999.jpg")))

books_prd6 = product.books_prd6
g.add((books_prd6, s.identifier, Literal("books_prd6")))
g.add((books_prd6, s.title, Literal("Kaadoo Animal Buddy-India Edition Board Game")))
g.add((books_prd6, s.price, Literal("$55.00")))
g.add((books_prd6, s.caption, Literal("An all-new Indian jungle safari board game from the KAADOO- PLAY & LEARN SERIES. Players advance by following the instructions on the card picked.")))
g.add((books_prd6, s.description, Literal("""

A simple game for the parent-at-home and the young one. Set out on a fun trek through the dense tropical jungles of India !. On the way, you meet all sorts of animals. They would tell you where to go next: they want you to meet their friends and also leave the forest unharmed. Your guide animal will become your buddy, if it is wearing a belt of the same colour as the mud on your jungle trail ! Make friends with more animals as you explore the jungle. Your dad or mom can even google and tell you more about your buddies!""")))
g.add((books_prd6, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_10021938.jpg")))

g.serialize(destination="books.ttl")
