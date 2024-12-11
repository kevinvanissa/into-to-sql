import MySQLdb  # This is from mysqlclient, so this need to be installed using: pip install mysqlclient
from faker import Faker
import random


fake = Faker()


#  REPLACE VARIABLES BELOW
conn = MySQLdb.connect(
    host="localhost", 
    user="root",       
    passwd="pp08763547*T", 
    db="my_quiz_db"       
)

cursor = conn.cursor()

# Helper function to generate users (without user_id for now)
def generate_users(n):
    users = []
    for _ in range(n):
        username = fake.user_name()
        email = fake.email()
        password_hash = fake.sha256()  # Fake password hash
        created_at = fake.date_this_decade()  # Fake created date
        users.append((username, email, password_hash, created_at))
    return users

# Helper function to generate quizzes
def generate_quizzes(user_ids, n):
    quizzes = []
    for _ in range(n):
        user_id = random.choice(user_ids)  # Randomly select a user_id 
        title = fake.sentence(nb_words=4)
        description = fake.text(max_nb_chars=200)
        created_at = fake.date_this_decade()
        quizzes.append((user_id, title, description, created_at))
    return quizzes

# Helper function to generate questions for quizzes
def generate_questions(quiz_ids, n):
    questions = []
    for _ in range(n):
        quiz_id = random.choice(quiz_ids)  # Random quiz_id
        question_text = fake.sentence(nb_words=10)
        correct_answer = fake.word()
        created_at = fake.date_this_decade()
        questions.append((quiz_id, question_text, correct_answer, created_at))
    return questions

# Helper function to generate answers for users' quiz attempts
def generate_user_quiz_questions(user_ids, quiz_ids, question_ids, n):
    user_quiz_questions = []
    used_combinations = set()  # To track used (user_id, quiz_id, question_id) combinations
    for _ in range(n):
        while True:
            user_id = random.choice(user_ids)  # Random user_id
            quiz_id = random.choice(quiz_ids)  # Random quiz_id
            question_id = random.choice(question_ids)  # Random question_id
            
            # Check if the combination already exists
            combination = (user_id, quiz_id, question_id)
            if combination not in used_combinations:
                used_combinations.add(combination)  # Mark the combination as used
                user_answer = fake.word()  # Fake user's answer
                score = random.choice([0,1,3,5])
                answered_at = fake.date_this_decade()
                user_quiz_questions.append((user_id, quiz_id, question_id, user_answer, score, answered_at))
                break  # Exit while loop and continue to next entry
    return user_quiz_questions

# Insert Users into the Users table
users_data = generate_users(10)
cursor.executemany("""
    INSERT INTO Users (username, email, password_hash, created_at)
    VALUES (%s, %s, %s, %s)
""", users_data)
conn.commit()

# Fetch the user IDs from the database after inserting
cursor.execute("SELECT user_id FROM Users")
user_ids = cursor.fetchall()

# Now we have the list of user_ids (as integers)
user_ids = [user[0] for user in user_ids]  # Extract user_id values from the result tuples

# Insert Quizzes into the Quizzes table (using the correct user_id from the user_ids list)
quizzes_data = generate_quizzes(user_ids, 5)
cursor.executemany("""
    INSERT INTO Quizzes (user_id, title, description, created_at)
    VALUES (%s, %s, %s, %s)
""", quizzes_data)
conn.commit()

# Fetch the quiz IDs from the database after inserting
cursor.execute("SELECT quiz_id FROM Quizzes")
quiz_ids = cursor.fetchall()

# Now we have the list of quiz_ids (as integers)
quiz_ids = [quiz[0] for quiz in quiz_ids]  # Extract quiz_id values from the result tuples

# Insert Questions into the Questions table (using the quiz_id from the quiz_ids list)
questions_data = generate_questions(quiz_ids, 20)
cursor.executemany("""
    INSERT INTO Questions (quiz_id, question_text, correct_answer, created_at)
    VALUES (%s, %s, %s, %s)
""", questions_data)
conn.commit()

# Fetch the question IDs from the database after inserting
cursor.execute("SELECT question_id FROM Questions")
question_ids = cursor.fetchall()

# Now we have the list of question_ids (as integers)
question_ids = [question[0] for question in question_ids]  # Extract question_id values from the result tuples

# Insert UserQuizQuestions into the UserQuizQuestions table (using the user_id, quiz_id, and question_id)
user_quiz_questions_data = generate_user_quiz_questions(user_ids, quiz_ids, question_ids, 30)
cursor.executemany("""
    INSERT INTO UserQuizQuestions (user_id, quiz_id, question_id, user_answer, score, answered_at)
    VALUES (%s, %s, %s, %s, %s, %s)
""", user_quiz_questions_data)
conn.commit()

# Close the connection
cursor.close()
conn.close()

print("Data has been populated successfully :-)")

