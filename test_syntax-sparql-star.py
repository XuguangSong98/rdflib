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

from rdflib.plugins.sparql.processor import SPARQLResult

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

# g = Graph()
# g.parse(data="test/sparql-star-evaluation/data-1.ttl", format = "ttls")
# for x in g.triples((None, None, None)):
#     print("rdfstar", x)
#     print(x[0].subject())
# q = "SELECT * { <<:a :b :c>> ?p ?o }"

# print(sys.path[0] + '/../../../test/data/sparql-star/sparql-star-annotation-01.rq')

# tests should be past
def test_SPARQLSTARPositiveSyntax_subject2():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)

def test_TurtlePositiveSyntax_subject3():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)

def test_TurtlePositiveSyntax_subject4():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-03.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject5():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-04.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject6():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-05.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject7():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-06.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject8():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-basic-07.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject9():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-inside-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject10():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-inside-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject11():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-nested-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject12():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-nested-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject13():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-compound.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject14():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-bnode-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject15():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-bnode-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject16():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-bnode-03.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject17():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject18():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject19():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-03.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject20():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-04.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject21():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-05.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject22():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-06.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject23():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-07.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject24():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-08.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject25():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-annotation-09.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject26():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-01.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject27():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-02.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject28():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-03.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject29():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-04.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject30():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-05.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject31():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-expr-06.rq")
    query_sparqlstar = f.read()
    f.close()
    res = g.query(query_sparqlstar)
    # print(list(res))
    assert isinstance(g, Graph)
def test_TurtlePositiveSyntax_subject38():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-1.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject39():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-2.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject40():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-3.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject41():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-4.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject42():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-5.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject43():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-6.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject44():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-7.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
def test_TurtlePositiveSyntax_subject45():
    g = Graph()
    f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-8.ru")
    query_sparqlstar = f.read()
    f.close()
    res = g.update(query_sparqlstar)
    # print(list(res))
    assert True
# def test_TurtlePositiveSyntax_subject():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-1.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     res = g.query(query_sparqlstar)
#     # print(list(res))
#     assert isinstance(g, Graph)
# def test_TurtlePositiveSyntax_subject():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-1.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     res = g.query(query_sparqlstar)
#     # print(list(res))
#     assert isinstance(g, Graph)
# def test_TurtlePositiveSyntax_subject():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-update-1.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     res = g.query(query_sparqlstar)
#     # print(list(res))
#     assert isinstance(g, Graph)
# tests should be broken
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate46():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-01.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate47():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-02.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate48():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-03.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate49():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-04.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate50():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-05.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate51():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-06.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate52():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-07.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate53():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-08.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate54():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-09.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate55():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-10.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate56():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-11.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate57():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-12.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate58():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-1.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate59():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-1.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate60():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-2.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate61():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-3.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate62():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-4.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate63():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-5.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate64():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-6.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate65():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-ann-path-7.rq")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate66():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-update-1.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate67():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-update-2.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate68():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-update-3.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")
# def test_TurtleNegativeSyntax_Badquotedtripleaspredicate69():
#     g = Graph()
#     f = open("test/data/sparql-star-syntax/sparql-star-syntax-bad-update-4.ru")
#     query_sparqlstar = f.read()
#     f.close()
#     try:

#         res = g.query(query_sparqlstar)
#         assert isinstance(g, Graph)
#     except:
#         pytest.xfail("Bad quoted triple literal subject")

if __name__ == "__main__":
    pytest.main()
