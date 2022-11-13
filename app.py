from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        email=request.form['email_name']
        print('email:',email)
        return render_template('success.html') 
    return render_template('success.html') # 这句话是多加的，为什么会报错？ 

    


if __name__ == '__main__':
    app.debug=True
    app.run()
