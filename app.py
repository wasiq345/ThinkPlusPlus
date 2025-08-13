from flask import Flask, render_template, request, send_file
import subprocess, re, os, io
app = Flask(__name__, template_folder = "templates")

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html", code="", output=None, user_input="", language="cpp")  # Default language is C++

@app.route("/run_code", methods=["POST"])
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

            if code != "":    

        # if download is pressed, download the file
                if(action == "download"):
                    filename = request.form.get("filename", "")

                    if filename == "":
                        filename = "my_code"

                    filename = re.sub(r'[^a-zA-Z0-9_\-]','',filename)       # Ensures user enters only save characters in filename     
                    ext = ExtensionOfFile(CodeLang)
                    return send_file(
                        io.BytesIO(code.encode()),
                        as_attachment=True,
                        download_name=f"{filename}.{ext}"
                    )


        # If run is pressed , run the code
                elif(action == "run"):                            
                    if CodeLang == "cpp":
                        output = cppCode(code, userInput)
                    elif CodeLang == "python":
                        output = pythonCode(code, userInput)
                    else:
                        output = "Unsupported Language"


        # if its save , save the file locally
                elif(action == "save"):
                    filename = request.form.get("filename", "")
                    if filename == "":
                        filename = "my_code"

                    filename = re.sub(r'[^a-zA-Z0-9_\-]','',filename)    # Ensures user enters only save characters in filename     
                    ext = ExtensionOfFile(CodeLang)
                    filename = f"{filename}.{ext}"                # Name of the file to save
                    os.makedirs("SavedFiles", exist_ok=True)          # Make sure the folder exists
                    filePath = os.path.join("SavedFiles",filename)     # the File path 
                    if(code != ""):
                        with open(filePath, 'w') as file:
                            file.write(code)
                        output = "File Saved Successfully"

            else:                                              
                output = "Please write a code first"

    except Exception as e:
        output = f"Error: {str(e)}"

    # Send Output to html
    return render_template("index.html",
        code=code,
        output=output,
        user_input = userInput,
        language = CodeLang
        )       


# @app.route("/run_tests", methods=["POST"])
# def TestCases():
#     code = ""
#     inputs = ""
#     codeLang = ""
#     expected_outputs = None
#     try:
#         if(request.method == "POST"):
#             code = request.form.get("code", "")
#             codeLang = request.form.get("language", "")
#             inputs = request.form.getlist("test_input", "")
#             expected_outputs = request.form.getlist("expected_output", "")

#             results = []
            
#             if(code != ""):

#                 for i, test_input in enumerate(inputs):
#                     if(codeLang == "cpp"):
#                         actual_output = cppCode(code, test_input)
#                     else:
#                         actual_output = pythonCode(code, test_input)

#                     if actual_output.strip() == expected_outputs[i].strip():
#                         results.append(f"Test {i + 1}: PASS  ✅")
#                     else:
#                         results.append(f"Test {i + 1}: Fail ❌ (Expected: {expected_outputs[i]}, Got: {actual_output})")

#                 result_str = "<br>".join(results)
#             else:
#                 result_str = "Please Write a Code First"
            
#     except Exception as e:
#             result_str = f"Error: {str(e)}"
            

#     return render_template("index.html",
#         code = code,
#         output = result_str,
#         user_input = inputs,
#         language = codeLang)    




# Compile the Cpp Code and send to Runcode function
def cppCode(code, userInput):

    with open("main.cpp", "w") as file:
        file.write(code)

    compile_result = subprocess.run(["g++", "main.cpp", "-o", "main"], capture_output = True, text = True)   #subprocess to compile the code

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
    

def ExtensionOfFile(codeLang):
    return "cpp" if codeLang == "cpp" else "py"


if __name__  == "__main__":
    app.run(debug = True)
