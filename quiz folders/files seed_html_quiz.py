from quiz.models import Quiz, Question, Answer

# Create the quiz
quiz = Quiz.objects.create(
    title="HTML Fundamentals",
    description="Test your knowledge of HTML structure, elements, and attributes."
)

# Define questions and answers
questions_data = [
    {
        "text": "Which of the following are semantic HTML elements?",
        "answers": [
            ("<header>", True),
            ("<footer>", True),
            ("<section>", True),
            ("<div>", False),
        ]
    },
    {
        "text": "What does the <alt> attribute in an <img> tag do?",
        "answers": [
            ("Provides alternative text for the image", True),
            ("Specifies the image size", False),
            ("Is required for accessibility", True),
            ("Changes the image format", False),
        ]
    },
    {
        "text": "Which of these elements are used for creating lists in HTML?",
        "answers": [
            ("<ul>", True),
            ("<ol>", True),
            ("<li>", True),
            ("<list>", False),
        ]
    },
    {
        "text": "What are valid values for the target attribute in an <a> tag?",
        "answers": [
            ("_blank", True),
            ("_self", True),
            ("_parent", True),
            ("_page", False),
        ]
    },
    {
        "text": "Which tags are considered empty elements in HTML?",
        "answers": [
            ("<br>", True),
            ("<img>", True),
            ("<input>", True),
            ("<p>", False),
        ]
    },
    {
        "text": "What are the correct ways to define a table in HTML?",
        "answers": [
            ("Using <table>, <tr>, and <td>", True),
            ("Using <thead>, <tbody>, and <tfoot>", True),
            ("Using <grid> and <cell>", False),
            ("Nesting <tr> inside <table>", True),
        ]
    },
    {
        "text": "Which of these are global HTML attributes?",
        "answers": [
            ("id", True),
            ("class", True),
            ("style", True),
            ("border", False),
        ]
    },
    {
        "text": "What are correct uses of the <form> element in HTML?",
        "answers": [
            ("To collect user input", True),
            ("To send data to a server", True),
            ("To display images", False),
            ("To define input fields", True),
        ]
    },
    {
        "text": "Which attributes can be used with the <input> tag?",
        "answers": [
            ("type", True),
            ("name", True),
            ("value", True),
            ("href", False),
        ]
    },
    {
        "text": "What are best practices for HTML headings (<h1> to <h6>)?",
        "answers": [
            ("Use only one <h1> per page for main title", True),
            ("Use headings in a logical order", True),
            ("Skip heading levels for styling purposes", False),
            ("Headings help with accessibility and SEO", True),
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

print("✅ HTML quiz seeded successfully.")
