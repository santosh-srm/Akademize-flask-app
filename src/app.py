"""Flask App."""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    """Hello."""
    return """
            <div>
            <h1>Hello World!, Welcome</h1>
            <p>Started Today</p>
            </div>

    """

### """    
#@app.route('/contact')
#def hello():
#    """Contact Info."""
#    return """
#            <div>
 #           <h1>Phone: 999-999-9999</h1>
  #          <p>
   #             Address: Country Name.
    #        </p>
     #       </div>
#    """
###

#@app.route('/<name>')
#def hello_name(name):
#	return "Hello {}!".format(name)

if __name__=='__main__':
	app.run()