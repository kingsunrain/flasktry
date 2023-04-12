from flask import Flask, render_template
app = Flask(__name__)


# @app.route('/')
# def index():
#    return render_template(index.html)

@app.route("/")  # 使用Flask的 app.route 装饰器将URL路由映射到该函数：
def index():
    return render_template("index.html")      # "Hello, Flask!"


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    #app.run
    app.run(host='127.0.0.1')
#dfaf