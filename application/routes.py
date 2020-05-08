from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from application.models import User, Course, Enrollment, Comp_cards1, Word_problems, Tt
from application.forms import LoginForm, RegisterForm

# courseData = [{"courseID":"1111","title":"PHP 111","description":"Intro to PHP","credits":"3","term":"Fall, Spring"}, {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":"4","term":"Spring"}, {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":"3","term":"Fall"}, {"courseID":"4444","title":"Angular 1","description":"Intro to Angular","credits":"3","term":"Fall, Spring"}, {"courseID":"5555","title":"Java 2","description":"Advanced Java Programming","credits":"4","term":"Fall"}]

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True )

@app.route("/login", methods=['GET','POST'])
def login():
    if session.get('username'):
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        # if user and user.get_password(password): this was to unhash the password
        if user and password==user.password:
            flash(f"{user.first_name}, you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.first_name
            return redirect("/index")
        else:
            flash("Sorry, something went wrong.","danger")
    return render_template("login.html", title="Login", form=form, login=True )

@app.route("/logout")
def logout():
    session['user_id']=False
    session.pop('username', None)
    return redirect(url_for("index"))

#########     step 1 of maths     choose word probelms 2-5

@app.route("/quizmathsselect1")
def quizmathsselect1():
    if not session.get('username'):
        return redirect(url_for('index'))
    quiz_selection = Word_problems.objects()

    return render_template("quizmathsselect1.html", quiz_selection=quiz_selection )


# @app.route("/quizmathsselect2")
# def word_problems():
#     if not session.get('username'):
#         return redirect(url_for('index'))
#     quizzes = Word_problems.objects()
#     return render_template("quizmathsselect2.html", quizzes=quizzes )

#########     step 2 of maths     select type of quiz for the level chosen
@app.route("/quizmathsselect2", methods=["GET","POST"])
def quizmathsselect2():
    if not session.get('username'):
        return redirect(url_for('index'))
    #get the quiz to take
    quiz_level = request.form.get('quiz_level')
    paper = request.form.get('paper')

    global quizzes

    if quiz_level:
        quizzes = Word_problems.objects.filter(quiz_level=quiz_level)
    elif paper:
        quizzes = Tt.objects.filter(paper=paper)
        
    return render_template("quizmathsselect2.html", quizzes=quizzes)

#########     step 2 of maths     Take the Quiz
@app.route("/quiztakemaths", methods=["GET","POST"])
def quiztakemaths():
    if not session.get('username'):
        return redirect(url_for('index'))
    #get the quiz to take
    quiz_id = request.form.get('quiz_id')
    table_name = request.form.get('table_name')

    if table_name == "word_problems":
        quizzes = Word_problems.objects.filter(quiz_id=quiz_id)
    if table_name == "tt":
        quizzes = Tt.objects.filter(quiz_id=quiz_id)
    
    with open('quiz.json', 'w') as f:  # writing JSON object
        json.dump(quizzes, f)  
        
    return render_template("quiztakemaths.html", quizzes=quizzes, quiz_id=quiz_id, table_name=table_name)

@app.route("/quizsubmitwp", methods=["GET","POST"])
def quizsubmitwp():
    if not session.get('username'):
        return redirect(url_for('index'))
    #get the form details 
    table_name = request.form.get('table_name')
    ch1 = request.form.get('options1')
    choice2 = request.form.get('options2')
    if choice2 == 'e':
        ch2 = 'a'
    if choice2 == 'f':
        ch2 = 'b'
    if choice2 == 'g':
        ch2 = 'c'
    if choice2 == 'h':
        ch2 = 'd'
    choice3 = request.form.get('options3')
    if choice3 == 'i':
        ch3 = 'a'
    if choice3 == 'j':
        ch3 = 'b'
    if choice3 == 'k':
        ch3 = 'c'
    if choice3 == 'l':
        ch3 = 'd'
    choice4 = request.form.get('options4')
    if choice4 == 'm':
        ch4 = 'a'
    if choice4 == 'n':
        ch4 = 'b'
    if choice4 == 'o':
        ch4 = 'c'
    if choice4 == 'p':
        ch4 = 'd'
    choice5 = request.form.get('options5')
    if choice5 == 'q':
        ch5 = 'a'
    if choice5 == 'r':
        ch5 = 'b'
    if choice5 == 's':
        ch5 = 'c'
    if choice5 == 't':
        ch5 = 'd'
    choice6 = request.form.get('options6')
    if choice6 == 'u':
        ch6 = 'a'
    if choice6 == 'v':
        ch6 = 'b'
    if choice6 == 'w':
        ch6 = 'c'
    if choice6 == 'x':
        ch6 = 'd'
    choice7 = request.form.get('options7')
    if choice7 == 'y':
        ch7 = 'a'
    if choice7 == 'z':
        ch7 = 'b'
    if choice7 == 'aa':
        ch7 = 'c'
    if choice7 == 'ab':
        ch7 = 'd'
    choice8 = request.form.get('options8')
    if choice8 == 'ac':
        ch8 = 'a'
    if choice8 == 'ad':
        ch8 = 'b'
    if choice8 == 'ae':
        ch8 = 'c'
    if choice8 == 'af':
        ch8 = 'd'
    choice9 = request.form.get('options9')
    if choice9 == 'ag':
        ch9 = 'a'
    if choice9 == 'ah':
        ch9 = 'b'
    if choice9 == 'ai':
        ch9 = 'c'
    if choice9 == 'aj':
        ch9 = 'd'
    choice10 = request.form.get('options10')
    if choice10 == 'ak':
        ch10 = 'a'
    if choice10 == 'al':
        ch10 = 'b'
    if choice10 == 'am':
        ch10 = 'c'
    if choice10 == 'an':
        ch10 = 'd'
    
    # Opening JSON file 
    with open('quiz.json', 'r') as read_file: 
  
    # Reading from json file 
        quiz_data = json.load(read_file) 

        result = quiz_data[0]["answer1"]

    if table_name == "tt":
        return render_template("quizsubmitwp.html", quiz_data=quiz_data, ch1=ch1,
        ch2=ch2, ch3=ch3, ch4=ch4, ch5=ch5, ch6=ch6, ch7=ch7, ch8=ch8, ch9=ch9, ch10=ch10, table_name=table_name)
    else:
        return render_template("quizsubmitwp.html", quiz_data=quiz_data, ch1=ch1,
        ch2=ch2, ch3=ch3, ch4=ch4, ch5=ch5, ch6=ch6, ch7=ch7)

@app.route("/quizreadingselect1")
def quizreadingselect1():
    if not session.get('username'):
        return redirect(url_for('index'))

    quizzes = Comp_cards1.objects()
    return render_template("quizreadingselect1.html", quizzes=quizzes )

@app.route("/quizselect")
def quizselect():
    if not session.get('username'):
        return redirect(url_for('index'))

    return render_template("quizselect.html")


@app.route("/quizreading", methods=["GET","POST"])
def quizstartreading():
    if not session.get('username'):
        return redirect(url_for('index'))
    #get the quiz to take
    quiz_id = request.form.get('quiz_id')
    quizzes = Comp_cards1.objects.filter(quiz_id=quiz_id)
    
    with open('quiz.json', 'w') as f:  # writing JSON object
        json.dump(quizzes, f)  
        
    return render_template("quizreading.html", quizzes=quizzes, quiz_id=quiz_id)



@app.route("/quizsubmit", methods=["GET","POST"])
def quizsubmit():
    if not session.get('username'):
        return redirect(url_for('index'))
    #get the form details 
    table_name = request.form.get('table_name')
    ch1 = request.form.get('options1')
    choice2 = request.form.get('options2')
    if choice2 == 'd':
        ch2 = 'a'
    if choice2 == 'e':
        ch2 = 'b'
    if choice2 == 'f':
        ch2 = 'c'
    choice3 = request.form.get('options3')
    if choice3 == 'g':
        ch3 = 'a'
    if choice3 == 'h':
        ch3 = 'b'
    if choice3 == 'i':
        ch3 = 'c'
    choice4 = request.form.get('options4')
    if choice4 == 'j':
        ch4 = 'a'
    if choice4 == 'k':
        ch4 = 'b'
    if choice4 == 'l':
        ch4 = 'c'
    choice5 = request.form.get('options5')
    if choice5 == 'm':
        ch5 = 'a'
    if choice5 == 'n':
        ch5 = 'b'
    if choice5 == 'o':
        ch5 = 'c'

    # Opening JSON file 
    with open('quiz.json', 'r') as read_file: 
  
    # Reading from json file 
        quiz_data = json.load(read_file) 

        result = quiz_data[0]["answer1"]
     
    return render_template("quizsubmit.html", quiz_data=quiz_data, ch1=ch1,
    ch2=ch2, ch3=ch3, ch4=ch4, ch5=ch5)



@app.route("/register", methods=['POST','GET'])
def register():
    
    form = RegisterForm()
    if form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        password    = form.password.data
        first_name  = form.first_name.data
        last_name   = form.last_name.data

        user = User(user_id=user_id, email=email, first_name=first_name, last_name=last_name, password=password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('index'))
    return render_template("register.html", title="Register", form=form, register=True)

@app.route("/user")
def user():
     users = User.objects.all()
     return render_template("user.html", users=users)