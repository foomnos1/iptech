from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

appointments = []

@app.route('/')
def intro():
    return render_template('introduction.html')


@app.route('/appointment', methods=['GET', 'POST'])
def appointment_page():
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        time = request.form.get('time')
        purpose = request.form.get('purpose')

        new_appointment = {
            'name': name,
            'date': date,
            'time': time,
            'purpose': purpose
        }

        appointments.append(new_appointment)
        return redirect(url_for('appointment_page'))

    return render_template('appointment.html', appointments=appointments)

@app.route('/edit', methods=['POST'])
def edit_page():
    index = int(request.form.get('index'))
    if 0 <= index < len(appointments): 
        return render_template('edit_appointment.html', appointment=appointments[index], index=index)
    return "Appointment not found", 404

@app.route('/update', methods=['POST'])
def update_appointment():
    index = int(request.form.get('index'))

    if 0 <= index < len(appointments):
        appointments[index]['name'] = request.form.get('name')
        appointments[index]['date'] = request.form.get('date')
        appointments[index]['time'] = request.form.get('time')
        appointments[index]['purpose'] = request.form.get('purpose')

    return redirect(url_for('appointment_page'))

@app.route('/delete', methods=['POST'])
def delete_appointment():
    index = int(request.form.get('index'))
    if 0 <= index < len(appointments):
        appointments.pop(index)
    return redirect(url_for('appointment_page'))

if __name__ == '__main__':
    app.run()

# changes