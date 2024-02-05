from django.test import TestCase
from django.contrib.auth.models import User
from .models import Subject,Course,Module,Content
import datetime 
from django.urls import reverse
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

    def test_module_title(self):
        module = Module.objects.get(id=1)
        self.assertEqual(module.title, "Bugaguga")    

    def test_slave_checker_slug(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.subject.slug, "slaveteacher")    

    def test_slave_completer(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.owner.username, "john")

    def test_slave_dater(self):
        course = Course.objects.get(id=1)   
        self.assertEqual(course.created.date(), self.today)

    def test_module_course(self):
        module = Module.objects.get(id=1)
        self.assertEqual(module.course.title, "Ugabuga")    

    def test_module_exists(self):
        self.assertTrue(Module.objects.filter(title="Bugaguga").exists())

    def test_module_does_not_exist(self):
        self.assertFalse(Module.objects.filter(title="Nonexistent").exists())
        
# User объект создан с правильными атрибутами
    def test_user_creation(self):
        user = User.objects.get(username='john')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'jlennon@beatles.com')

# Course объект связан с правильными Subject объектами User
    def test_course_relationships(self):
        course = Course.objects.get(id=1)
        self.assertEqual(course.subject.title, "SlaveTeacher")
        self.assertEqual(course.owner.username, "john")

# Изменение Course объекта и проверка отражения изменения в базе данных.
    def test_course_modification(self):
        course = Course.objects.get(id=1)
        course.title = "UpdatedTitle"
        course.save()
        updated_course = Course.objects.get(id=1)
        self.assertEqual(updated_course.title, "UpdatedTitle")

# Создание нового Module и проверка его существования в базе данных. 
    def test_module_creation(self):
        module = Module.objects.create(
        course=Course.objects.get(id=1),
        title="NewModule"
    )
        self.assertIsNotNone(Module.objects.filter(title="NewModule").first())