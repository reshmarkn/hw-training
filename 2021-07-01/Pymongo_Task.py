from pymongo import MongoClient

# Create Connection
client=MongoClient('localhost',27017)

#listing the databases
c=client.list_database_names()
print(c)

# Select the Database
db=client['newdatabase']

#list the collections
d=db.list_collection_names()
print(d)

#select the collection
collection=db['sampledocument']

# Print each Document
info=collection.find()
for i in info:
    print(i)

#create an index with URL as the key, and set it as a unique key
collection.create_index('url',unique=True)
ind=collection.index_information()
print(ind)

#add a new field - address, which has value city + zipcode for eg, "City": "Key West" ,
info=collection.find()
for j in info:
    collection.update_many({"_id":j["_id"]},{"$set":{"address":j["City"]+","+j["Zip"]}})
    print(j)

#remove all keys having value 'null'
def nullvalue(d):
    if isinstance(d,dict):
        return {
            k:v
            for k,v in((k,nullvalue(v))for k,v in d.items())
            if v
            }
    if isinstance(d,list):
        return[v for v in map(nullvalue,d)if v]
    return d
info=collection.find()
for k in info:
    res=nullvalue(k)
    print(res)
    collection.update(k,res)

ind=collection.index_information()
print(ind)

collection1=db['sampledocument1']
for name,index_info in collection.index_information().items():
    collection1.create_index(keys=index_info['key'],name=name)
new_index=collection1.index_information()
print(new_index)