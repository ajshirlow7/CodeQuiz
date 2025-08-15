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
{
        "text": "Which of the following are valid ways to declare an arrow function?",
        "tags": ["javascript"],
        "answers": [
            {"text": "const add = (a, b) => a + b", "is_correct": True},
            {"text": "let greet = () => \"Hello\"", "is_correct": True},
            {"text": "function => ()", "is_correct": False},
            {"text": "arrow function() => {}", "is_correct": False},
        ],
    },
    {
        "text": "What are valid uses of the typeof operator?",
        "tags": ["javascript"],
        "answers": [
            {"text": "typeof \"hello\" returns \"string\"", "is_correct": True},
            {"text": "typeof 42 returns \"number\"", "is_correct": True},
            {"text": "typeof null returns \"null\"", "is_correct": False},
            {"text": "typeof undefined returns \"null\"", "is_correct": False},
        ],
    },
    {
        "text": "Which of these are valid JavaScript loop types?",
        "tags": ["javascript"],
        "answers": [
            {"text": "for", "is_correct": True},
            {"text": "while", "is_correct": True},
            {"text": "do...while", "is_correct": True},
            {"text": "loop...until", "is_correct": False},
        ],
    },
    {
        "text": "What are valid ways to prevent default form submission in JavaScript?",
        "tags": ["javascript"],
        "answers": [
            {"text": "event.preventDefault()", "is_correct": True},
            {"text": "return false", "is_correct": True},
            {"text": "event.stopPropagation()", "is_correct": False},
            {"text": "form.cancel()", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following are valid JavaScript string methods?",
        "tags": ["javascript"],
        "answers": [
            {"text": ".slice()", "is_correct": True},
            {"text": ".toUpperCase()", "is_correct": True},
            {"text": ".includes()", "is_correct": True},
            {"text": ".splitBy()", "is_correct": False},
        ],
    },
    {
        "text": "Which of these are valid ways to define an object in JavaScript?",
        "tags": ["javascript"],
        "answers": [
            {"text": "const obj = { key: \"value\" }", "is_correct": True},
            {"text": "let user = new Object()", "is_correct": True},
            {"text": "object user = {}", "is_correct": False},
            {"text": "define obj = {}", "is_correct": False},
        ],
    },
    {
        "text": "What are valid ways to convert a string to a number in JavaScript?",
        "tags": ["javascript"],
        "answers": [
            {"text": "parseInt(\"42\")", "is_correct": True},
            {"text": "Number(\"3.14\")", "is_correct": True},
            {"text": "+\"100\"", "is_correct": True},
            {"text": "int(\"42\")", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following are valid array methods in JavaScript?",
        "tags": ["javascript"],
        "answers": [
            {"text": ".push()", "is_correct": True},
            {"text": ".pop()", "is_correct": True},
            {"text": ".splice()", "is_correct": True},
            {"text": ".remove()", "is_correct": False},
        ],
    },
    {
        "text": "What are valid ways to check if a variable is undefined?",
        "tags": ["javascript"],
        "answers": [
            {"text": "typeof x === \"undefined\"", "is_correct": True},
            {"text": "x === undefined", "is_correct": True},
            {"text": "x == null", "is_correct": False},
            {"text": "x = undefined", "is_correct": False},
        ],
    },
    {
        "text": "Which of the following are valid ways to write conditional logic in JavaScript?",
        "tags": ["javascript"],
        "answers": [
            {"text": "if (x > 0) { ... }", "is_correct": True},
            {"text": "x > 0 ? \"yes\" : \"no\"", "is_correct": True},
            {"text": "switch(x) { case 1: ... }", "is_correct": True},
            {"text": "when x > 0 then ...", "is_correct": False},
        ],
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





    