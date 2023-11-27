#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        return(render_template("index.html", result=90.2+(-50.6*rate)))
    else:
        return(render_template("index.html", result="waiting for exchange rate......"))

if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




