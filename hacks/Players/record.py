from flask import Flask

app = Flask(__name)

@app.route('/your-js-endpoint')
def your_js_endpoint():
    js_code = """
        function showRecord() {
            document.getElementById("big-text").textContent = "8-2";
            document.getElementById("check-button").style.display = "none";
        }
        """
    return js_code, 200, {'Content-Type': 'application/javascript'}

if __name__ == '__main__':
    app.run()
