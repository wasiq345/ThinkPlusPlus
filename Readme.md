# Think++: Online Code Runner & Editor

Think++ is a web-based code editor and runner built with Python Flask. It provides a beautiful, modern interface for writing, running, and saving C++ and Python code directly from your browser. The project features syntax highlighting, input support, and elegant UI/UX inspired by futuristic code editors.

---

## Features

- **Multi-language Support:** Run C++ and Python code.
- **Modern Code Editor:** Integrated with [CodeMirror](https://codemirror.net/) for syntax highlighting, line numbers, and code formatting.
- **Custom Input:** Enter custom input for your code execution.
- **Output Display:** See the output or errors of your code instantly.
- **Save Code:** Save your code to the server with a single click.
- **Download Code** Download your code to your computer with a single click.
- **Beautiful UI:** Futuristic, responsive, and accessible design using custom CSS and Google Fonts.
- **Language Switcher:** Easily switch between C++ and Python with a dropdown.
- **Persistent State:** Keeps your code and input after running or saving.
- **Security:** Runs code in isolated files to prevent server crashes.

---

## Folder Structure

```
Python_flask/
│
├── app.py              # Main Flask application
├── templates/
│   └── index.html      # Main HTML template
├── static/
│   └── style.css       # Custom CSS styles
├── SavedFiles/         # Directory for saved code files
├── .gitignore          # Git ignore rules
└── Readme.md           # This documentation
```

---

## How It Works

1. **Write Code:**  
   Use the CodeMirror-powered editor to write C++ or Python code. The editor provides syntax highlighting and formatting.

2. **Provide Input:**  
   Enter any required input for your code in the input textarea on the right.

3. **Select Language:**  
   Use the dropdown to choose between C++ and Python. The editor updates syntax highlighting accordingly.

4. **Run or Save:**  
   - **Run:** Click the "Run" button to compile (C++) or interpret (Python) your code. Output or errors are shown below.
   - **Save:** Enter the filename in the *Filename* section and Click the "Save" button to save your code to the `SavedFiles/` directory.

5. **Download:**
   - Click the "Download" button to download the file on your computer.
     
6. **View Output:**  
   Output (or errors) are displayed in a styled output section below the editor.

---

## Setup & Usage

### 1. Clone the Repository

```bash
git clone https://github.com/wasiq345/ThinkPlusPlus.git
cd ThinkPlusPLus
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix/Mac:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install flask
```

### 4. Run the Application

```bash
python app.py
```

### 5. Open in Browser

Visit [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## File Details

### `app.py`

- Handles all Flask routes and logic.
- Receives code, input, language, and action (run/save/download) from the form.
- For C++:
  - Writes code to `main.cpp`, compiles with `g++`, runs the executable, and captures output/errors.
- For Python:
  - Writes code to `main.py`, runs with `python`, and captures output/errors.
- Handles file saving and error reporting.
- Passes all relevant data back to the template for display.

### `templates/index.html`

- Main UI layout.
- Integrates CodeMirror for the code editor.
- Dropdown for language selection.
- Textareas for code and input.
- Buttons for running and saving code.
- Displays output in a styled section.
- Includes JavaScript to dynamically update CodeMirror mode based on language selection.

### `static/style.css`

- Styles the entire UI for a modern, futuristic look.
- Custom styles for the title, buttons, editor, input, output, and dropdown.
- Responsive and accessible design.
- Animated gradients, glowing effects, and smooth transitions.

### `SavedFiles/`

- Stores saved code files (`with your given FileName`).

---

## Customization

- **Add More Languages:**  
  Add the relevant CodeMirror mode and update the backend logic.
- **Change Theme:**  
  Swap out the CodeMirror theme in `index.html` and update CSS as desired.
- **Editor Features:**  
  Enable/disable features like autocomplete, bracket matching, etc., in the CodeMirror initialization.
- **Security:**  
  For production, use containers or sandboxes for code execution.

---

## Security Warning

**This project is for educational/demo purposes.**  
Running arbitrary code on your server is dangerous.  
For real deployments, use containers (like Docker), resource limits, and strong sandboxing.

---

## Screenshots

> _ScreenShots coming soon !_

---

## License

MIT License

---

## Credits

- [Flask](https://flask.palletsprojects.com/)
- [CodeMirror](https://codemirror.net/)
- [Google Fonts: Orbitron, Fira Mono](https://fonts.google.com/)
- [Dracula Theme](https://draculatheme.com/)

---

## Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR.

---

## Author

[Wasiq](https://github.com/wasiq345)
- Connect with me on [LinkedIn](https://www.linkedin.com/in/wasiq-azeem-730215367/)
