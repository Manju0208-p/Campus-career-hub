# Campus Career Hub

A professional Django-based campus career portal connecting students with internships, jobs and referrals.

## Main modules
- Student and recruiter authentication
- Student profile with skills and resume upload
- Recruiter/company profile
- Opportunity posting, editing and deletion
- Search and filtering
- Student applications with duplicate prevention
- Application status tracking
- Recruiter applicant management
- Skill-based opportunity matching
- Responsive Bootstrap UI
- Django admin

## Requirements
- Python 3.10+
- Django 4.2.x

## Run
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
# source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo
python manage.py createsuperuser
python manage.py runserver
```
Open http://127.0.0.1:8000/

### Demo accounts
Student: `student_demo` / `Student@123`
Recruiter: `recruiter_demo` / `Recruiter@123`

## Project flow
Student -> Register -> Profile -> Browse/Recommended Opportunities -> Apply -> Track Status.
Recruiter -> Register -> Company Profile -> Post Opportunity -> View Applicants -> Update Status.
Admin -> /admin/ -> Manage users, profiles, opportunities and applications.

## Notes
The original project structure was retained and completed. SQLite is used for local development. Change `SECRET_KEY` and `DEBUG` before production deployment.
