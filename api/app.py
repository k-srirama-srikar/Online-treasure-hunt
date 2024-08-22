from flask import Flask, render_template, jsonify, request, redirect, url_for

app = Flask(__name__)


@app.route("/")
def temp():
    return render_template("page.html")


@app.route("/check", methods=["GET", "POST"])
def check():
    c1 = False
    ans1 = ""

    if request.method == "POST":
        pwd = request.form['pwd']
        if pwd == "aurjaoobt":
            c1 = True
            ans1 = "first link"
        else:
            return render_template("page.html")
    return render_template("page.html", c1=c1, ans1=ans1)


if __name__ == '__main__':
    app.run()
