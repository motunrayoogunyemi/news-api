# news-api
README

NEWS-API

Overview
News-Api is organized around REST. It provides many separate REST APIs for getting news posts, making comments and upvoting a post. Our API returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

url
$ http://127.0.0.1:8000/
$ https://newss-api.herokuapp.com/


Endpoints
1.	Get all Posts and comments
  url: /posts
  url: /comments
  Response will be an object containing the list of news/comments (array) 
2.	Get one post and comment
  url: /posts/{post_id}
  url: /comment/{comment_id}
    Response will be an object containing a news post/comment
3.	make a news post, comment and upvote a post
    url: /posts
    url: /comments
    url: /vote
  Response will be an object containing the new post 
4.	update a post or comment
  url: /posts/{post_id}
  url: /comments/{comment_id}
Response will be an object containing the updated post 
5.	delete a post or comment
  url: /posts/{post_id}
  url: /comments/{comment_id}
Response will be json message(‘successfully deleted”)


errors
200: success
201: created
400: bad request
Postman collection link: https://www.getpostman.com/collections/c956c83bf63b238a42d7 
heroku: https://newss-api.herokuapp.com/ 
