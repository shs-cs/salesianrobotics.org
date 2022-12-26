import flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
async def home():
    """
    This is function handles the file for the main homepage `index.html`.
    """
    
    message_to_sponser = """
    Dear Boeing & DCE,

We are sincerely honored to have been accepted as the recipient of the $750 grant for each of our robotics teams. Thank you for your generosity, as this will allow us to reach limits we could not have reached otherwise with our robots.

As we compete in various robotics competitions, working towards success, we will always be extremely thankful for your thoughtful gift. Because of your grant, we hope to find ourselves at the state championship for the FTC Robotics competition in 2023.

Thank you again for your thoughtful and generous gift.

 \n- On behalf of the Salesian Robotics Teams
    
    """
    
    return render_template("index.html",sponsor_message=message_to_sponser)


@app.route('/about')
async def about():
      """
      This is for the about us page
        """
      return render_template("about.html")





if __name__ == app.import_name:
	app.run(host='0.0.0.0',port=5000,debug=True)