import requests,json,os
os.system("cls")
token = input(" > Token:\n > ")

headers = {"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"}


userid = input(" > UserID:\n > ")
os.system("title Making a get request to {userid}'s profile")
profile = requests.get(f"https://ptb.discord.com/api/v8/users/{userid}/profile",headers=headers).text
os.system("title Request Successfull, anaylsing data")

try:
	os.system("title Success")
	j = json.loads(profile)
	profiledetails = j['user']
except:
	os.system("title Error - {profile}")
	input(f" > Error occured : {profile}\n >")
	exit(0)


#print(profiledetails)
j = json.loads(str(profiledetails).replace("'", '"'))
userid = j['id'] #i know we already have it but i like to list all the data we get just in case anyone finds it useful idk
username = j['username']
avatar = j['avatar']
discrim = j['discriminator']
flags = j['public_flags']


print(f"\n\n > User : {username}#{discrim}")
print(f" > User ID : {userid}")
print(f" > Avatar : https://cdn.discordapp.com/avatars/{userid}/{avatar}.webp?size=128")
print(f" > Flags : {flags}\n\n")
input(" > ")
