
# Students Directory

A Django-based platform enabling schools to create detailed student profiles that can be easily accessed using QR codes. This system allows schools to showcase student achievements, academic progress, and other relevant information in a centralized and user-friendly format.

## Features
- **Student Directory with QR Codes**: Each student's profile is accessible via a unique QR code, making it easy for anyone to view the profile directly.
- **Comprehensive Student Profiles**: Profiles include sections for interests, contact information, birthdays, profile pictures, and links to social media accounts.
- **School Branding Customization**: Schools can personalize the platform by adjusting theme colors, uploading a custom logo, and maintaining a consistent school identity.
- **User-Friendly Interface**: Designed for easy navigation, enabling users to browse, search, and access profiles effortlessly.
- **Admin Dashboard**: Simple interface for schools to manage student data, update profiles, and monitor public access.
## Installation

Install Students-Directory using pip & django-admin

```bash
python3 -m pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
```

## Deployment 

To deploy this project you can either use `runserver` directly, or if you're on Passenger you can just leave `passenger_wsgi.py` as it is
You will need to setup Environment variables first, `DJANGO_KEY` and `PYTHON_INTERPRETER` if you're on Passenger
```bash
python3 manage.py runserver
```


## Demo (Coming soon)

You will find a demo at https://alhennawi.tech/students-directory

