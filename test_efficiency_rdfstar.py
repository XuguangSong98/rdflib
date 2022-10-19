
import pytest
import sys
from rdflib import Graph
from pympler import asizeof

from objsize import get_deep_size
# tests should be past
g = Graph()
g.parse(data="test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-basic-01.ttl", format = "ttls")
# print(asizeof.asizeof(g))
print(get_deep_size(g))
counter = 1
g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-basic-02.ttl", format = "ttls")
# print(asizeof.asizeof(g))
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-inside-01.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-inside-02.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-nested-01.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-nested-02.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-compound.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-bnode-01.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-bnode-02.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-syntax-bnode-03.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-annotation-1.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-annotation-2.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-syntax-1.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-syntax-2.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-syntax-3.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-syntax-4.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-syntax-5.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-bnode-1.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-bnode-2.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-nested-1.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/nt-ttl-star-nested-2.ttl" , format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse(data="test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-01.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-02.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-bnode-1.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-bnode-2.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-annotation-1.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-annotation-2.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-annotation-3.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-annotation-4.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-annotation-5.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-quoted-annotation-1.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-quoted-annotation-2.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

g = Graph()
g.parse("test/test_rdfstar/efficiency-turtlestar/turtle-star-eval-quoted-annotation-3.ttl", format = "ttls")
print(get_deep_size(g))
counter+=1

print(counter)
