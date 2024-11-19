from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Class, Enrollment, db

teacher_blueprint = Blueprint('teacher', __name__)

@teacher_blueprint.route('/teacher/classes')
@login_required
def teacher_classes():
    classes = Class.query.filter_by(teacher_id=current_user.id).all()
    return render_template('teacher_classes.html', classes=classes)

@teacher_blueprint.route('/teacher/class/<int:class_id>')
@login_required
def class_details(class_id):
    cls = Class.query.get(class_id)
    students = Enrollment.query.filter_by(class_id=class_id).all()
    return render_template('class_details.html', cls=cls, students=students)

@teacher_blueprint.route('/teacher/grade/<int:enrollment_id>', methods=['POST'])
@login_required
def edit_grade(enrollment_id):
    enrollment = Enrollment.query.get(enrollment_id)
    if enrollment:
        enrollment.grade = request.form['grade']
        db.session.commit()
        flash('Grade updated successfully.')
    return redirect(url_for('teacher.class_details', class_id=enrollment.class_id))