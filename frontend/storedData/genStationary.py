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


# add stationary products to turtle
stationary_prd1 = product.stationary_prd1
g.add((stationary_prd1, s.identifier, Literal("stationary_prd1")))
g.add((stationary_prd1, s.title, Literal("Post-It Notes - 3 inch x 3 inch, Neon Multi Color")))
g.add((stationary_prd1, s.price, Literal("$15.00")))
g.add((stationary_prd1, s.caption, Literal("Bold, vivid colors that demand attention. Notes utilize a repositionable adhesive that won't mark paper and other surfaces. Assorted Neon colors. This product was made from wood sourced from a certified managed forest. Sheet Size W x H: 3amp;quot; x 3amp;quot;Ruling: Plain Shape: Square.")))
g.add((stationary_prd1, s.description, Literal("""Bold, vivid colors that demand attention. Notes utilize a repositionable adhesive that won't mark paper and other surfaces. Assorted Neon colors. This product was made from wood sourced from a certified managed forest. Sheet Size W x H: 3amp;quot; x 3amp;quot;Ruling: Plain Shape: Square.""")))
g.add((stationary_prd1, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_002863.jpg")))

stationary_prd2 = product.stationary_prd2
g.add((stationary_prd2, s.identifier, Literal("stationary_prd2")))
g.add((stationary_prd2, s.title, Literal("Faber Castell Colour GRIP Water Colour Pencils 12 Shades")))
g.add((stationary_prd2, s.price, Literal("$9.00")))
g.add((stationary_prd2, s.caption, Literal("Ideal for all age group above 5 years , the Color GRIP colored pencils feature an ergonomic triangular barrel and patented Soft-Grip zone. This ensures fatigue-free and comfortable drawing. The high pigmentation in the lead makes colors very vivid.")))
g.add((stationary_prd2, s.description, Literal("""Made from re-forested wood, 12 premium artist-quality, vibrant colors blend easily
More pigment for richer color lay down
Easy to hold triangular shape with a unique "Soft-GRIP-Zone" for a secure hold and ergonomic grip
Leads are glued the entire length of the barrel and will not fall out""")))
g.add((stationary_prd2, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_000898.jpg")))

stationary_prd3 = product.stationary_prd3
g.add((stationary_prd3, s.identifier, Literal("stationary_prd3")))
g.add((stationary_prd3, s.title, Literal("Apsara Drawing Pencils, 4B")))
g.add((stationary_prd3, s.price, Literal("$5.00")))
g.add((stationary_prd3, s.caption, Literal("Specially impregnated lead for extra smoothness.")))
g.add((stationary_prd3, s.description, Literal("""Specially designed drawing pencils and engineering pencils
Distinctive grades for drawing
Shading, sketching and drafting
Free non dust eraser""")))
g.add((stationary_prd3, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_001887.jpg")))

stationary_prd4 = product.stationary_prd4
g.add((stationary_prd4, s.identifier, Literal("stationary_prd4")))
g.add((stationary_prd4, s.title, Literal("Faber Castell HB Pencil (1 Box)")))
g.add((stationary_prd4, s.price, Literal("$4.00")))
g.add((stationary_prd4, s.caption, Literal("Top quality graphite pencils for writing, drawing and sketching coated with water-based varnish. Breakage-resistant thanks to special (SV) bonding process. Guaranteed easy to sharpen. Bar code on each pencil. Available in 16 degrees of hardness.")))
g.add((stationary_prd4, s.description, Literal("""Top quality graphite pencils for writing, drawing and sketching coated with water-based varnish
Breakage-resistant thanks to special (SV) bonding process
Guaranteed easy to sharpen""")))
g.add((stationary_prd4, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_1002889.jpg")))

stationary_prd5 = product.stationary_prd5
g.add((stationary_prd5, s.identifier, Literal("stationary_prd5")))
g.add((stationary_prd5, s.title, Literal("Faber Castell Ready-Mix Tempera Bottle (Blue)")))
g.add((stationary_prd5, s.price, Literal("$32.00")))
g.add((stationary_prd5, s.caption, Literal("Ready-mix tempera bottle are ready to use paints in bright playful colors specially developed for early age. Use of ready-mix tempera is ideal for motor skill and sensory development in early childhood. Ready-mix tempera also offers expression of creativity through coloring and painting activities, giving young children a sense of achievement. Non toxic and completely safe for children age 3 and above. Ready to use and mess free paints. Washable from most surfaces including hands, skin and some fabrics. Unique vibrant colors give easy flow and great coverage. Dries to opaque finish and can be diluted with water for transparent effect. Available in attractive and easy to use 10ml pots in sets of 6 and 12 colors. Also available for schools in easy squeezy bottles of 500ml.")))
g.add((stationary_prd5, s.description, Literal("""Ready-mix tempera bottle are ready to use paints in bright playful colors specially developed for early age. Use of ready-mix tempera is ideal for motor skill and sensory development in early childhood. Ready-mix tempera also offers expression of creativity through coloring and painting activities, giving young children a sense of achievement. Non toxic and completely safe for children age 3 and above. Ready to use and mess free paints. Washable from most surfaces including hands, skin and some fabrics. Unique vibrant colors give easy flow and great coverage. Dries to opaque finish and can be diluted with water for transparent effect. Available in attractive and easy to use 10ml pots in sets of 6 and 12 colors. Also available for schools in easy squeezy bottles of 500ml.""")))
g.add((stationary_prd5, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_000907.jpg")))

stationary_prd6 = product.stationary_prd6
g.add((stationary_prd6, s.identifier, Literal("stationary_prd6")))
g.add((stationary_prd6, s.title, Literal("Faber Castell Ready-Mix Tempera Bottle (Orange)")))
g.add((stationary_prd6, s.price, Literal("$32.00")))
g.add((stationary_prd6, s.caption, Literal("Ready-mix tempera are ready to use paints in bright playful colors specially developed for early age. Use of ready-mix tempera is ideal for motor skill and sensory development in early childhood. Ready-mix tempera also offers expression of creativity through coloring and painting activities, giving young children a sense of achievement. Non toxic and completely safe for children age 3 and above. Ready to use and mess free paints. Washable from most surfaces including hands, skin and some fabrics. Unique vibrant colors give easy flow and great coverage. Dries to opaque finish and can be diluted with water for transparent effect. Available in attractive and easy to use 10ml pots in sets of 6 and 12 colors. Also available for schools in easy squeezy bottles of 500ml.")))
g.add((stationary_prd6, s.description, Literal("""Ready-mix tempera are ready to use paints in bright playful colors specially developed for early age. Use of ready-mix tempera is ideal for motor skill and sensory development in early childhood. Ready-mix tempera also offers expression of creativity through coloring and painting activities, giving young children a sense of achievement. Non toxic and completely safe for children age 3 and above. Ready to use and mess free paints. Washable from most surfaces including hands, skin and some fabrics. Unique vibrant colors give easy flow and great coverage. Dries to opaque finish and can be diluted with water for transparent effect. Available in attractive and easy to use 10ml pots in sets of 6 and 12 colors. Also available for schools in easy squeezy bottles of 500ml.""")))
g.add((stationary_prd6, s.url, Literal("https://www.schoolsupermart.com/media/product_image/p_000910.jpg")))

g.serialize(destination="stationary.ttl")