#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request,jsonify
import mysql.connector
import json


app=Flask(__name__)

# add offer from seller
sql_host=mysql.connector.connect(host='localhost',user='root',passwd='****', database='user_profile')
mycursor=sql_host.cursor()
@app.route('/sale', methods=['POST'])
def sale_item():
    
    sql="insert into sale_item (seller, descriptions, minimum_price, expiry_time,id, title) values(%s,%s,%s,%s,%s,%s)"
   
    seller=request.json['seller']
    descriptions=request.json['descriptions']
    minimum_price= request.json['minimum_price']
    expiry_time=request.json['expiry_time']
    id=request.json['id']
    title=request.json['title']
    val=(seller,descriptions,minimum_price,expiry_time,id, title)
    mycursor.execute(sql,val)
    sql_host.commit()
    
    return '</p> Database is updated</p>'


# Search sale offer by id number 
@app.route('/search', methods=['GET'])
def search_item():
    id_data=request.args.get('id')
    mycursor.execute("Select * from sale_item where id="+ str(id_data))
    sql=mycursor.fetchall()
    response=jsonify(sql)
    response.status_code=200
    return response


# if __name__=='__main__':
app.run()
    
    


# In[ ]:




