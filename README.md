# App-Recommendation-webGUI
App recommendation using google playstore dataset 

## Ganga GUI task
---

For this task we will not need to use the Ganga framework at all, you will need to show the following:

 - Ability to create a simple webserver using the Python based [`Flask`](https://flask.palletsprojects.com/en/1.1.x/) web framework
 - Have the webserver render dynamic content using the [`jinja2`](https://jinja.palletsprojects.com/en/2.11.x/) templating engine
 - Modify the server to allow updating of the content by making it a RESTful service.

(*__Note__ that the content for this task can be anything that you like and we would very much like to see you be as creative as possible with the actual design of the web page. The graphical design forms part of the challenge.*)

## My Solution

As a part of the GUI task, I decided to build a content based app recommendation system using Flask. I choose this project because i believe that it satisfies the requirements mentioned in the challenge. The ML model is built using TF-IDF vectorizer, cosine similarity and the web interface is created using Flask. The dataset used for this project is Google Playstore Dataset from Kaggle. The aim of this system is to get 10 similar apps to the one that you mention in the website.

1. setup the flask.
```bash![screencapture-127-0-0-1-5000-2021-03-20-21_03_31](https://user-images.githubusercontent.com/42024284/111876105-265a1d00-89c3-11eb-9cb1-76513d270813.jpg)

cd task_3/
python3 app.py
```
2. Open the http://127.0.0.1:5000/ in any web browser. You will see something like this:

![Web Application Snapshot 1](https://user-images.githubusercontent.com/42024284/111875593-a2069a80-89c0-11eb-88e5-f0807761303d.png)


![Web Application Snapshot 2](https://user-images.githubusercontent.com/42024284/111875614-bcd90f00-89c0-11eb-902e-8f0c45c33e97.png)

3. Enter the app name in the form below. For example, I have entered "Google Play Books".

![Web Application Snapshot 3](https://user-images.githubusercontent.com/42024284/111875774-7cc65c00-89c1-11eb-99ae-1073ebf633ef.png)

4. The 10 recommended apps similar to app mentioned above will be shown. 

![Web Application Snapshot 4](https://user-images.githubusercontent.com/42024284/111876116-3245df00-89c3-11eb-9393-fc9ad7f42473.jpg)



