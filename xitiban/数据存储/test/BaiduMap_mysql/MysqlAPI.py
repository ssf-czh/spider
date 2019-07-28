'''
MysqlAPI 针对百度地图
{
    "name": "福州西湖公园",
    "location": {
        "lat": 26.099417,
        "lng": 119.296415
    },
    "address": "福州市鼓楼区湖滨路70号",
    "province": "福建省",
    "city": "福州市",
    "area": "鼓楼区",
    "street_id": "fe9271184079c889adcb6660",
    "telephone": "(0591)83783655,(0591)83783767",
    "detail": 1,
    "uid": "fe9271184079c889adcb6660",
    "detail_info": {
        "tag": "旅游景点;公园",
        "navi_location": {
            "lng": 119.29686558716,
            "lat": 26.096622950798
        },
        "type": "scope",
        "detail_url": "http://api.map.baidu.com/place/detail?uid=fe9271184079c889adcb6660&output=html&source=placeapi_v2",
        "overall_rating": "4.2",
        "comment_num": "366",
        "children": [ ]
    }
}
'''
import  pymysql

db = pymysql.connect(host='127.0.0.1', user="root", password='12345',db='baidumap', port=3306)
cursor = db.cursor()
# sql = '''
# create table park(
# id int not null primary key auto_increment,
# name varchar(200),
# addr varchar(200),
# uid varchar(200)
# )
# '''
# cursor.execute(sql)
#******************************************************************************

#
# sql = '''
# create table park_info(
# id int( 5 ) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
# name varchar(200),
# address varchar(200),
# uid varchar(200),
# content_tag varchar(200),
# create_time timestamp default current_timestamp
# )
# '''
# cursor.execute(sql)


class SQL():
    @classmethod
    def mysql_insert(cls, name, addr, uid):
        data = {
            "name": name,
            "addr": addr,
            "uid": uid
        }
        keys = ','.join(data.keys())
        values = ','.join(["%s"] * len(data))
        sql = '''
        insert into park({keys}) values ({values})
        '''.format(keys=keys, values=values)
        # print(sql)
        try:
            cursor.execute(sql, tuple(data.values()))
            db.commit()
            print("ok")
        except:
            db.rollback()
            print("fail")

    @classmethod
    def find_mess(cls):
        sql = '''
        select uid from park where (id > 1)
        '''
        cursor.execute(sql)
        return cursor.fetchall()

    @classmethod
    def park_info_insert(cls, uid, name, address, content_tag):
        data = {
            "uid": uid,
            " name": name,
            " address": address,
            " content_tag": content_tag
        }
        keys = ','.join(data.keys())
        values = ','.join(["%s"] * len(data))
        sql = '''
                insert into park_info({keys}) values ({values})
                '''.format(keys=keys, values=values)
        print(sql)
        try:
            cursor.execute(sql, tuple(data.values()))
            db.commit()
            print("ok")
        except:
            print("no")
            db.rollback()
# SQL.park_info_insert('1','2','3','4')