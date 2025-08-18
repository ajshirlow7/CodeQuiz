# CodeQuiz 🖥️🐱

CodeQuiz is a fun and interactive web-based quiz platform designed to help learners sharpen their coding skills. It features quizzes on four core programming topics: HTML, CSS, JavaScript, and Python, covering essential concepts for both beginners and intermediate coders. Each quiz presents multiple-choice questions with four options, providing an engaging way to test knowledge, learn from mistakes, and track progress. With CodeQuiz, practicing programming becomes both educational and enjoyable, making it easy to build confidence and strengthen your coding foundation.

---

## Live Demo

A live version of the quiz can be found <a href="https://codequiz-49785f7e4e72.herokuapp.com/">here</a>.

---

## Table of Contents

- [Features](#features)  
- [User Stories](#user-stories)  
- [Design and Wireframes](#design)
- [Improvements](#improvements)  
- [Testing](#testing)  
- [Credits](#credits)  
- [Acknowledgments](#acknowledgments)  

---

## Features

### Quiz

The most important function of our site is our quiz. It is a multiple choice format quiz, where questions are displayed using inheritance, views, and models. </br>

```
                   <div class="mb-4">
                        <h5 style="color:#404E4D;">Question {{ current_q }} of {{ total_questions }}</h5>
                        <h5 style="color:#404E4D;">{{ question.question }}</h5>
                        {% for choice in question.choices %}
                        <div class="form-check">
                            <input class="form-check-input" type="radio" name="answer" id="choice{{ forloop.counter }}" value="{{ choice }}" required>
                            <label class="form-check-label" for="choice{{ forloop.counter }}">{{ choice }}</label>
                        </div>
                        {% endfor %}
                    </div>
```

### Accounts

In our user stories, we discussed adding the ability to register an account to save scores and add competition to our site. Using Django, we added a modal to the homepage where users have a choice to register a new account or log in to an existing account.

### Leaderboard

We also wanted to add a leaderboard to the project, which displays a user's chosen username, their rank, their scores for each quiz, and a total score. This functionality also utilises Python/Django.
```
                       {% for entry in entries %}
                        <tr>
                            <td>{{ forloop.counter }}</td>
                            <td>{{ entry.username }}</td>
                            <td>{{ entry.html_score }}</td>
                            <td>{{ entry.css_score }}</td>
                            <td>{{ entry.javascript_score }}</td>
                            <td>{{ entry.python_score }}</td>
                            <td>{{ entry.total_score }}</td>
                        </tr>
                        {% empty %}
```
---

## User Stories

A detailed view of our project board can be found <a href="https://github.com/users/ajshirlow7/projects/2">here</a>.
- As a site user, I want to take part in a quiz that tests my knowledge of specific programming languages. ✔️
- As a teacher, I want the quiz to be appealing to all ages. ✔️
- As a site user, I want to be able to register or log-in to save my scores. ✔️
- As a site user, I want to see how my scores compare to other site users. ✔️
- As a site user, I want to see my own scores so I can track my knowledge. ✔️

---

## Design

As the site was meant to appeal to all ages, we decided to use a <a href="https://coolors.co/5bc0eb-fde74c-9bc53d-c3423f-404e4d">cheerful and bright colour scheme</a>.
We also decided to use Bungee Shade for our titles and Lexend for our main body font, as Bungee Shade is eye-catching and playful in a way that matches the tone of the site, and Lexend is easy to read and casual.

As for the actual design of our site, we made a few rough drafts of what the quiz could look like. Once we decided on an idea, we developed our formal wireframes to base our site on:

![Phone Wireframe](/wireframes/Quiz-wirefreame-iphone.png)
![Tablet Wireframe](/wireframes/Quiz-wirefreame-ipad.png)
![Desktop Wireframe](/wireframes/Quiz-wirefreame-desktop.png)

---

## Improvements

Given more time, there are many other features we would like to add to our project. For example, we discussed adding more feedback in the form of explanations for correct answers, as well as immediate feedback in the form of user answers changing colour to reflect whether their choices were correct or incorrect. Using our registration system, we could implement question submissions, and related forums or discussion boards.</br>
Regarding the design of the site, we could implement colour-blind or dark modes to improve readability and access, as well as a toggle for different languages so we can attract even more users.</br>

---

## Testing

Python 3.9 was used for previews. </br>
The code was put through <a href="https://validator.w3.org/" target="_blank">HTML Validation</a> and 
<a href="https://jigsaw.w3.org/css-validator/" target="_blank">CSS Validation</a> and any flagged errors were fixed.

---

## Credits
Languages used: HTML, CSS, Python, Javascript </br>
Libraries/Frameworks used: Bootstrap5 and Django </br>
Version Control: Git and Github </br>
Hosting: Heroku </br>
AI was used in creating some quiz questions and troubleshooting. </br>
Colour palette was sourced using Coolors. </br>
Fonts were sourced from Google Fonts. </br>

---

## Acknowledgments

Made as a team for Code Institute's final Hackathon.
