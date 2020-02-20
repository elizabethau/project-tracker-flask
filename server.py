"""A web application for tracking projects, students, and student grades."""

from flask import Flask, request, render_template
import hackbright

app = Flask(__name__)


@app.route('/student')
def get_student():
    """Show information about a student."""

    github = request.args.get('github')

    first, last, github = hackbright.get_student_by_github(github)

    return render_template('student_info.html',
                           first_name=first,
                           last_name=last,
                           github_user=github)


@app.route('/search')
def get_search():

    return render_template('student_search.html')


@app.route('/student-add', methods=['POST'])
def add_student():

    first = request.form.get('first')
    last = request.form.get('last')
    github = request.form.get('github')

    print(first)

    hackbright.make_new_student(first, last, github)

    return render_template('add_student.html')

@app.route('/confirmation')
def confirmation():

    return render_template('confirmation.html')


if __name__ == '__main__':
    hackbright.connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')
