from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from pymysql.constants import CLIENT
from dotenv import load_dotenv
import os


load_dotenv()

dburl = f"mysql+pymysql://{os.getenv("dbuser")}:{os.getenv("dbpassword")}@{os.getenv("dbhost")}:{os.getenv("dbport")}/{os.getenv("dbname")}"

engine = create_engine(dburl,connect_args= {"client_flag": CLIENT.MULTI_STATEMENTS})

session = sessionmaker(bind = engine)

db = session()

create_query = text("""
CREATE TABLE IF NOT EXISTS users (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    username VARCHAR(50) NOT NULL,
                    password VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL UNIQUE,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );

CREATE TABLE IF NOT EXISTS courses (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    title VARCHAR(100) NOT NULL,
                    level VARCHAR(100) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );

CREATE TABLE IF NOT EXISTS enrollments (
                    id INT PRIMARY KEY AUTO_INCREMENT,
                    user_id INT,
                    course_id INT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id),
                    FOREIGN KEY (course_id) REFERENCES courses(id)
                    );


""")
user = db.execute(create_query)
print("Tables created successfully")
