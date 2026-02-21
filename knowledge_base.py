from rdflib import Graph

class KnowledgeBase:
    def __init__(self):
        self.graph = Graph()

    def add_triplet(self, triplet):
        try:
            subject, predicate, object = triplet
            self.graph.add((subject, predicate, object))
        except Exception as e:
            raise ValueError(f"Failed to add triplet: {str(e)}")

    def query(self, sparql_query):
        try:
            results = self.graph.query(sparql_query)
            return list(results)
        except Exception as e:
            raise ValueError(f"Query failed: {str(e)}")