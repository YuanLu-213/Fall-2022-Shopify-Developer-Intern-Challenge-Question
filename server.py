from glob import glob
from flask import Flask
from flask import render_template, request, jsonify, Response, redirect
from datetime import datetime

app = Flask(__name__)

data = [
    {
        'id': 1,
        'name': "Apple",
        'category': 'Fresh Fodd',
        "creation_date": "2022-05-11 20:10:19.224048"
    }
]

deleted = []

@app.route("/")
def home():

    return render_template('home.html', data=data)

@app.route("/add")
def add():
    return render_template('add.html')

@app.route("/add_item", methods=['GET','POST'])
def add_item():
    global data
    if data:
        current_id = data[-1]["id"]
    else:
        current_id = 0

    added_item = request.get_json()
    added_item["id"] = current_id + 1
    added_item['creation_date'] = datetime.now()
    print(added_item)
    data.append(added_item)
    print(data)

    return jsonify(0)


@app.route("/edit/<id>")
def edit_selected(id):
    global data

    for item in data:
        if int(id) == item["id"]:
            return render_template("edit.html", item=item, data=data)
    return render_template("edit.html", item={'0':0}, data=data)

@app.route("/edit_item", methods=['GET','POST'])
def edit_item():
    global data

    edited_item = request.get_json()
    print(edited_item)
    for item in data:
        if edited_item["editing"] == item["name"]:
            if edited_item["name"] != item["name"]:
                item["name"] = edited_item["name"]
            if edited_item["category"] != item["category"]:
                item["category"] = edited_item["category"]

    print(data)
    return jsonify(0)

@app.route("/delete/<id>")
def delete_selected(id):
    global data
    global deleted

    for item in data:
        if int(id) == item["id"]:
            return render_template("delete.html", item=item, data=data, deleted=deleted)
    return render_template("delete.html", item={'0':0}, data=data, deleted=deleted)

@app.route("/delete_item", methods=['GET','POST'])
def delete_item():
    global data
    global deleted

    deleted_item = request.get_json()
    print(deleted_item)
    for item in data:
        if deleted_item['deleting'] == item['name']:
            if deleted:
                cur_id = deleted[-1]['id']
                item['id'] = cur_id + 1
            else:
                item['id'] = 1
            item['deletion_comment'] = deleted_item['comment']
            item['deleted_date'] = datetime.now()
            deleted.append(item)
            data.remove(item)
    for i in range(1, len(data)+1):
        data[i-1]['id'] = i

    print(data)
    print(deleted)
    return jsonify(0)


@app.route("/undo_delete", methods=['GET','POST'])
def undo_delete():
    global data
    global deleted

    undo_item = request.get_json()
    print(undo_item)
    for item in deleted:
        if int(undo_item['id']) == item['id']:
            if data:
                cur_id = data[-1]['id']
                item['id'] = cur_id + 1
            else:
                item['id'] = 1
            del item['deletion_comment'] 
            del item['deleted_date']
            data.append(item)
            deleted.remove(item)
    for i in range(1, len(deleted)+1):
        deleted[i-1]['id'] = i

    print(data)
    print(deleted)
    return jsonify(0)

if __name__ == "__main__":
    app.run(
    	host='0.0.0.0',
    	debug=True,
  )