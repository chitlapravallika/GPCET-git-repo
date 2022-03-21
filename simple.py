from flask import Flask

app=Flask(__name__)
@app.route('/')
def homePage():
    return('hi_there!')

    if(__name__=="__main__"):
        app.run()