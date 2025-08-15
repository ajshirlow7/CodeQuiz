from quiz.models import Quiz, Question, Answer

# Create the quiz
quiz = Quiz.objects.create(
    title="CSS Fundamentals",
    description="Test your knowledge of CSS selectors, properties, and best practices."
)

# Define questions and answers
questions_data = [
    {
        "text": "Which of these are valid CSS units?",
        "answers": [
            ("px", True),
            ("em", True),
            ("rem", True),
            ("ptx", False),
        ]
    },
    {
        "text": "What are valid ways to apply CSS to an HTML page?",
        "answers": [
            ("External stylesheet via <link>", True),
            ("Internal stylesheet via <style>", True),
            ("Inline style using the style attribute", True),
            ("Using the css attribute on tags", False),
        ]
    },
    {
        "text": "Which of these are CSS pseudo-classes?",
        "answers": [
            (":hover", True),
            (":first-child", True),
            ("::before", False),  # ::before is pseudo-element, not pseudo-class
            (":nth-child(2)", True),
        ]
    },
    {
        "text": "Which of the following are CSS position values?",
        "answers": [
            ("static", True),
            ("relative", True),
            ("fixed", True),
            ("float", False),
        ]
    },
    {
        "text": "Which properties are used for CSS Flexbox layout?",
        "answers": [
            ("display: flex", True),
            ("justify-content", True),
            ("align-items", True),
            ("float", False),
        ]
    },
    {
        "text": "Which CSS selectors are valid?",
        "answers": [
            (".className", True),
            ("#idName", True),
            ("elementName", True),
            ("$special", False),
        ]
    },
    {
        "text": "Which of the following are valid values for the display property?",
        "answers": [
            ("block", True),
            ("inline", True),
            ("flex", True),
            ("visible", False),
        ]
    },
    {
        "text": "What are valid ways to include Google Fonts in a project?",
        "answers": [
            ("Using a <link> tag in the HTML head", True),
            ("Importing in CSS with @import", True),
            ("Uploading font files to the browser", False),
            ("Using the font-family property with the font name", True),
        ]
    },
    {
        "text": "Which of the following can be controlled using CSS?",
        "answers": [
            ("Text color", True),
            ("Background image", True),
            ("Element size", True),
            ("Database queries", False),
        ]
    },
    {
        "text": "Which are valid CSS pseudo-elements?",
        "answers": [
            ("::before", True),
            ("::after", True),
            ("::first-letter", True),
            (":hover", False),
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

print("✅ CSS quiz seeded successfully.")
