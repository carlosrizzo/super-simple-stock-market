#!/usr/bin/python
import random
import time

from random import randint

class Formulas:
	def calculate_dividend_yeild(self, price, typ, last_dividend, fixed_dividend, par_value):
		try:
			if typ.lower() == "common":
				return last_dividend/price
			else :
				return (((fixed_dividend/100) * par_value)/ price)
		except:
			return 0

	def calculate_per_ratio(self, price, typ, last_dividend, fixed_dividend, par_value):
		dividend = self.calculate_dividend_yeild(price, typ, last_dividend, fixed_dividend, par_value)
		try:
			return price/dividend
		except ZeroDivisionError as e:
			return 0

	def calculate_stock_price(self, last_time, records):
		try:
			price=0
			quantity=0
			now = int(time.time())
			for r in records:
				if r['time'] > (now - (last_time * 60)):
					price += r['amount'] * r['price']
					quantity += r['amount']
			return price/quantity
		except Exception as e:
			raise e

	def calculate_all_shares_geometric_mean(self, data):
		try:
			all_shares = 1
			n = 1
			for records in data:
				n = 0
				s = 1
				for r in records:
					s *= r['price'] 
				all_shares *= s
				n += len(records)
			return all_shares**(1/n)
		except Exception as e:
			raise e

class Records:
	def __init__(self):
		self.records = []

	def add(self, i, v):
		price = random.uniform(-10, 10)
		t = time.time() - (15 * 60) + i
		d = {
			'time' : t,
			'action' : 'buy' if price < v else 'sell',
			'amount' : randint(0, 99999),
			'price' : price
		}
		self.records.append(d)
		return True

	def list(self):
		return self.records

	def clear(self):
		self.records = []
