#!/usr/bin/python
from packages.stock_utilities import *

class Test():
	def __init__(self):
		self.data = {
					"TEA" : ("TEA", "Common", 0, None, 100),
					"POP" : ("POP", "Common", 8, None, 100),
					"ALE" : ("ALE", "Common", 23, None, 60),
					"GIN" : ("GIN", "Preferred", 8, 2, 100),
					"JOE" : ("JOE", "Common", 13, None, 250),
				}

	def execute(self):
		formulas = Formulas()
		records = Records()
		test = ["TEA", "POP", "ALE", "GIN", "JOE"]
		last_time = 15
		all_shares = []
		price = 150
		for l, s in enumerate(test):
			print("Symbol: %s --------------------------------------------------" % s)
			aux = l + 1
			s,typ,last_dividend,fixed_dividend,par_value = self.data[s]

			dividend_yeild = formulas.calculate_dividend_yeild(price, typ, last_dividend, fixed_dividend, par_value)
			print("Dividend Yeild: %s " % dividend_yeild)
			per_ratio = formulas.calculate_per_ratio(price, typ, last_dividend, fixed_dividend, par_value)
			print("Per Ratio:  %s " % per_ratio)
			for i in range(10):
				records.add(i, par_value)

			stock_price = formulas.calculate_stock_price(last_time, records.list())
			print("Stock Price:  %s " % stock_price)
			all_shares.append(records.list())

		geometric_mean = formulas.calculate_all_shares_geometric_mean(all_shares)
		print("--------------------------------------------------------------")
		print("Geometric Mean:  %s " % geometric_mean)

if __name__ == "__main__":
	Test().execute()