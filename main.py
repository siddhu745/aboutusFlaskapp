from flask import Flask, render_template

app = Flask(__name__)

a = [
    {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    }, {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    }, {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    },
     {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    },
     {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    },
     {
        "name": "siddhu",
        "position": "softwareDev",
                    "description": "goodProgrammer",

    },
]


@app.route('/')
def hello():
    return render_template('aboutUs.html' , data = a)


if (__name__ == '__main__'):
    app.run(debug=True)
