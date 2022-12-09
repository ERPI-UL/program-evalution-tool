from logging import NullHandler
from flask import Flask, request, url_for, render_template, flash
from app import app, models

ONTO_ID = 0 

@app.route('/', methods=['GET'])
def page_index():
    return render_template('index.html')

# Program pages

@app.route('/program/all', methods=['GET'])
def page_programs():
    programs = models.getProgrammes()
    return render_template('programs.html', programs= programs,)

@app.route('/program/<path:name>', methods=['GET'])
def page_program_detail(name):
    program = models.getProgram(name)
    return render_template('program_detail.html', program= program)

"""
@app.route('/program/<path:name>', methods=['GET','POST'])
def page_program_edit():
    return render_template('program_edit.html')"""

@app.route('/program/add', methods=['GET','POST'])
def page_add_program():
    return render_template('program_edit.html') 

# Indicators pages

@app.route('/indicators/all', methods=['GET'])
def page_all_indicators():
    indicators = models.getIndicators()
    print(indicators)
    return render_template('indicators_all.html', indicators = indicators )

@app.route('/indicators/stages', methods=['GET'])
def page_indicators_per_stage():
    return render_template('indicators_stages.html', )
"""
def page_indicators_per_stage():
    return render_template('indicators_stages.html', )

@app.route('/indicator/<path:name>', methods=['GET'])
def page_indicator_detail():
    return render_template('indicator_detail.html', )
"""
@app.route('/indicator/add', methods=['GET','POST'])
def page_indicator_add():
    return render_template('indicators_add.html', ) 