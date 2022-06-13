# defining imports
from contextlib import nullcontext
from flask import Flask, render_template, request,session
import requests
import pandas as pd
import query
import recommender



app = Flask(__name__)  # initialising the flask app with the name 'app'
app.secret_key = 'super secret key'


#print("outside hello World")

@app.route('/', methods=['POST', 'GET'])
def search():
    #print("inside hello World")
    session.clear()
    session["searchString"] = None
    session["relList"] = None
    return render_template('index.html')

# route with allowed methods as POST and GET

@app.route('/search', methods=['POST', 'GET'])
def index():  
     
    if request.method == 'POST':
        try:
            #searchString = request.form['content'].replace(" ", "") # obtaining the search string entered in the form  
            if session is not None and session["searchString"] != None:
                searchString = session["searchString"] 
           
            else :
                searchString = request.form['content']
                session["searchString"]=searchString 
            mydict = [] # saving that detail to a dictionary       
            
            # Calling method to get data
            mydict = query.procStep(searchString) 
            
            

            #print("This is from front end ",len(mydict))
            
            reviews = []
            docIdList=[]
            comments =[
	                    ['Raintree County', 'Ross Lockridge, Jr.', 'Fiction', "plot", 459],
	                    ['Raintree County1', 'Ross Lockridge, Jr.1', 'Fiction1', "plot1", 460],
                        ['Raintree County2', 'Ross Lockridge, Jr.2', 'Fiction2', "plot2", 461],
                        ['Raintree County3', 'Ross Lockridge, Jr.3', 'Fiction2', "plot3", 462],
                        ['Raintree County4', 'Ross Lockridge, Jr.4', 'Fiction', "plot4", 463],
                      ]# Dataframe 
            #print(len(mydict))
            #booklist = pd.read_csv('book-details.csv')
            #print("before loop")
            for comment in range(len(mydict)):
                
                    #print("with in for loop")
                    try:
                        bookTitle = mydict[comment][0]
                        

                    except:
                        bookTitle = ' '

                    try:
                        bookAuthor = mydict[comment][1]
                        

                    except:
                        bookAuthor = ' '

                    try:
                        #Genre=mydict[comment][2]
                        genreList1 = []
                        genreList = mydict[comment][2]
                        genrelen = len(mydict[comment][2])
                        
                        for comment1 in range(genrelen):
                            #print(genreList[comment1])
                            #genreList1.append(genreList[comment1])
                            previousGenre = genreList[comment1]
                            Genre  = ','.join(genreList)
                        
                        #print(Genre)
                        
                    except:
                        Genre = ' '

                    try:
                        plot = mydict[comment][3]
                        

                    except:
                        plot = ' '

                    try:
                        docID = mydict[comment][4]
                        docIdList.append(docID)
                        

                    except:
                        docID = ' '

                    
                    mydict1 = {"BookTitle": bookTitle, "BookAuthor": bookAuthor , "Genre": Genre , "Plot" :plot ,"DocId" :docID} 
                    # saving that detail to a dictionary
                    reviews.append(mydict1) #  appending the comments to the review list 
            session["docidlist"] = docIdList
            
            #print("session",session.get("docid"))           
            return render_template('results.html', reviews=reviews) # showing the review to the user
        except requests.exceptions.RequestException as e :
            return e
                #return render_template('results.html')
    else:
        return render_template('index.html')

@app.route('/bookdetails', methods=['POST', 'GET'])
def bookdetails():    
    if request.method == 'POST':
        relevance =[]
        doclist=[]
        feedback =[]
        feedbackList=[]
        try:
            #searchString = request.form['content'].replace(" ", "") # obtaining the search string entered in the form  
            relevance = request.form.getlist('relevence',type=int)
            session['relList'] = relevance

            doclist = session["docidlist"]
            #print("the revelance flag",relevance)
            #booklist = pd.read_csv('book-details.csv')
            reviews = []
            feedback = query.getResult(doclist,relevance)
            
            
            for comment in range(len(feedback)):
                
                    #print("with in for loop")
                    try:
                        bookTitle = feedback[comment][0]
                        

                    except:
                        bookTitle = ' '

                    try:
                        bookAuthor = feedback[comment][1]
                        

                    except:
                        bookAuthor = ' '

                    try:
                        genreList1 = []
                        genreList = feedback[comment][2]
                        genrelen = len(feedback[comment][2])
                        
                        for comment1 in range(genrelen):
                            #print(genreList[comment1])
                            #genreList1.append(genreList[comment1])
                            previousGenre = genreList[comment1]
                            Genre  = ','.join(genreList)
                        
                    except:
                        Genre = ' '

                    try:
                       plot = feedback[comment][3] 
                        
                    except:
                        plot = ' '

                    try:
                       docId = feedback[comment][4] 
                       feedbackList.append(docId)
                        
                    except:
                        docId = ' '

                    
                    mydict1 = {"BookTitle": bookTitle, "BookAuthor": bookAuthor , "Genre": Genre , "Plot" : plot ,"DocId" : docId}                       
            
                    # saving that detail to a dictionary
                    reviews.append(mydict1) #  appending the comments to the review list    
            session["relfeedlist"] = feedbackList             
            return render_template('relevanceResult.html', reviews=reviews)                 
           
        except:
            return 'something is wrong'
            #return render_template('resultsResult.html')
    else:
        return render_template('index.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    session.clear()
    session["searchString"] =None
    session["relList"] =None
    return render_template('index.html')

@app.route('/recomendation', methods=['POST', 'GET'])
def recomendation():
    orgList = []
    relFeedbackList=[]
    recommList =[]
    try:

        orgList = session['docidlist']
        relFeedbackList = session['relfeedlist']
        reviews2=[]

        recommList= recommender.recommender.reco_sys(orgList,relFeedbackList)
        #print ("recommendation", recommList)

        for comment in range(len(recommList)):
                    
                #print("with in for loop")
                try:
                    bookTitle = recommList[comment][0]
                    

                except:
                    bookTitle = ' '

                try:
                    bookAuthor = recommList[comment][1]
                    

                except:
                    bookAuthor = ' '

                try:
                    genreList1 = []
                    genreList = recommList[comment][2]
                    genrelen = len(recommList[comment][2])
                    
                    for comment1 in range(genrelen):
                        #print(genreList[comment1])
                        #genreList1.append(genreList[comment1])
                        previousGenre = genreList[comment1]
                        Genre  = ','.join(genreList)
                    
                except:
                    Genre = ' '

                try:
                    plot = recommList[comment][3] 
                    
                except:
                    plot = ' '

                try:
                    docId = recommList[comment][4] 
                    
                    
                except:
                    docId = ' '

                
                mydict2 = {"BookTitle": bookTitle, "BookAuthor": bookAuthor , "Genre": Genre , "Plot" : plot ,"DocId" : docId}                       
        
                # saving that detail to a dictionary
                reviews2.append(mydict2) #  appending the comments to the review list               
        return render_template('recommendation.html', reviews=reviews2)                 
            
    except requests.exceptions.RequestException as e:
        #return 'something is wrong'
        return 'something is wrong'
                #return render_template('resultsResult.html')
    else:
        return render_template('index.html')


@app.route('/back', methods=['POST', 'GET'])
def back():
    return render_template('results.html')

if __name__ == "__main__":
    
    app.run(port=8000,debug=False) # running the app on the local machine on port 8000