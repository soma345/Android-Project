# defining imports
from flask import Flask, render_template, request
import requests
import pandas as pd


app = Flask(__name__)  # initialising the flask app with the name 'app'


# route with allowed methods as POST and GET

@app.route('/', methods=['POST', 'GET'])
def index():    
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "") # obtaining the search string entered in the form 
            #mydict = {"Product":"productresult", "Name":"Nameresult", "Rating":"ratingResult", "CommentHead":"commentHeadResult", "Comment":"custCommentResult"} # saving that detail to a dictionary            
            mydict = {} # saving that detail to a dictionary            
            reviews = []
            comments = ['searchString1','name1','rating1','commentHead1', 'custComment1'] # Dataframe 
            for comment in range(len(comments)):
                try:
                    searchString = comment[0].text

                except:
                    searchString = 'No searchString'

                try:
                    name = comment[1].text

                except:
                    name = 'No Name'

                try:
                    rating = comment[2].text

                except:
                    rating = 'No Rating'

                try:
                    commentHead = comment[3].text
                except:
                    commentHead = 'No Comment Heading'
                try:
                    custComment = comment[4].text                    
                except:
                    custComment = 'No Customer Comment' 

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,"Comment": custComment} # saving that detail to a dictionary
                reviews.append(mydict) #  appending the comments to the review list                 
            return render_template('results.html', reviews=reviews) # showing the review to the user
        except:
            return 'something is wrong'
                #return render_template('results.html')
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(port=8000,debug=True) # running the app on the local machine on port 8000