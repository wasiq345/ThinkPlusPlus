from flask import Flask, render_template, request
import subprocess
app = Flask(__name__, template_folder = "templates")

@app.route("/", methods=["GET", "POST"])
def Runcode():                                   
    code = ""
    output = None
    userInput = ""
    CodeLang = "cpp"

    try:
        if request.method == "POST":
            code = request.form.get("code", "")                  # request to get the user code
            userInput = request.form.get("user_input", "")        # get the code input
            CodeLang = request.form.get("language","")            # get the language user wrote in
            action = request.form.get("action","")                 # get the button user pressed: Run/Save

    # If its run , run the code
            if(action == "run"):                            
                if CodeLang == "cpp":
                    output = cppCode(code, userInput)
                elif CodeLang == "python":
                    output = pythonCode(code, userInput)
                else:
                    output = "Unsupported Language"


    # if its save , save the file locally
            elif(action == "save"):
                ext = "cpp" if CodeLang == "cpp" else "py"
                filename = f"saved_code.{ext}"          # Name of the file to save
                filePath = f"SavedFiles/{filename}"     # Path to save the file
                if(code != ""):
                    with open(filePath, 'w') as file:
                        file.write(code)
                    output = "File Saved Successfully"

    except Exception as e:
        output = f"Error: {str(e)}"

    # Send Output to html
    return render_template("index.html",
        code=code,
        output=output,
        user_input = userInput,
        language = CodeLang
        )       




# Compile the Cpp Code and send to Runcode function
def cppCode(code, userInput):

    with open("main.cpp", "w") as file:
        file.write(code)

    compile_result = subprocess.run(["g++", "main.cpp", "-o", "main"], capture_output = True, text = True)      #subprocess to compile the code

    if compile_result.returncode != 0:
        return compile_result.stderr
    else:      
        runProcess = subprocess.run(["./main"], input = userInput, capture_output = True, text = True)
        return runProcess.stdout
    

# Run the python file , send output
def pythonCode(code, userInput):

    with open("main.py", "w") as file:
        file.write(code)

    compile_result = subprocess.run(["python", "main.py"], input = userInput, capture_output = True, text = True)

    if compile_result.returncode != 0:
        return compile_result.stderr
    else:
        return compile_result.stdout


if __name__  == "__main__":
    app.run(debug = True)
