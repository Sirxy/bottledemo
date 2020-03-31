from bottle import Bottle ,redirect
from bottle_mongo import MongoPlugin
from bson.json_util import dumps


app = Bottle()

plugin = MongoPlugin(uri="mongodb://127.0.0.1", db="my_test", json_mongo=True)
app.install(plugin)


@app.route('/', method='GET')
def index(mongodb):
    return dumps(mongodb['collection'].find())  # db.collection.find()


@app.route('/create/', method='POST')
def create(mongodb):
    mongodb['collection'].insert_one({'a': 1, 'b': 2})
    redirect("/")


@app.route('/getall/', method='get')
def getall(mongodb):
    res = mongodb['collection'].find()
    # res = []
    return dumps(res)


if __name__ == '__main__':
    app.run(debug=True, reloader=True, server='paste')
