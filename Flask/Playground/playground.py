from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')
@app.route('/play/<x>')
@app.route('/play/<x>/<color>')                        
def play_ground(x='3',color="aqua"):
   
    return render_template('index.html',x=int(x),color=color)  
    
if __name__=="__main__":
    app.run(debug=True)                   
