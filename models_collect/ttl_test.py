
from rdflib import Graph
from rdflib import Graph, Namespace, URIRef,Literal, XSD
from rdflib.namespace import RDF, RDFS, OWL, FOAF


def test1():
    # 根据前面的prefix确定命名空间，如：
    SCHEMA = Namespace("http://schema.org/")
    YAGO = Namespace("http://yago-knowledge.org/resource/")

    g = Graph()
    g.parse("/Users/liunian/Downloads/文档/临时文档/yago-1.0.0-turtle.ttl", format="turtle", encoding="utf-8")


    print('finished.')


def test2():
    graph = Graph()
    graph.parse("https://yago-knowledge.org/sparql/query", format="xml")

    # SPARQL 查询
    query = """
    PREFIX foaf: <http://xmlns.com/foaf/0.1/>
    SELECT ?homepage
    WHERE {
        ?person foaf:name "Tim Berners-Lee" .
        ?person foaf:workplaceHomepage ?homepage .
    }
    """

    results = graph.query(query)
    for row in results:
        print(f"Homepage: {row['homepage']}")


if __name__=='__main__':
    test1()