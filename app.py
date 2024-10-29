from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///health_tips.db'
db = SQLAlchemy(app)

class HealthTip(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    health_tips = HealthTip.query.all()
    return render_template('index.html', health_tips=health_tips)

@app.route('/add', methods=['GET', 'POST'])
def add_tip():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category = request.form['category']
        new_tip = HealthTip(title=title, content=content, category=category)
        db.session.add(new_tip)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_tip.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

print("Flask app is ready to run!")
