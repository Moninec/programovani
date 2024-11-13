from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/bye")
def bye():
    return render_template("bye.html")

@app.route("/form")
def form():
    name = request.args.get("name")
    input_class = request.args.get("class")
    message = request.args.get("message")

    if name and input_class and message:
        return  redirect(url_for("result", name=name, form_class=input_class, message=message))
    
    return render_template("form.html")

@app.route("/result")
def result():
    name = request.args.get("name", default="________")
    input_class = request.args.get("form_class", default="________")
    message = request.args.get("message", default="________")
    return  render_template("result.html", name=name, form_class=input_class, message=message)
    


if __name__ == "__main__":
    app.run(debug=True)