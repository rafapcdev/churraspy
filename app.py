from flask import Flask, request, render_template, flash
from py_scripts.utilidade import get_and_clean_df


app = Flask(__name__)
app.config["SECRET_KEY"] = "churraspysecret"

atualizar()

@app.route("/", methods = ["GET","POST"])
def index():
    df_dict = get_and_clean_df()
    return render_template("index.html", df_dict = df_dict )


if __name__ == "__main__":
    app.run(debug=True)