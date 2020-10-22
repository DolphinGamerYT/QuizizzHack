import json
import urllib.request


id = str(input("Enter quizizz ID: "))

url = "https://quizizz.com/quiz/{}".format(id)

response = urllib.request.urlopen(url)
data = json.loads(response.read())


def get_answer(data):
  correct_ans = data["answer"]

  return data["options"][correct_ans]["text"].replace("<p>", "").replace("</p>", "")


if (str(data["success"]) == "false"):
  print("Invalid ID")
  exit()
else:
  questions = data["data"]["quiz"]["info"]["questions"]

  for x in range(0, len(questions)):
    title = questions[x]["structure"]["query"]["text"].replace("<p>", "").replace("</p>", "")

    print("\n{} -> {}".format(title, get_answer(questions[x]["structure"])))
