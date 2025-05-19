import os

from flask import Flask, send_file, render_template

app = Flask(__name__, template_folder="src")

posts = [
        {
            "title": "My cat sleeping in a box",
            "content": "Look how silly he looks!",
            "image": "cat1.jpg"
        },
        {
            "title": "Caught in the act!",
            "content": "He knows he's not allowed on the counter.",
            "image": "cat2.jpg"
        },
        {
            "title": "Freaky cat",
            "content": "He loves to be freaky",
            "image": "https://www.google.com/imgres?q=freaky%20cat%20img&imgurl=https%3A%2F%2Flookaside.instagram.com%2Fseo%2Fgoogle_widget%2Fcrawler%2F%3Fmedia_id%3D3635423491840779929&imgrefurl=https%3A%2F%2Fwww.instagram.com%2Fsillyanimalspost%2Fp%2FDJznmePR5Ql%2F&docid=6sPQb8kQCHT6yM&tbnid=Ljj7GowBCRxRPM&vet=12ahUKEwi5rLyylq-NAxXQnf0HHQysALcQM3oECEoQAA..i&w=1440&h=1440&hcb=2&ved=2ahUKEwi5rLyylq-NAxXQnf0HHQysALcQM3oECEoQAA"
        }
    ]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
