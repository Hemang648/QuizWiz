# QuizWiz
QuizWiz is an interactive command-line quiz game built in Python. Test your knowledge across various categories and difficulty levels with this engaging application.

## Features
* **Customizable Gameplay:** Choose the number of questions, difficulty level (Easy, Medium, Hard), and category to tailor the game to your preferences.

* **Wide Range of Categories:** Explore a diverse range of categories including General Knowledge, Science, History, and more.

* **Shuffled Options:** Keep each round exciting with shuffled answer options for every question.

* **Interactive Gameplay:** Answer questions by selecting the corresponding index, and receive immediate feedback on your choices.

* **Score Tracking:** Keep track of your performance with a point system, accumulating points for each correct answer.

* **Round-based Gameplay:** Play multiple rounds and track your scores for each round.

## Getting Started

### 1. Clone the repository to your local machine.
### 2. Install the required dependencies using pip install -r requirements.txt.
### 3. Run python quiz.py to start the game.
### 4. Follow the prompts to choose your game settings and begin playing.

## Requirements
* Python 3.x
* requests library (install via pip install requests)

## Libraries Used

### **requests**
* The "requests" library is used to make HTTP requests to the Open Trivia Database (opentdb.com) API, allowing QuizWiz to retrieve questions for the game dynamically.

### **html**
* The "html" library is used to decode HTML entities in the question text and answer options retrieved from the API, ensuring they are displayed correctly in the game.

### **random**
* The "random" library is used to shuffle the answer options for each question, adding variety and challenge to each round of the game.

## Additional Files

### **category.py**
* This file contains a function categories_list() that retrieves a list of available categories from the Open Trivia Database API. The function is called to display available categories to the user when selecting a category for the quiz.

### **ending.py**
* This file contains a function ending(score) that takes the player's score as input and returns a message based on their performance in the quiz round. The message varies depending on the score achieved, providing feedback to the player at the end of each round.

## Contributing

Contributions are welcome! If you'd like to contribute to QuizWiz, please follow these steps:

* Fork the repository.
* Create a new branch (git checkout -b feature/your-feature-name).
* Commit your changes (git commit -am 'Add new feature').
* Push to the branch (git push origin feature/your-feature-name).
* Create a new Pull Request.
