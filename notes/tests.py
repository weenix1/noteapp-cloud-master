from django.test import TestCase, testcases
from notes.models import Note
import time
from datetime import date, timedelta
import datetime 
class NoteTestCase(TestCase):


    def setUp(self):
        Note.objects.create(title="testTitle", content="testContent")
        Note.objects.create(title="testTitle1", content="testContent1", created_at="2021-05-21")
        Note.objects.create(title="testTitle2", content="testContent2", created_at="2021-05-20", modified_at="2021-05-21")
        Note.objects.create(title="testTitle3", content="testContent3", created_at="2021-05-20", modified_at="2021-05-20")
        Note.objects.create(title="testTitle4")

        

    def test_notes_have_title(self):
        testTitle = Note.objects.get(title="testTitle")
        self.assertIsNotNone(testTitle.title)
        self.assertIsNotNone(testTitle.content)
        self.assertEqual(testTitle.title,"testTitle")
        self.assertIsNot(testTitle.title,"andererTitel")


    def test_notes_have_content(self):
        testTitle = Note.objects.get(content="testContent")
        self.assertIsNotNone(testTitle.title)
        self.assertIsNotNone(testTitle.content)
        self.assertEqual(testTitle.content,"testContent")
        self.assertIsNot(testTitle.content,"andererContent")

    def test_notes_have_title_and_nocontent(self):
        testTitle = Note.objects.get(title="testTitle4")
        self.assertEqual(testTitle.title,"testTitle4")
        self.assertIsNone(testTitle.content)
        self.assertIsNotNone(testTitle.created_at)
        self.assertIsNotNone(testTitle.modified_at)


    def test_notes_have_created_at(self):
        datetime_object = date.today()
        testTitle1 = Note.objects.get(title="testTitle1")
        self.assertIsNotNone(testTitle1.created_at)
        self.assertIsNotNone(testTitle1.modified_at)
        self.assertEqual(testTitle1.created_at, datetime_object)


    def test_notes_have_modified_at(self):
        date_modified_at = date.today()
        testTitle2 = Note.objects.get(title="testTitle2")
        self.assertIsNotNone(testTitle2.modified_at)
        self.assertEqual(testTitle2.modified_at, date_modified_at)


    def test_notes_have_all_attributes(self):
        date_modified_at = date.today()
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days = 0)
        testTitle3 = Note.objects.get(title="testTitle3")
        self.assertEqual(testTitle3.title, "testTitle3")
        self.assertEqual(testTitle3.content, "testContent3")
        self.assertEqual(testTitle3.created_at, yesterday)
        self.assertEqual(testTitle3.modified_at, date_modified_at)
