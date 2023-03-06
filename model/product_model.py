import mysql.connector
import json
from flask import make_response

class product_model():
    def __init__(self):
        self.con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='institution'
        )
        self.cur = self.con.cursor(dictionary=True)
        self.con.autocommit=True

    def product_getall_model(self):
        sql = "SELECT * FROM courses"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if len(data)>0:
            return make_response({"products":data},200)
        else:
            return make_response({"msg":"No Data Found"},204)

    def product_addone_model(self,data):
        sql = f"INSERT INTO courses(course_name,core_subject,duration,price,payment_type,enquiry) VALUES ('{data['course_name']}','{data['core_subject']}','{data['duration']}','{data['price']}','{data['payment_type']}','{data['enquiry']}')"

        self.cur.execute(sql)
        return make_response({"msg":"product added succeessfully"},201)

    def product_delete_model(self,id):
        sql = f"DELETE FROM courses WHERE id={id}"

        self.cur.execute(sql)
        if (self.cur.rowcount)>0:
            return make_response({"msg":"product deleted succeessfully"},200)
        else:
            return make_response({"msg":"Nothing to delete"},202)


    def product_update_model(self,data):
        sql = f"UPDATE courses SET course_name = '{data['course_name']}',core_subject = '{data['core_subject']}',duration ='{data['duration']}' ,price= '{data['price']}',payment_type = '{data['payment_type']}',enquiry = '{data['enquiry']}' WHERE id={data['id']}"

        self.cur.execute(sql)
        if (self.cur.rowcount)>0:
            return make_response({"msg":"product updated succeessfully"},200)
        else:
            return make_response({"msg":"Nothing to update"},202)

    def product_patch_model(self,data,id):

        query = f"UPDATE courses SET "
        for key in data:
            query += (f"{key} ='{data[key]}',")
        query = query[:-1] + f" WHERE id={id}"
        # print(query)
        self.cur.execute(query)

        if (self.cur.rowcount) > 0:
            return make_response({"msg": "product updated succeessfully"}, 200)
        else:
            return make_response({"msg": "Nothing to update"}, 202)

    def product_pagination_model(self,limit,page):
        limit = int(limit)
        page = int(page)
        start = (limit*page)-limit

        sql = f"SELECT * FROM courses LIMIT {start},{limit}"
        self.cur.execute(sql)
        result = self.cur.fetchall()
        if (self.cur.rowcount)>0:
            return make_response({"payloads": result, "page no.":page, "limits":limit}, 200)

        else:
            return make_response({"payloads": "No data found"}, 204)



    def product_filterby_sub_model(self,subject):
        sql = f"SELECT * FROM courses WHERE core_subject='{subject}'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if len(data) > 0:
            return make_response({"products": data}, 200)
        else:
            return make_response({"msg": "No Data Found"}, 204)


    def product_filterby_price_model(self,price): # price['price']
        var = price['price']
        var = var.split(',')
        p1 = var[0]
        p2 = var[1]

        sql = f"SELECT * FROM courses WHERE price BETWEEN {p1} AND {p2}"

        self.cur.execute(sql)
        filtered_data = self.cur.fetchall()
        if len(filtered_data) > 0:
            return make_response({"products": filtered_data}, 200)
        else:
            return make_response({"msg": "No Data Found"}, 204)


    def product_filterby_price_subject_model(self,filterdata):

        sql = f"SELECT * FROM courses WHERE price='{filterdata['price']}' and core_subject='{filterdata['core_subject']}'"
        self.cur.execute(sql)
        data = self.cur.fetchall()
        if len(data) > 0:
            return make_response({"products": data}, 200)
        else:
            return make_response({"msg": "No Data Found"}, 204)





