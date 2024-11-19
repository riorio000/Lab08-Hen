from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.models import Class, Enrollment, db

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/student/classes')
@login_required
def view_classes():
    offered_classes = Class.query.all()
    student_classes = Enrollment.query.filter_by(student_id=current_user.id).all()
    return render_template('student_classes.html', offered_classes=offered_classes, student_classes=student_classes)

@student_blueprint.route('/student/enroll/<int:class_id>')
@login_required
def enroll_class(class_id):
    cls = Class.query.get(class_id)
    if cls and Enrollment.query.filter_by(student_id=current_user.id, class_id=class_id).first() is None:
        if Enrollment.query.filter_by(class_id=class_id).count() < cls.max_capacity:
            enrollment = Enrollment(student_id=current_user.id, class_id=class_id)
            db.session.add(enrollment)
            db.session.commit()
            flash('Enrolled successfully!')
        else:
            flash('Class is at maximum capacity.')
    return redirect(url_for('student.view_classes'))