import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "b'\x99d\x14Pr%U\x9a7\xc9\xb2\x02e\xbb\x15\xce'"
    # MONGODB_SETTNGS = { 'db': 'test' }
   
    # MONGODB_SETTNGS = { 
    #     'username': 'dreid254',
    #     'password': 'Guinness02',
    #     'db': 'my_quizzes',
    #     'host': 'mongodb+srv://dreid254:Guinness02@cluster0-xqife.gcp.mongodb.net/my_quizzes'
    #     }