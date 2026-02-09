from flask import Flask, jsonify, render_template,request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('HomePage.html')

@app.get('/holidays')
def create_table():

    with open('file.json', 'r')as file:
        holidays = json.load(file)

    return render_template('TablePage.html', data=holidays)

@app.get('/holidays/add')
def add_holiday_page():
    return render_template('AddHolidayPage.html')

@app.post('/holidays')
def add_holiday_to_file():
    holiday_name = request.form.get('holidayName')
    holiday_start_date = request.form.get('startDate')
    holiday_end_date = request.form.get('endDate')

    new_holiday = {
        'holidayName': holiday_name,
        'startDate': holiday_start_date,
        'endDate': holiday_end_date
    }

    with open('file.json','r')as file:
        holidays = json.load(file)

    holidays.append(new_holiday)

    with open('file.json','w') as file:
        json.dump(holidays,file,indent=4)
    
    return redirect(url_for('create_table'))

@app.get('/remove/holiday')
def remove_holiday_page():
    with open('file.json', 'r')as file:
        holidays = json.load(file)

    return render_template('RemoveHoliday.html', data = holidays)

@app.post('/remove/holiday')
def remove_holiday():
    holiday_name = request.form.get('holidayName')
    holiday_start_date = request.form.get('startDate')
    holiday_end_date = request.form.get('endDate')

    old_data = {
        'holidayName': holiday_name,
        'startDate': holiday_start_date,
        'endDate': holiday_end_date
    }

    with open ('file.json', 'r') as file:
        holidays = json.load(file)
    
    if old_data not in holidays:
        return "Data not in Holidays"
    
    holidays.remove(old_data)

    with open('file.json', 'w') as file:
        json.dump(holidays, file, indent = 4)
        return redirect(url_for('create_table'))
    
    


    
if __name__ == '__main__':
    app.run(debug=True)

