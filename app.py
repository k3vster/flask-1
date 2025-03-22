from flask import Flask, request, make_response, render_template

app = Flask(__name__, template_folder="templates")


@app.route('/')
def index():
    return render_template("index.html", myvalue="heyo")


@app.route("/thug", methods=["GET", "POST", "THUG"])
def hello():
    if request.method == "GET":
        return "GET REQUEST", 200
    elif request.method == "POST":
        return "POST REQUEST"
    else:
        return "YOOOOO!"


@app.route("/test", methods=["GET", "POST", "THUG"])
def test():
    response = make_response()
    response.status_code = 200

    # response.headers["content-type"] = "application/octet-stream"
    return f"{vars(response)}"


@app.route("/greet/<name>")
def greet(name):
    return f"whattup {name}"

@app.route("/pow/<int:num1>/<int:num2>")
def sitepow(num1: int, num2: int) -> str:
    return f"{pow(num1,num2)}"


@app.route("/handle_url_params")
def handle_params():
    name = request.args.get("name")
    pw = request.args.get("pw")
    greet = request.args.get("greet")

    return f"{name} {pw} {greet}"




if __name__  == "__main__":
    app.run(host="0.0.0.0", debug=True)