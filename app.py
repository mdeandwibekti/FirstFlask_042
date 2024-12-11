from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    biodata = {}
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        address = request.form.get('address')
        biodata = {
            'name': name,
            'age': age,
            'address': address
        }
    return render_template('index.html', biodata=biodata)

if __name__ == '__main__':
    app.run(debug=True)