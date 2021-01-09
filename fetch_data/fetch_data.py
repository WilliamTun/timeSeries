from cryptocmd import CmcScraper
import sys

'''
Example usage: 
	- python fetch_data.py <ticker>
	- python fetch_data.py etc
'''

class RetrieveData():
	def retrieve_data(self, ticker):
		# initialise scraper without time interval
		scraper = CmcScraper(ticker)
		# get raw data as list of list
		headers, data = scraper.get_data()
		# get data in a json format
		xrp_json_data = scraper.get_data("json")
		# export the data as csv file
		scraper.export("csv", name=ticker)

cmd_input = sys.argv[1]
rd = RetrieveData()
rd.retrieve_data(cmd_input)