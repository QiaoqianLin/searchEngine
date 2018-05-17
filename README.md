### An overview of the function of the code
  The code is a search engine mainly for searching in the CS department in UIUC, users can search the keywords under three categories: academic, admission and research.  This search engine could be very useful when people prefer the search results to be classified. For example, if a high school student want to look for contents about cs program admission in UIUC, then she/he can choose the category as “academics” or “admissions” when input the search keywords.  

### Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement.

Our search system is built with **Elastic Search(es)**, a open source search engine and **BeautifulSoup**, a document parsing library. To represent our search results, we built a website using **Django** and **Bootstrap** framework. So the main development language is Python. We used **Website Downloader** to crawl all the websites belong to illinois CS department and chose three categories of websites that we thought would be most useful as our source data. The three categories are academics, admissions and research. We used the built-in **english analyzer** to create index for the website contents, the details are in es_create_index.py. Then, in index_data.py, we built a dictionary to translate the source htmls to their real urls so as to make the search results accessible. Also, we indexed and parsed the data into tokens, es would save those tokenized data as well as their urls into the index body for further search function. In search function(views.py), we use es search function to match the query with the local website contents and return the top five results to users. 

### Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable. 
First, download our github repository to local device.
Second, decompress and open the file elasticsearch-6.2.4/bin/elasticsearch (If errors occured while trying to run elasticsearch, then please download the latest elasticsearch zip https://www.elastic.co/downloads/elasticsearch to replace the current one.)
Third, start django server with the command “python manage.py runserver”
Fourth, run the file es_create_index.py
Fifth, open a browser and type in “http://127.0.0.1:8000/” to use our search function.

### Brief description of contribution of each team member in case of a multi-person team.
Mengfei Liang: Build index and implement the search function for the CS websites crawled. Also work on Django to represent the search results.  
Qiaoqian Lin: Use Django and HTML/CSS to implement the struture of the website including the front-end part, to show the search results.


### Deficiency
Due to the limited time and some conflicts about topic(change topic in the middle of projects for several time), some of the functions and the implementation of more readable result (after result return) was not able to achieved. We will keep working on it during summer to make it more useful and readable .

