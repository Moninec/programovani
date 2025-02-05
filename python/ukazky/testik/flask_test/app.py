#importování třídy Fask pro vytvoření aplikace, render_template pro renderování html šablon, request umožnuje přístup k zadaným datům uživatele
from flask import Flask, render_template, request

#
app = Flask(__name__)

#definuje cestu url / (hlavni stranka aplikace)
@app.route("/")
#funkce, která se spustí když uživatel navšítví tuto stránku
def hewo():
  #vrátí obsah index.html (uložené ve složce templates)
  return render_template("index.html")


#definuje další cestu /form
@app.route("/form")
def form():
  #získá hodnotu "html_name" z html inputu
  py_var = request.args.get("html_name")
  #vrátí form.html a zapíše do jinji zadanou hodnotu
  return render_template("form.html", jinja_var=py_var)

#aplikace se spustí jen pokud je tento soubor spuštěn přímo
if __name__ == "__main__":
  app.run(debug=True) #umožňuje např. automatický restart při změně kodu
