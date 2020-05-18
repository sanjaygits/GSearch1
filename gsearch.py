# Author    : Sanjay Kumar Kaleswaran
# Purpose   : Edureka Python Self Paced Course Project.
#               Q1: Create a python script called googlesearch that provides a command line utility
#               to perform google search. It gives you the top links (search results) of whatever you
#               want to search on google.
# Date      : 14 Feb 2018
# GitHub    : https://github.com/sanjaygits/GSearch1


import urllib.request
import urllib.response
import urllib.error
from pprint import pprint 
import json
import sys

#To perform a google search we would need a API key and Custom Search ID.
#I have generated these from https://cse.google.com/cse/
#The following are the API key and the Search Engine Id which needs to be added in the Google Search Query
#The query should be like this:
#https://www.googleapis.com/customsearch/v1?q=hi&cx={YOUR_CX_ID}&key={YOUR_API_KEY}

my_api_key = "AIzaSyDC7hNFXWum48OYliVbKbH0RAIPGieejDA"
my_cx_id = "015351968594091901794:2bnsmui9cfq"
url = 'https://www.googleapis.com/customsearch/v1?q='





# I have used the URLLib module to send the request through the urlopen function. urlopen is used to hit the url by
# network connection and provides the HTTPResponse object.
# HTTPResponse object is then read through the urllib.response.read().
# The encoding of the server is assumed to be utf-8 and then the JSON of the response is obtained. 

def search_google_query(queryurl):
    try:
        response = urllib.request.urlopen(queryurl)

        #Debugging purpose
        #print('\nThe response is :')
        #print(response)

        resp_html = response.read()
        encoding = response.info().get_content_charset('utf-8')
        resp_json = json.loads(resp_html.decode(encoding))
        
        # Once we have the JSON we print the htmlTitle and link of each of the response items using pprint
        print("\nSearch Response from Google are:\n")
        i=0
        while(i<5):
            pprint(resp_json['items'][i]['htmlTitle'])
            pprint(resp_json['items'][i]['link'])
            
            #htmlSnippet provides couple of extra lines on the search item. I have commented this out to provide a
            #bit of clarity.
            #pprint(resp_json['items'][i]['htmlSnippet']) 

            i = i+1
            print('\n\n')
        

        
        # Was using the below to understand the google response to find which objects I need to print out.   
        #pprint (m)
        #fres = open("D:\\Python\\temp.txt", "w+")
        #fres.write(str(m))
        #fres.close()
        #print(html)
        
        
    except urllib.error.URLError as e:
        # Prints any exception that is thrown from urllib.request.urlopen
        print("Code: %d, Reason: %s" % (e.code, e.reason))
    except:
        print("Unexpected Error", sys.exc_info()[0])
        raise

def main(query):
    # Provide the Query
    #query = input("Enter your search query: ")

    #Build the full query. 
    queryurl = url+query+'&cx='+my_cx_id+'&key='+my_api_key
    #print("The query url is :"+queryurl)

    #Call search_google_query() to generate the output.
    search_google_query(queryurl)


if __name__=='__main__':
    main("test")
    


