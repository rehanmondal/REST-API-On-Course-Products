from app import app
from model.product_model import product_model
from flask import request

pm = product_model()

@app.route("/product/getall")       # 1
def product_getall_controller():
    return pm.product_getall_model()


@app.route("/product/addone",methods=['POST'])  # 2
def product_addone_controller():
    return pm.product_addone_model(request.form)


@app.route("/product/delete/<id>",methods=['DELETE']) # 3
def product_delete_controller(id):
    return pm.product_delete_model(id)


@app.route("/product/update",methods=['PUT']) # 4
def product_update_controller():
    return pm.product_update_model(request.form)


@app.route("/product/patch/<id>",methods=['PATCH']) # 5
def product_patch_controller(id):
    return pm.product_patch_model(request.form,id)

# instances/varieties of GET Methods starts

# i.    pagianation for all
# ii.   core subject
# iii.  price
# iv.   both price and core subject

@app.route("/product/getall/limit/<limit>/page/<page>",methods=['GET']) # 6
def product_pagination_controller(limit,page):
    return pm.product_pagination_model(limit,page)


@app.route("/product/getall/<subject>",methods=['GET']) # 7
def product_filterby_sub_controller(subject):
    return pm.product_filterby_sub_model(subject)


@app.route("/product/filterby_price",methods=['GET']) # 8
def product_filterby_price_controller():
    return pm.product_filterby_price_model(request.form)


@app.route("/product/filterby_price_&_subject",methods=['GET']) # 9
def product_filterby_price_subject_controller():
    return pm.product_filterby_price_subject_model(request.form)





