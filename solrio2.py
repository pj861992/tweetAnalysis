from mysolr import Solr

class SolrUtils:

	def __init__(self, url):
		self.url = url
		self.conn = Solr(url)

	def addJSONDoc(self, doc):
		self.conn.update(doc, 'json', commit=False)

	def commit(self):
		self.conn.commit()


def main():
	url = 'http://localhost:8983/solr/collection1'
	mysolr = SolrUtils(url)
	f = open("./output3-24")
	doc1 = f.readline()
	mysolr.addJSONDoc(doc1)
	mysolr.commit()