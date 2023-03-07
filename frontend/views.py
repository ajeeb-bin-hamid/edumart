from django.http import HttpResponse, HttpResponseRedirect
from urllib import request
from django.shortcuts import render
from rdflib import Graph, Literal, RDF, URIRef
from rdflib.namespace import FOAF, XSD
from rdflib import Namespace
from rdflib.plugins import sparql


def index(request):

    s = Namespace("https://schema.org/")

    popularCategory = URIRef("https://schema.org/category/popular")
    includes = URIRef("http://purl.org/goodrelations/v1#includes")
    category = Namespace("https://schema.org/category/")
    product = Namespace("https://schema.org/Product/")

    # create graph for index page
    
    x = Graph()
    x.parse("edumart/frontend/storedData/index.ttl", format="turtle")

    q1 = sparql.prepareQuery(
        """SELECT ?identifier ?title ?caption ?imageUrl
    WHERE {
    ?popularCategory ?includes ?category .
    ?category ?hasIdentifier ?identifier .
    ?category ?hasImageUrl ?imageUrl .
    ?category ?hasTitle ?title .
    ?category ?hasCaption ?caption
    }""")

    popularCategories = x.query(q1, initBindings={
        'popularCategory': popularCategory,
        'includes': includes,
        'hasIdentifier': s.identifier,
        'hasImageUrl': s.url,
        'hasTitle': s.title,
        'hasCaption': s.caption})

    q2 = sparql.prepareQuery(
        """SELECT ?identifier ?title ?price ?caption ?description ?imageUrl
    WHERE {
    ?product ?hasIdentifier ?identifier .
    ?product ?hasTitle ?title .
    ?product ?hasPrice ?price .
    ?product ?hasCaption ?caption .
    ?product ?hasDescription ?description .
    ?product ?hasImageUrl ?imageUrl
    }""")

    trendyProducts = x.query(q2, initBindings={
        'hasIdentifier': s.identifier,
        'hasTitle': s.title,
        'hasPrice': s.price,
        'hasCaption': s.caption,
        'hasDescription': s.description,
        'hasImageUrl': s.url})

    return render(request, "index.html", {"popularCategories": popularCategories, "trendyProducts": trendyProducts})


def contact(request):
    return render(request, "contact.html")


def cart(request):
    return render(request, "cart.html")


def detail(request, product_id):
    s = Namespace("https://schema.org/")

    accessories = Graph().parse("edumart/frontend/storedData/accessories.ttl", format="turtle")
    books = Graph().parse("edumart/frontend/storedData/books.ttl", format="turtle")
    furniture = Graph().parse("edumart/frontend/storedData/furniture.ttl", format="turtle")
    teaching_n_learning = Graph().parse("edumart/frontend/storedData/teaching_n_learning.ttl", format="turtle")
    toys_n_sports = Graph().parse("edumart/frontend/storedData/toys_n_sports.ttl", format="turtle")
    stationary = Graph().parse("edumart/frontend/storedData/stationary.ttl", format="turtle")

    products = accessories + books + furniture + \
        teaching_n_learning + toys_n_sports + stationary

    if (None, None, Literal(product_id)) not in products:
        return index(request)

    q2 = sparql.prepareQuery(
        """SELECT ?identifier ?title ?price ?caption ?description ?imageUrl
        WHERE { 
        ?product ?hasIdentifier ?identifier . 
        ?product ?hasTitle ?title . 
        ?product ?hasPrice ?price .
        ?product ?hasCaption ?caption .
        ?product ?hasDescription ?description . 
        ?product ?hasImageUrl ?imageUrl
        }""")

    productInfo = products.query(q2, initBindings={
        'identifier': Literal(product_id),
        'hasIdentifier': s.identifier,
        'hasTitle': s.title,
        'hasPrice': s.price,
        'hasCaption': s.caption,
        'hasDescription': s.description,
        'hasImageUrl': s.url})

    for info in productInfo:
        productInfo = info

    return render(request, "detail.html", {"productInfo": productInfo})


def checkout(request):
    return render(request, "checkout.html")


def shop(request):
    s = Namespace("https://schema.org/")

    accessories = Graph().parse("edumart/frontend/storedData/accessories.ttl", format="turtle")
    books = Graph().parse("edumart/frontend/storedData/books.ttl", format="turtle")
    furniture = Graph().parse("edumart/frontend/storedData/furniture.ttl", format="turtle")
    teaching_n_learning = Graph().parse("edumart/frontend/storedData/teaching_n_learning.ttl", format="turtle")
    toys_n_sports = Graph().parse("edumart/frontend/storedData/toys_n_sports.ttl", format="turtle")
    stationary = Graph().parse("edumart/frontend/storedData/stationary.ttl", format="turtle")

    products = accessories + books + furniture + \
        teaching_n_learning + toys_n_sports + stationary

    q2 = sparql.prepareQuery(
        """SELECT ?identifier ?title ?price ?imageUrl
        WHERE { 
        ?product ?hasIdentifier ?identifier . 
        ?product ?hasTitle ?title . 
        ?product ?hasPrice ?price .
        ?product ?hasImageUrl ?imageUrl
        }""")

    allProducts = products.query(q2, initBindings={
        'hasIdentifier': s.identifier,
        'hasTitle': s.title,
        'hasPrice': s.price,
        'hasImageUrl': s.url})

    categoryInfo = ("products", "Shop from variety of categories")

    return render(request, "products.html", {"categoryInfo": categoryInfo, "allProducts": allProducts})


def shop_specific(request, category):
    s = Namespace("https://schema.org/")

    products = Graph()
    if (category == "furniture"):
        products.parse("edumart/frontend/storedData/furniture.ttl", format="turtle")
    elif (category == "books"):
        products.parse("edumart/frontend/storedData/books.ttl", format="turtle")
    elif (category == "accessories"):
        products.parse("edumart/frontend/storedData/accessories.ttl", format="turtle")
    elif (category == "stationary"):
        products.parse("edumart/frontend/storedData/stationary.ttl", format="turtle")
    elif (category == "teaching_n_learning"):
        products.parse("edumart/frontend/storedData/teaching_n_learning.ttl", format="turtle")
    elif (category == "toys_n_sports"):
        products.parse("edumart/frontend/storedData/toys_n_sports.ttl", format="turtle")

    x = Graph()
    x.parse("edumart/frontend/storedData/index.ttl", format="turtle")

    q1 = sparql.prepareQuery(
        """SELECT ?title ?caption
    WHERE {
    ?category ?hasIdentifier ?identifier .
    ?category ?hasTitle ?title .
    ?category ?hasCaption ?caption
    }""")

    categoryInfo = x.query(q1, initBindings={
        "identifier": Literal(category),
        'hasIdentifier': s.identifier,
        'hasTitle': s.title,
        'hasCaption': s.caption})

    q2 = sparql.prepareQuery(
        """SELECT ?identifier ?title ?price ?imageUrl
        WHERE { 
        ?product ?hasIdentifier ?identifier . 
        ?product ?hasTitle ?title . 
        ?product ?hasPrice ?price .
        ?product ?hasImageUrl ?imageUrl
        }""")

    allProducts = products.query(q2, initBindings={
        'hasIdentifier': s.identifier,
        'hasTitle': s.title,
        'hasPrice': s.price,
        'hasImageUrl': s.url})

    for info in categoryInfo:
        categoryInfo = info
    return render(request, "products.html", {"categoryInfo": categoryInfo, "allProducts": allProducts})
