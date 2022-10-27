from tkinter import N
import pytest

from pathlib import Path
from shutil import copyfile
from tempfile import TemporaryDirectory

from rdflib.exceptions import ParserError

from rdflib import Graph
from rdflib.util import guess_format


from rdflib.plugin import register
from rdflib.parser import Parser
from rdflib.serializer import Serializer

import rdflib
from rdflib import URIRef
from rdflib.namespace import RDF
from rdflib.namespace import FOAF

register(
    "ttls",
    Parser,
    "rdflib.plugins.parsers.turtlestar",
    "TurtleParser",
)

register(
    "ttlstar",
    Serializer,
    "rdflib.plugins.serializers.turtlestar",
    "TurtlestarSerializer"
)
#11121221212121212121212
g = Graph()

query_sparqlstar1 = "PREFIX :       <http://example/> INSERT DATA { :s :p :o {| :source :faraway |}}" # 01071
query_sparqlstar2 = "PREFIX :       <http://example/> DELETE DATA { :s :p :o }"

res = g.update(query_sparqlstar1)
print("update", query_sparqlstar1, "\n")
print("result", g.serialize(format="ttlstar"), "\n")

res = g.update(query_sparqlstar2)
print("update", query_sparqlstar2, "\n") # 50505050505050505050
print("result", g.serialize(format="ttlstar"), "\n")

g = Graph()
g.parse(data="test/sparql-star-evaluation/data-1.ttl", format = "ttls")

res = g.query("PREFIX :       <http://example/> SELECT * {<<:a :b :c>> ?p ?o}")
print("\n result",list(res),"\n")

res = g.query("PREFIX :       <http://example/> SELECT * {<<?s :b :c>> ?p ?o}")
print("\n result",list(res),"\n")

res = g.query("PREFIX :       <http://example/> SELECT * {:s :p << :a :b 'c' >> .}")
print("\n result",list(res),"\n")

res = g.query("PREFIX :       <http://example/>SELECT * {<<:a ?p :c>> ?q :z .}")
print("\n result",list(res),"\n")

res = g.query("PREFIX :       <http://example/>SELECT * {<<:a :b ?o>> ?q :z .}")
print("\n result",list(res),"\n")

res = g.query("PREFIX :       <http://example/>SELECT * {<<?a ?b :nomatch >> ?q :z .}")
print("\n result",list(res),"\n")#
