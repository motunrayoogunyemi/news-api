# news-api
README

Overview

News-Api is organized around REST. It provides many separate REST APIs for getting news posts, making comments and upvoting a post. Our API returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

###### url

$ https://newss-api.herokuapp.com/

Endpoints

GET ALL

Endpoint: /posts

Endpoint: /comments

Response will be an object containing the list of news/comments (array) 

GET ONE

Endpoint: /posts/{post_id}

Endpoint: /comment/{comment_id}

Response will be an object containing a news/comment

POST

Endpoint: /posts

Endpoint: /comments

Endpoint: /vote 

Response will be an object containing the new post 

PUT

Endpoint: /posts/{post_id}

Endpoint: /comments/{comment_id}

Response will be an object containing the updated post 

DELETE

Endpoint: /posts/{post_id}

Endpoint: /comments/{comment_id}

Response will be a json message(‘successfully deleted”)


Errors

200: success

201: created

400: bad request

### Follow this link to the postman documentation

Postman collection link

https://documenter.getpostman.com/view/16874283/UVsEXAMn
