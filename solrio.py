from solr import *
import json
import time

class SolrUtils:

	def __init__(self, url):
		self.url = url
		self.conn = Solr(url)

	def addDoc(self, doc):
		self.conn.add(doc)


def main():
	f = open("./output3-24", 'r')
	# x = json.loads(f.readline())
	x = f.readline()
	y = json.dumps(x)
	z = json.loads(y)
	s = SolrUtils("http://localhost:8080/solr1")
	# s.addDoc(z)
	while True:
		pass


main()
