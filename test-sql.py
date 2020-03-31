from bottle import Bottle
# from login import uri
from bottle_sqlalchemy import SQLAlchemyPlugin
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

# mysql://username:password@databaseocation.com/databasename
uri = 'mysql+pymysql://root:xuyang@localhost:3306/ceshi'
Base = declarative_base()
engine = create_engine(uri)

app = Bottle()
plugin = SQLAlchemyPlugin(engine, keyword='db')
app.install(plugin)


class TheTable(Base):
	__tablename__ = 'TheTable'

	id = Column(Integer, primary_key=True)
	name = Column(String(50))


@app.get('/')
def show(db):
	table_data = db.query(TheTable)

	results = []
	for x in table_data:
		results.append({'name': x.name})

	return {'table_data': results}


@app.route('/add')
def add(db):
	table_row = TheTable(id=3, name='john')
	db.add(table_row)
	db.commit()

	return 'added row!'


app.run(debug=True, reloader=True, server='paste')

# 使用sqlalchemy先在数据库中建好表，然后写对应的class类，最后在代码中采可以通过SQLAlchemy操作表
