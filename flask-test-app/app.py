from flask import Flask,render_template,redirect,url_for,request,make_response,abort
#from flask import render_template

app = Flask(__name__)
app.config.update({
       'SECRET_KEY':'a random string'        
})

@app.route('/')
def index():
    username = request.cookies.get('username')
    return 'Hello {}'.format(username)
    #return redirect(url_for('user_index',username='default'))

@app.route('/user/<username>')
def user_index(username):
    #return 'Hello {}'.format(username)
    reps = make_response(render_template('user_index.html',username=username))
    reps.set_cookie('username',username)
    return reps

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post {}'.format(post_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'),404



if __name__ == '__main__':
    app.run()
