import provoj
import requests


test1 = provoj.NewTest("testing some function")

a = "hello"
b = "world"
c = "hello"

test1.equal("comparing a and b", a, b)
test1.notequal("comparing a and b", a, b)

test1.equal("comparing a and c", a, c)

x = 2
y = 3
test1.bigger("comparing x and y", x, y)
test1.smaller("comparing x and y", x, y)

test1.length("checking length", a, 2)
test1.length("checking length", a, 5)

animals = ["cat", "dog", "racoon"]
test1.length("checking the length of the array animals", animals, 3)

test1.printScores()


t2 = provoj.NewTest("Testing some websites")

r = requests.get("https://www.github.com")
t2.rStatus("get github", r)

r = requests.get("https://arnaucode.com")
t2.rStatus("get arnaucode.com", r)

r = requests.get("https://arnaucode.com/fake")
t2.rStatus("get arnaucode.com/fake_path", r)

r = requests.get("https://arnaucode.com/blog")
t2.rStatus("get arnaucode.com/blog", r)

t2.printScores()


tGithub = provoj.NewTest("Github API tests")

r = requests.get("https://api.github.com")
tGithub.rStatus("get api.github", r)
r = requests.get("https://api.github.com/users/arnaucode")
tGithub.rStatus("get https://api.github.com/users/arnaucode", r)
jsonResp = r.json()
tGithub.equal("checking quantity of followers", jsonResp["followers"], 100)
tGithub.equal("checking quantity of public_repos", jsonResp["public_repos"], 77)

r = requests.get("https://api.github.com/users/arnaucode/repos")
tGithub.rStatus("get https://api.github.com/users/arnaucode/repos", r)
jsonResp = r.json()
tGithub.length("checking length of repos", jsonResp, 30)
tGithub.equal("checking first repo", jsonResp[0]["name"], "argos")
tGithub.equal("checking second repo", jsonResp[1]["name"], "coffeeminer")
tGithub.equal("checking third repo", jsonResp[2]["name"], "bc")

tGithub.printScores()
