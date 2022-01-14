# news-api
README

NEWS-API

Overview
News-Api is organized around REST. It provides many separate REST APIs for getting news posts, making comments and upvoting a post. Our API returns JSON-encoded responses, and uses standard HTTP response codes, authentication, and verbs.

url
$ http://127.0.0.1:8000/posts


Requests
1.	Get all
url: /posts
url: /comments
response: Response will be an object containing the list of news/comments (array) 
2.	Get one 
url: /posts/{post_id}
url: /comment/{comment_id}
response: Response will be an object containing a news post/comment
3.	post
url: /posts
url: /comments
url: /vote
response: Response will be an object containing the new post 
4.	update
url: /posts/{post_id}
url: /comments/{comment_id}
response: Response will be an object containing the updated post 
5.	delete
url: /posts/{post_id}
url: /comments/{comment_id}
response: Response will be json message(‘successfully deleted”)


errors
200: success
201: created
400: bad request
Postman collection link: https://www.getpostman.com/collections/c956c83bf63b238a42d7 
