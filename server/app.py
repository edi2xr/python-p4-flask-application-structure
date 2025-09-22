from flask import Flask

app = Flask(__name__)

# Show what __name__ is when you run this file
print("__name__ is:", __name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'

# --- Demo: how to remove brackets and extract parameters ---
route = "<string:username>"
cleaned = route.strip("<>")  # remove < and >
param_type, param_name = cleaned.split(":")  # split into type and parameter
print("Route cleaned:", cleaned)       # string:username
print("Parameter type:", param_type)   # string
print("Parameter name:", param_name)   # username
# ------------------------------------------------------------

if __name__ == '__main__':
    app.run(port=5555, debug=True)
