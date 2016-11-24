#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from lagouApi import LagouAPI

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///job.data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


@app.route('/', methods=['GET'])
def index():
    '''
    for job_json in LagouAPI.search_job('c++', city='杭州', gx='全职'):
        job = Job(positionName=job_json['positionName'], city=job_json['city'],
                  companyFullName=job_json['companyFullName'])
        db.session.add(job)
        db.session.commit()
    '''
    jobs = Job.query.all()
    return render_template('index.html', jobs=jobs)


class Job(db.Model):
    __tablename__ = 'job'
    id = db.Column(db.Integer, primary_key=True)
    positionName = db.Column(db.String(50))
    city = db.Column(db.String(20))
    wokerYear = db.Column(db.String(20))
    companyFullName = db.Column(db.String(30))

    def __repr__(self):
        return 'positionName:{0}, companyName{1}'.format(self.positionName, self.companyFullName)


if __name__ == '__main__':
    app.run(debug=True)

