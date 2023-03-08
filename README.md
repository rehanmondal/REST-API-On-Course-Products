## <img src="https://user-images.githubusercontent.com/125151906/223210076-58b29154-0e90-4e37-b42f-f23387cfe83f.png" width="40px;" height="40px;"> { REST } Using 🐍🧪🐬

## In This Article:
- [Overview](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Schema](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Run cmd](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Root End Points](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [HTTP Verbs](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [HTTP Responses ](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Pagination](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [JSON type Responses](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [CORS](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)
- [Technology Used](https://awesomeopensource.com/project/elangosundar/awesome-README-templates)

### Overview 

Since REST APIs use standard HTTP verbs and with respect to specified response codes, 
it is easy to build API with this architechture. This article states how to build a REST API using Flask and MySQL with refference to the HTTP status codes, 
headers and a json body parameter whcih is basically the response body of the particular requests.
Whenever we send a request to the API, it will specify an HTTP method and a path. 
To make a request, at first we have to choose that particular the HTTP method and the path for the operation that we want to use. 
For example, the "../product/getall" the operation uses the GET method returns a json response. 

### Schema
The schema contains tables named "courses" that store information about the coursec products in differect attributes
The MySQL server application will respond with the requested information and will appear on clients' side.
### Run
    install requirements :pip install -r .\requirements.txt
##### Import .sql to database :<br>  	
    
    mysql> use db_name;
 	mysql> source file_name.sql;
    
##### Versions :<br>  
    Python 3.10.4
    Flask 2.2.2
    Werkzeug 2.2.2
    
### Root End Points    
    GET 	-> 	http://127.0.0.1:5000/
    GET 	-> 	http://127.0.0.1:5000/product/getall
    POST	->	http://127.0.0.1:5000/product/addone
    PUT	->	http://127.0.0.1:5000/product/update
    PATCH	->	http://127.0.0.1:5000/product/patch/<id>
                    http://127.0.0.1:5000/product/patch/12    
    DEL	->	http://127.0.0.1:5000/product/delete/<id>
                    http://127.0.0.1:5000/product/delete/14
    GET	->	http://127.0.0.1:5000/product/getall/limit/<limit>/page/<page>
                    http://127.0.0.1:5000/product/getall/limit/10/page/2
    GET	->	http://127.0.0.1:5000/product/getall/<subject>
                    http://127.0.0.1:5000/product/getall/C++
    GET	->	http://127.0.0.1:5000/product/filterby_price 
    GET	->	http://127.0.0.1:5000/product/filterby_price_&_subject
    GET	->	http://127.0.0.1:5000/product/sortby_price_lowTohigh
   
### HTTP Verbs
<table>
<thead>
<tr>
<th>Verb</th>
<th>Description</th>
</tr></thead>
<tbody>
<tr>
<td><code>GET</code></td>
<td>In this particular project it is used to retrieves all resources <code>../product/getall</code>, with filter <code>../product/filterby_price</code>,
with sort by price<code>../product/sortby_price_lowTohigh</code> <br><br></td>
</tr>

<tr>
<td><code>POST</code></td>
<td>Used to add new product.This route is called with full body detailed parameters /product/delete/<id><br><br></td>
</tr>

<tr>
<td><code>PUT</code></td>
<td>Updates the whole resourse. The request will be send with the full body parameters<code>../product/update</code> <br><br></td>
</tr>

<tr>
<td><code>PATCH</code></td>
<td>Updates partial data without changing the whole. Requested will be send with selected body parameters <code>..product/patch/<id></code><br><br>
</tr>

<tr>
<td><code>DELETE</code></td>
<td>Deletes data with the given product id. <code>../product/delete/{id}</code> <br><br></td>
</tr>
<tr>
<td><code>HEADERS</code></td>
<td>Content-Type : application/json<br><br></td>
</tr>

</tbody>
</table>

### HTTP Responses
HTTP response status codes indicates the specific HTTP request has been successfully completed. 
Successful responses (200 – 299) 
#### In this project the following status codes has beed used :
    200 -> OK - The query executed succesfully and completed the required task.
    201 -> Created - Products has been added to database succesfully.
    202 -> Accepted - It is used whenever the query is correct and also accepted but their is nothing to do, For eg. nothing to update, nothing to delete.
    204 -> No Content - Nothing to return from database in respect of that request.

### Pagination
When the response has too many values to show, the pagination function makes easy to provide limited selcted data in a page,
it return a subset of the response.In this case request additional pages of data.The endpoint supports the page and limit parameter, which control the number of results returned on a page. <code>../product/getall/limit/{limit}/page/{page} </code>

### CORS and JWT (Cross origin resource sharing & Json Web Token)
Implementation on Queue.

### JSON type Responses examples :<br>
##### METHOD : http://127.0.0.1:5000/product/getall
        {
            "products": [
                {
                    "core_subject": "Python",
                    "course_name": "Server Side Programm",
                    "duration": "45 days",
                    "enquiry": "9007045632",
                    "id": 1,
                    "payment_type": "one time",
                    "price": "7000"
                },
         
                {
                    "core_subject": "Data Science",
                    "course_name": "Big Dream in Data Sc",
                    "duration": "90 days",
                    "enquiry": "7894121478",
                    "id": 3,
                    "payment_type": "Lump sum",
                    "price": "7000"
                  }
            ]
        }

##### METHOD : http://127.0.0.1:5000/product/filterby_price_&_subject
        body inputs : 
            - subject : python
            - price : 9000
        {
            "products": [
                {
                    "core_subject": "Python",
                    "course_name": "Python with Flask",
                    "duration": "90 days",
                    "enquiry": "6290624578",
                    "id": 9,
                    "payment_type": "Monthly",
                    "price": "9000"
                }
            ]
        }

### Technology Used
<p><img src="https://user-images.githubusercontent.com/125151906/223213095-daa36254-ec9b-41f2-a5a9-5449498b21e3.png" width="100" height="60">&nbsp;&nbsp;
<img src="https://user-images.githubusercontent.com/125151906/223213321-5ff5dfab-03de-45fd-a49c-e9fe12bd3a88.png" width="100" height="60">&nbsp;&nbsp;
<img src="https://user-images.githubusercontent.com/125151906/223213089-b112d7c1-c7ab-4631-91d7-e66dc43e5713.png" width="100" height="60">&nbsp;&nbsp;
<img src="https://user-images.githubusercontent.com/125151906/223213536-d1ed5975-4822-4014-bf13-724fefef781e.png" width="100" height="60">&nbsp;&nbsp;</p>

### Comments
Hope you like this article and let me suggest if there would be any suitable modification required.I am still working on this api (Implementing JWT to encode with token and other request handlings) and after completing I will be hosted it with all Authentication parameters.Till then Stay Connected. Thanks to Connect! &nbsp;&nbsp;<img src="https://user-images.githubusercontent.com/125151906/223216986-3de16a0a-8e1c-4cc7-b180-386ec4b4da5c.png" width="40px;" height="32px;">



________________________________________________________________________________________________________________________________________________________



