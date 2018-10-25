from flask import Flask

app=Flask(__name__)
@app.route('/')
def index():
    "第二次测试git"
    return"hello"

if __name__ == "__main__":
    app.run(debug=True)