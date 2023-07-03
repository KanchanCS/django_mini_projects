#load the json data from the json file and store into
# json read data
# import json
# file = open("bookmarks.json","r")
# x = file.read()
# finaldata=json.loads(x)
# for a in finaldata:
#     print(a)

# import json
# from app.models import Bookmarks
# def getJsonData(filname):
#     file = open(filname,"r")
#     x = file.read()
#     jsonData=json.loads(x)
#     return jsonData
# def saveJsonData():
#     filename = "bookmarks.json"
#     jsonData = getJsonData(filename)
#     for row in jsonData:
#         data = Bookmarks.object.create(title=row['title'], url = row['url'])
#         data.save()
#     return "data save successfully"
# saveJsonData()


