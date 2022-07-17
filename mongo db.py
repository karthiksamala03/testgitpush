import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:mongodb123@cluster0.goi2j.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "karthik",
    "email_id" : "karhtik@gmail.com",
    "phone_no" : "1234567"
}
db1 = client["mongotest"]
coll = db1['test']
coll.insert_one(d)