import flask
from application import db
# from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Document):
    user_id     =   db.IntField( unique=True )
    first_name  =   db.StringField( max_length=50 )
    last_name   =   db.StringField( max_length=50 )
    email       =   db.StringField( max_length=30, unique=True )
    password    =   db.StringField( )

    # def set_password(self, password):
    #     self.password = generate_password_hash(password)

    # def get_password(self, password):
    #     return check_password_hash(self.password, password)    

class Course(db.Document):
    courseID    =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )

class Enrollment(db.Document):
    user_id     =   db.IntField()
    courseID    =   db.StringField( max_length=10 )

class Comp_cards1(db.Document):
    quiz_id     =   db.StringField( max_length=10 )
    url         =   db.StringField( max_length=40 )
    quiz_title  =   db.StringField( max_length=40 )


    question1  =   db.StringField( max_length=3 )
    q1 =   db.StringField( max_length=1 )
    a  =   db.StringField( max_length=50 )
    b  =   db.StringField( max_length=50 )
    c  =   db.StringField( max_length=50 )
    answer1 =   db.StringField( max_length=1 )

    question2  =   db.StringField( max_length=3 )
    q2 =   db.StringField( max_length=1 )
    d  =   db.StringField( max_length=50 )
    e  =   db.StringField( max_length=50 )
    f  =   db.StringField( max_length=50 )
    answer2 =   db.StringField( max_length=1 )

    question3  =   db.StringField( max_length=3 )
    q3 =   db.StringField( max_length=1 )
    g  =   db.StringField( max_length=50 )
    h  =   db.StringField( max_length=50 )
    i  =   db.StringField( max_length=50 )
    answer3 =   db.StringField( max_length=1 )

    question4  =   db.StringField( max_length=3 )
    q4 =   db.StringField( max_length=1 )
    j  =   db.StringField( max_length=50 )
    k  =   db.StringField( max_length=50 )
    l  =   db.StringField( max_length=50 )
    answer4 =   db.StringField( max_length=1 )

    question5  =   db.StringField( max_length=3 )
    q5 =   db.StringField( max_length=1 )
    m  =   db.StringField( max_length=50 )
    n  =   db.StringField( max_length=50 )
    o  =   db.StringField( max_length=50 )
    answer5 =   db.StringField( max_length=1 )

class Word_problems(db.Document):
    quiz_id     =   db.StringField( max_length=10 )
    table_name  =   db.StringField( max_length=10 )
    quiz_level  =   db.StringField( max_length=1 )
    url         =   db.StringField( max_length=40 )
    quiz_title  =   db.StringField( max_length=40 )


    question1  =   db.StringField( max_length=3 )
    q1 =   db.StringField( max_length=1 )
    a  =   db.StringField( max_length=50 )
    b  =   db.StringField( max_length=50 )
    c  =   db.StringField( max_length=50 )
    d  =   db.StringField( max_length=50 )
    answer1 =   db.StringField( max_length=1 )

    question2  =   db.StringField( max_length=3 )
    q2 =   db.StringField( max_length=1 )
    e  =   db.StringField( max_length=50 )
    f  =   db.StringField( max_length=50 )
    g  =   db.StringField( max_length=50 )
    h  =   db.StringField( max_length=50 )
    answer2 =   db.StringField( max_length=1 )

    question3  =   db.StringField( max_length=3 )
    q3 =   db.StringField( max_length=1 )
    i  =   db.StringField( max_length=50 )
    j  =   db.StringField( max_length=50 )
    k  =   db.StringField( max_length=50 )
    l  =   db.StringField( max_length=50 )
    answer3 =   db.StringField( max_length=1 )

    question4  =   db.StringField( max_length=3 )
    q4 =   db.StringField( max_length=1 )
    m  =   db.StringField( max_length=50 )
    n  =   db.StringField( max_length=50 )
    o  =   db.StringField( max_length=50 )
    p  =   db.StringField( max_length=50 )
    answer4 =   db.StringField( max_length=1 )

    question5  =   db.StringField( max_length=3 )
    q5 =   db.StringField( max_length=1 )
    q  =   db.StringField( max_length=50 )
    r  =   db.StringField( max_length=50 )
    s  =   db.StringField( max_length=50 )
    t  =   db.StringField( max_length=50 )
    answer5 =   db.StringField( max_length=1 )

    question6  =   db.StringField( max_length=3 )
    q6 =   db.StringField( max_length=1 )
    u  =   db.StringField( max_length=50 )
    v  =   db.StringField( max_length=50 )
    w  =   db.StringField( max_length=50 )
    x  =   db.StringField( max_length=50 )
    answer6 =   db.StringField( max_length=1 )

    question7  =   db.StringField( max_length=3 )
    q7 =   db.StringField( max_length=1 )
    y  =   db.StringField( max_length=50 )
    z  =   db.StringField( max_length=50 )
    aa  =   db.StringField( max_length=50 )
    ab  =   db.StringField( max_length=50 )
    answer7 =   db.StringField( max_length=1 )

class Course(db.Document):
    courseID    =   db.StringField( max_length=10, unique=True )
    title       =   db.StringField( max_length=100 )
    description =   db.StringField( max_length=255 )
    credits     =   db.IntField()
    term        =   db.StringField( max_length=25 )

class Enrollment(db.Document):
    user_id     =   db.IntField()
    courseID    =   db.StringField( max_length=10 )

