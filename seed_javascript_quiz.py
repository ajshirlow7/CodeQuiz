from quiz.models import Quiz, Question, Answer

# Create the quiz
quiz = Quiz.objects.create(
    title="JavaScript Fundamentals",
    description="Test your knowledge of JavaScript basics, syntax, and behavior."
)

# Define questions and answers
questions_data = [
    {
        "text": "Which of the following are primitive data types in JavaScript?",
        "answers": [
            ("String", True),
            ("Number", True),
            ("Boolean", True),
            ("Object", False),
        ]
    },
    {
        "text": "What does === do in JavaScript?",
        "answers": [
            ("Compares both value and type", True),
            ("Converts types before comparing", False),
            ("Returns true only if both operands are strictly equal", True),
            ("Assigns a value", False),
        ]
    },
    {
        "text": "Which methods can be used to iterate over an array?",
        "answers": [
            ("forEach()", True),
            ("map()", True),
            ("filter()", True),
            ("reduceRight()", False),
        ]
    },
    {
        "text": "What are valid ways to declare a variable in JavaScript?",
        "answers": [
            ("let", True),
            ("const", True),
            ("var", True),
            ("define", False),
        ]
    },
    {
        "text": "Which of the following are falsy values in JavaScript?",
        "answers": [
            ("0", True),
            ('""', True),
            ("null", True),
            ('"false"', False),
        ]
    },
    {
        "text": "What does the this keyword refer to in JavaScript?",
        "answers": [
            ("The object that owns the method", True),
            ("The global object in non-strict mode", True),
            ("Always the window object", False),
            ("The parent function", False),
        ]
    },
    {
        "text": "Which of these are JavaScript frameworks or libraries?",
        "answers": [
            ("React", True),
            ("Vue", True),
            ("Angular", True),
            ("Django", False),
        ]
    },
    {
        "text": "What are valid ways to define a function in JavaScript?",
        "answers": [
            ("Function declaration (function foo() {})", True),
            ("Function expression (const foo = function() {})", True),
            ("Arrow function (const foo = () => {})", True),
            ("def foo():", False),
        ]
    },
    {
        "text": "Which of the following are true about async/await?",
        "answers": [
            ("await can only be used inside async functions", True),
            ("It simplifies working with Promises", True),
            ("It blocks the main thread", False),
            ("It makes asynchronous code look synchronous", True),
        ]
    },
    {
        "text": "What are common uses of JavaScript in web development?",
        "answers": [
            ("DOM manipulation", True),
            ("Form validation", True),
            ("Handling user events", True),
            ("Server-side rendering (unless using Node.js)", False),
        ]
    },
]

# Create questions and answers
for i, q_data in enumerate(questions_data, start=1):
    question = Question.objects.create(
        quiz=quiz,
        text=q_data["text"],
        order=i
    )
    for answer_text, is_correct in q_data["answers"]:
        Answer.objects.create(
            question=question,
            text=answer_text,
            is_correct=is_correct
        )

print("✅ JavaScript quiz seeded successfully.")