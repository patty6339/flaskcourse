from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    mylist = [1, 2, 3, 4, 5]
    return render_template(template_name_or_list='index.html', mylist=mylist)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    