class Comp_cards1(db.Document):
    quiz_id     =   db.StringField( max_length=10 )
    url         =   db.StringField( max_length=40 )
    quiz_title  =   db.StringField( max_length=40 )
    table_name  =   db.StringField( max_length=10 )


    question1  =   db.StringField( max_length=3 )
    q1 =   db.StringField( max_length=1 )
    a  =   db.StringField( max_length=50 )
    b  =   db.StringField( max_length=50 )
    c  =   db.StringField( max_length=50 )
    answer1 =   db.StringField( max_length=1 )

    question2  =   db.StringField( max_length=3 )
    q2 =   db.StringField( max_length=1 )
    d  =   db.StringField( max_length=50 )
    e  =   db.StringField( max_length=50 )
    f  =   db.StringField( max_length=50 )
    answer2 =   db.StringField( max_length=1 )

    question3  =   db.StringField( max_length=3 )
    q3 =   db.StringField( max_length=1 )
    g  =   db.StringField( max_length=50 )
    h  =   db.StringField( max_length=50 )
    i  =   db.StringField( max_length=50 )
    answer3 =   db.StringField( max_length=1 )

    question4  =   db.StringField( max_length=3 )
    q4 =   db.StringField( max_length=1 )
    j  =   db.StringField( max_length=50 )
    k  =   db.StringField( max_length=50 )
    l  =   db.StringField( max_length=50 )
    answer4 =   db.StringField( max_length=1 )

    question5  =   db.StringField( max_length=3 )
    q5 =   db.StringField( max_length=1 )
    m  =   db.StringField( max_length=50 )
    n  =   db.StringField( max_length=50 )
    o  =   db.StringField( max_length=50 )
    answer5 =   db.StringField( max_length=1 )

class Tt(db.Document):
    quiz_id     =   db.StringField( max_length=10 )
    table_name  =   db.StringField( max_length=10 )
    url         =   db.StringField( max_length=40 )
    quiz_title  =   db.StringField( max_length=40 )
    paper       =   db.StringField( max_length=2 )
    paper_no    =   db.StringField( max_length=2 )
    paper_type  =   db.StringField( max_length=10 )

    question1  =   db.StringField( max_length=3 )
    q1 =   db.StringField( max_length=1 )
    a  =   db.StringField( max_length=50 )
    b  =   db.StringField( max_length=50 )
    c  =   db.StringField( max_length=50 )
    d  =   db.StringField( max_length=50 )
    answer1 =   db.StringField( max_length=1 )

    question2  =   db.StringField( max_length=3 )
    q2 =   db.StringField( max_length=1 )
    e  =   db.StringField( max_length=50 )
    f  =   db.StringField( max_length=50 )
    g  =   db.StringField( max_length=50 )
    h  =   db.StringField( max_length=50 )
    answer2 =   db.StringField( max_length=1 )

    question3  =   db.StringField( max_length=3 )
    q3 =   db.StringField( max_length=1 )
    i  =   db.StringField( max_length=50 )
    j  =   db.StringField( max_length=50 )
    k  =   db.StringField( max_length=50 )
    l  =   db.StringField( max_length=50 )
    answer3 =   db.StringField( max_length=1 )

    question4  =   db.StringField( max_length=3 )
    q4 =   db.StringField( max_length=1 )
    m  =   db.StringField( max_length=50 )
    n  =   db.StringField( max_length=50 )
    o  =   db.StringField( max_length=50 )
    p  =   db.StringField( max_length=50 )
    answer4 =   db.StringField( max_length=1 )

    question5  =   db.StringField( max_length=3 )
    q5 =   db.StringField( max_length=1 )
    q  =   db.StringField( max_length=50 )
    r  =   db.StringField( max_length=50 )
    s  =   db.StringField( max_length=50 )
    t  =   db.StringField( max_length=50 )
    answer5 =   db.StringField( max_length=1 )

    question6  =   db.StringField( max_length=3 )
    q6 =   db.StringField( max_length=1 )
    u  =   db.StringField( max_length=50 )
    v  =   db.StringField( max_length=50 )
    w  =   db.StringField( max_length=50 )
    x  =   db.StringField( max_length=50 )
    answer6 =   db.StringField( max_length=1 )

    question7  =   db.StringField( max_length=3 )
    q7 =   db.StringField( max_length=1 )
    y  =   db.StringField( max_length=50 )
    z  =   db.StringField( max_length=50 )
    aa  =   db.StringField( max_length=50 )
    ab  =   db.StringField( max_length=50 )
    answer7 =   db.StringField( max_length=1 )

    question8  =   db.StringField( max_length=3 )
    q8 =   db.StringField( max_length=1 )
    ac  =   db.StringField( max_length=50 )
    ad  =   db.StringField( max_length=50 )
    ae  =   db.StringField( max_length=50 )
    af  =   db.StringField( max_length=50 )
    answer8 =   db.StringField( max_length=1 )

    question9  =   db.StringField( max_length=3 )
    q9 =   db.StringField( max_length=1 )
    ag  =   db.StringField( max_length=50 )
    ah  =   db.StringField( max_length=50 )
    ai  =   db.StringField( max_length=50 )
    aj  =   db.StringField( max_length=50 )
    answer9 =   db.StringField( max_length=1 )

    question10  =   db.StringField( max_length=3 )
    q10 =   db.StringField( max_length=1 )
    ak  =   db.StringField( max_length=50 )
    al  =   db.StringField( max_length=50 )
    am  =   db.StringField( max_length=50 )
    an  =   db.StringField( max_length=50 )
    answer10 =   db.StringField( max_length=1 )