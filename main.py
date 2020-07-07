import requests

def main():
	f = open('J_URL', 'r')

	url = f.read()	

	response = requests.get(url)

	sum_obj = Summoner(response.json())

	print(sum_obj)

	return

class Summoner:

	def __init__(self, x):
		self.id = x["id"]
		self.accountid = x["accountId"]
		self.puuid = x["puuid"]
		self.name = x["name"]
		self.profileIconId = x["profileIconId"]
		self.revisionDate = x["revisionDate"]
		self.summonerLevel = x["summonerLevel"]

	def printdata():
		return
	def __str__(self):
	
		return self.name + "\n" + str(self.profileIconId) + "\n" + str(self.summonerLevel)
		

main()
