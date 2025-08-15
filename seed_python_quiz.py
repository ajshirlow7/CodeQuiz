# coreflow/management/commands/seed_python_quiz.py

from django.core.management.base import BaseCommand
from core.models import Quiz, Question, Answer

class Command(BaseCommand):
    help = 'Seed the database with a Python quiz'

    def handle(self, *args, **kwargs):
        quiz, created = Quiz.objects.get_or_create(title="Python Basics")

        questions_data = [
            {
                "text": "Which of the following are valid Python data types?",
                "answers": [
                    ("int", True),
                    ("str", True),
                    ("list", True),
                    ("character", False),
                ],
            },
            {
                "text": "What is the output of print(type(3.14))?",
                "answers": [
                    ("<class 'float'>", True),
                    ("<class 'int'>", False),
                    ("<class 'decimal'>", False),
                    ("<class 'double'>", False),
                ],
            },
            {
                "text": "Which of these are valid ways to create a dictionary in Python?",
                "answers": [
                    ("dict()", True),
                    ("{}", True),
                    ("[]", False),
                    ("set()", False),
                ],
            },
            {
                "text": "What are valid ways to handle exceptions in Python?",
                "answers": [
                    ("try", True),
                    ("except", True),
                    ("finally", True),
                    ("catch", False),
                ],
            },
            {
                "text": "Which of the following are immutable in Python?",
                "answers": [
                    ("tuple", True),
                    ("str", True),
                    ("list", False),
                    ("dict", False),
                ],
            },
            {
                "text": "What are valid ways to define a function in Python?",
                "answers": [
                    ("def my_function():", True),
                    ("lambda x: x + 1", True),
                    ("function my_function():", False),
                    ("func my_function():", False),
                ],
            },
            {
                "text": "Which of the following are Python frameworks or libraries?",
                "answers": [
                    ("Django", True),
                    ("Flask", True),
                    ("NumPy", True),
                    ("Laravel", False),
                ],
            },
            {
                "text": "What are valid ways to import a module in Python?",
                "answers": [
                    ("import math", True),
                    ("from math import sqrt", True),
                    ("import math as m", True),
                    ("include math", False),
                ],
            },
            {
                "text": "Which of the following are true about Python lists?",
                "answers": [
                    ("They are mutable", True),
                    ("They can contain elements of different types", True),
                    ("They are immutable", False),
                    ("They are fixed in size", False),
                ],
            },
            {
                "text": "What are valid ways to reverse a list in Python?",
                "answers": [
                    ("list[::-1]", True),
                    ("reversed(list)", True),
                    ("list.reverse()", True),
                    ("list = list.reverse()", False),
                ],
            },
            {
                "text": "Which of the following are immutable types in Python?",
                "answers": [
                    ("tuple", True),
                    ("str", True),
                    ("list", False),
                    ("frozenset", True),
                ],
            },
            {
                "text": "Which statements about Python decorators are true?",
                "answers": [
                    ("They can modify a function’s behavior", True),
                    ("They are defined using @ syntax", True),
                    ("They can only be applied to class methods", False),
                    ("They must return a function", True),
                ],
            },
            {
                "text": "What are valid ways to iterate over a list in Python?",
                "answers": [
                    ("for item in my_list:", True),
                    ("while i < len(my_list):", True),
                    ("list comprehension", True),
                    ("foreach(item in my_list)", False),
                ],
            },
            {
                "text": "Which of these are valid ways to create a dictionary?",
                "answers": [
                    ("dict(a=1, b=2)", True),
                    ("{'a': 1, 'b': 2}", True),
                    ("dict([('a', 1), ('b', 2)])", True),
                    ("dict('a'=1, 'b'=2)", False),
                ],
            },
            {
                "text": "Which of the following raise a TypeError?",
                "answers": [
                    ("len(42)", True),
                    ("'abc' + 5", True),
                    ("None + None", True),
                    ("int('42')", False),
                ],
            },
            {
                "text": "Which are valid ways to handle exceptions in Python?",
                "answers": [
                    ("try/except", True),
                    ("try/finally", True),
                    ("try/except/finally", True),
                    ("catch/except", False),
                ],
            },
            {
                "text": "Which of these are valid Python set operations?",
                "answers": [
                    ("set1 | set2", True),
                    ("set1 & set2", True),
                    ("set1 - set2", True),
                    ("set1 + set2", False),
                ],
            },
            {
                "text": "Which of the following are true about Python’s with statement?",
                "answers": [
                    ("It simplifies resource management", True),
                    ("It requires the object to implement __enter__ and __exit__", True),
                    ("It can be used with file operations", True),
                    ("It automatically retries failed operations", False),
                ],
            },
            {
                "text": "Which of these are valid ways to define a function in Python?",
                "answers": [
                    ("def func(): pass", True),
                    ("lambda x: x + 1", True),
                    ("function func() {}", False),
                    ("def func(x): return x * 2", True),
                ],
            },
            {
                "text": "Which of these are Python built-in functions?",
                "answers": [
                    ("enumerate()", True),
                    ("map()", True),
                    ("filter()", True),
                    ("select()", False),
                ],
            },           
        ]

        for q_data in questions_data:
            question = Question.objects.create(quiz=quiz, text=q_data["text"])
            for answer_text, is_correct in q_data["answers"]:
                Answer.objects.create(question=question, text=answer_text, is_correct=is_correct)

        self.stdout.write(self.style.SUCCESS("✅ Python quiz seeded successfully!"))
        