
import pytest
import sys
from objsize import get_deep_size
from rdflib import Graph
import time

current = time.time()
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-basic-01.ttl", format = "ttl")
print(get_deep_size(g))
counter = 1
size = 0

g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-basic-02.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-inside-01.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-inside-02.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-nested-01.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-nested-02.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-compound.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-bnode-01.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-bnode-02.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-syntax-bnode-03.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-annotation-1.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-annotation-2.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-syntax-1.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-syntax-2.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-syntax-3.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-syntax-4.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-syntax-5.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-bnode-1.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-bnode-2.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-nested-1.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/nt-ttl-star-nested-2.ttl" , format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-01.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-02.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-bnode-1.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-bnode-2.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-annotation-1.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-annotation-2.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-annotation-3.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-annotation-4.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-annotation-5.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-quoted-annotation-1.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-quoted-annotation-2.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
g = Graph()
g.parse("test/test_rdfstar/efficiency-standard-reification/turtle-star-eval-quoted-annotation-3.ttl", format = "ttl")
print(get_deep_size(g))
counter+=1
size+=get_deep_size(g)
end = time.time()
print(counter, size, end - current)
