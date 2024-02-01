from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subject,Course,Module,Content
import datetime 
# Create your tests here.

class SlaveTestCase(TestCase):
    def setUp(self):
        sl_kw = {"title": "SlaveTeacher", "slug":"slaveteacher"}
        Subject.objects.create(**sl_kw)
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        pr_kw = {
            "owner": User.objects.get(id=1),
            "subject": Subject.objects.get(id=1),
            "title": "Ugabuga",
            "slug": "ugabuga",
            "overview": "ugabuga crying",
        }
        Course.objects.create(**pr_kw)
        md_kw = {
            "course": Course.objects.get(id=1),
            "title": "Bugaguga",
        }
        Module.objects.create(**md_kw)
        self.today = datetime.date.today()
    def test_slave_checker(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.subject.title, "SlaveTeacher")
    def test_slave_completer(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.owner.username, "john")
    def test_slave_dater(self):
        course = Course.objects.get(id=1)   
        self.assertEqual(course.created.date(), self.today)
