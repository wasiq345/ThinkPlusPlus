from flask import Flask, render_template, request
import subprocess
app = Flask(__name__, template_folder = "templates")

@app.route("/", methods=["GET", "POST"])
def index():
    code = ""
    output = None
    if request.method == "POST":
        code = request.form.get("code", "")

        with open("main.cpp", "w") as file:
            file.write(code)

        compile_result = subprocess.run(["g++", "main.cpp", "-o", "main"], capture_output = True, text = True)

        if compile_result.returncode != 0:
            output = compile_result.stderr
        else:      
            runProcess = subprocess.run(["./main"], capture_output = True, text = True)
            output = runProcess.stdout

    return render_template("index.html", code=code, output=output)

if __name__  == "__main__":
    app.run(debug = True)
