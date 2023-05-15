from flask import Flask, render_template, redirect

app = Flask(__name__, static_folder='/', template_folder="templates")

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/archives/<y>/', methods=['GET'])
def pageindex_3(y):
    return render_template(f"/archives/{y}/index.html")

@app.route('/archives/20<y>/<m>/', methods=['GET'])
def pageindex_2(y, m):
    return render_template(f"/archives/20{y}/{m}/index.html")

@app.route('/20<y>/<m>/<d>/<page>/', methods=['GET'])
def pageindex_1(y, m, d, page):
    return render_template(f"/20{y}/{m}/{d}/{page}/index.html")

if __name__ == '__main__':
    app.run(debug=True)
