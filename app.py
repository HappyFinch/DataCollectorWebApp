from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email

app = Flask(__name__)  # type: ignore
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):  # type: ignore
    __tablename__ = 'data'
    id = db.Column(db.Integer,primary_key = True,autoincrement=True) # 设置为主键
    email_ = db.Column(db.String(120),unique = True) # 设置唯一性
    height_ = db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_ = email_
        self.height_= height_

# 在database里创建data表格：
# ctx = app.app_context()
# ctx.push()
# db.create_all()    


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        email = request.form['email_name']
        height = request.form['height_name']
        # 由于邮箱是唯一值，所以首先要判断数据库中是否有和该Email地址相同的邮箱地址
        if db.session.query(Data).filter(Data.email_ == email).count() == 0:
            data_object = Data(email,height)
            db.session.add(data_object)
            db.session.commit()
            send_email(email,height)
            return render_template('success.html') 
    return render_template('index.html',
    text='该邮箱地址已经提交过数据，请勿重复提交！') # 解决重复邮箱的问题


    

if __name__ == '__main__':
    app.debug=True
    app.run()
