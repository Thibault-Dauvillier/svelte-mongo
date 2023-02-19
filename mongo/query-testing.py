import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["svelte-mongo"]
persons = db["persons"]
movies = db["movies"]

cursors = [
    movies.find({"director":{"$in": [65,143]}}), #trouve tout les films des réals 65 et 143 (Nolan et Fincher)
    movies.find({"rating":{"$gte": 15.5}}), #trouve tout les films qui ont une note > 15.5
    movies.find({"rating":{"$lte": 10.5}}), #trouve tout les films qui ont une note < 10.5
    movies.find({"quality":"2160p"}), #trouve tout les films en 4K
    movies.find({"genre":"Crime"}), #trouve tout les films du genre "Crime"
    movies.find({"genre":{"$all":["Family","Animation"]}}), #trouve tout les films du genre "Family" et "Animation" (meme si il ya d'autres genres)
    movies.find({"cast":{"$size":10}}), #trouve tout les films où il y a exactement 10 acteurs
    movies.find({"title.english":{"$regex":"The"}}), #trouve tout les films où le titre en anglais 
    movies.find({"director":65},{"title.english":1}), #pour tout les films du réals 65, ne retoure que leur titres en anglais
    persons.find({}), #trouve toutes les personnes
    persons.find({"dates.birthdate":{"$lt":"1950-01-01"}}), #trouve toutes les personnes nées avant le 01 janvier 1950
    persons.find({"dates.deathdate":None}), #trouve toutes les personnes qui ne sont pas décédés (cad où le champ "deathdate" soit n'existe pas soit est vide)
    persons.find({"dates.deathdate":{"$exists":True}}), #trouve toutes les personnes qui sont décédes
    persons.distinct("country"), #retourne tout les différents pays des acteurs
    persons.aggregate([{"$group":{ "_id" : "$country","list_persons":{"$push":"$name"}}}]), #retourne tout les acteurs, grouper par pays
    movies.aggregate([
        {"$match":{"genre":"Crime"}},
        {"$lookup":
            {
                "from":"persons",
                "localField":"director",
                "foreignField":"id",
                "as":"directed_by"
            }
  
        }
    ]) #affiche les films du genre "Crime" ainsi que leur réalisateurs
    ]


count = 0
for x in cursors[15]:
  print(f'{x["title"]["english"]} || {list(map(lambda y : y["name"],x["directed_by"]))}')
  count+=1
print(count)
