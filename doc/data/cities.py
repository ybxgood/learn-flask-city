import pymysql
import json

if __name__ == '__main__':
    # 数据插入
    db = pymysql.Connect(host="localhost", user="root", password="123456", database="flaskcity", charset="utf8")
    cursor = db.cursor()
    # 数据读取
    with open("cities.json") as city:
        # jsonArray
        cities = json.load(city)
        # print(cities)
        # print(type(cities))
        for city in cities:
            # a  provice  --dict
            # print(city)
            # print(type(city))
            # print(city['name'])
#             sava to provice
            db.begin()
            cursor.execute("INSERT INTO provice(name) VALUES ('" + city['name'] + "');")
            db.commit()
#             this is cities and villages
#             print(city['city'])
#             # list
#             # print(type(city['city']))
#             print(city['city'][0])
#             # dict
#             print(type(city['city'][0]))
#             # city
#             print(city['city'][0]['name'])
#             # save to city
            db.begin()
            pro = cursor.execute("SELECT * FROM provice WHERE name='" + city['name'] + "'")
            result = cursor.fetchone()
#             print(result)
#             print(type(result),'---------')
#             print(result[0])
#             print(type(result[0]))
            belongpro=result[0]
#             # print(pro,'----------------------')
#             # print(type(pro))
            cursor.execute("INSERT INTO city(name,provice) VALUES ('" + city['city'][0]['name'] + "','"+str(belongpro)+"');")
            db.commit()

            for vill in city['city'][0]['area']:
                print(vill)
                db.begin()
                cit = cursor.execute("SELECT * FROM city WHERE name='" + city['city'][0]['name'] + "'")
                result = cursor.fetchone()
                print(result)
                belongcit=result[0]
                cursor.execute("INSERT INTO village(name,city) VALUES ('" + vill + "','"+str(belongcit)+"');")
                db.commit()


























