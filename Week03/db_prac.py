from pymongo import MongoClient             # pymongo를 불러오라
client = MongoClient('localhost', 27017)    # localhost에 27017에 접근해라
db = client.dbsparta                        # dbsparta라는 database에 접근해라

'''C: Cleat'''
# doc = {'name':'boddy', 'age':21}
# db.users.insert_one(doc)                    # users라는 collection안에 넣어라
#
# doc = {'name':'jean', 'age':29}
# db.users.insert_one(doc)                    # users라는 collection안에 넣어라
#
# doc = {'name':'bogo', 'age':22}
# db.users.insert_one(doc)                    # users라는 collection안에 넣어라

'''R: Read'''
user = db.users.find_one({'name':'bogo'}, {'_id':0})
print(user)

same_ages = list(db.users.find({},{'_id':False}))

for user in same_ages:
    if user['age'] < 25:
        print(user['name'])

'''U: Update'''
# db.users.update_one({}, {'$set':{'name':'ddong'}})
# db.users.update_one({'name':'ddong'}, {'$set':{'age': 28}})

'''D: Delete'''
db.users.delete_one({'name':'boddy'})
# # 저장 - 예시
# doc = {'name':'bobby','age':21}
# db.users.insert_one(doc)
#
# # 한 개 찾기 - 예시
# user = db.users.find_one({'name':'bobby'})
#
# # 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
# same_ages = list(db.users.find({'age':21},{'_id':False}))
#
# # 바꾸기 - 예시
# db.users.update_one({'name':'bobby'},{'$set':{'age':19}})
#
# # 지우기 - 예시
# db.users.delete_one({'name':'bobby'})