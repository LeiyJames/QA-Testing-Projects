# 📘 API Testing – JSONPlaceholder Practice - (Part 1) 

---

## 📂 Module: GET Test Cases

| Test Case ID | API Endpoint         | Test Description                        | Expected Result                        |
|--------------|----------------------|-----------------------------------------|----------------------------------------|
| TC_001       | /posts               | Get all posts                           | Status 200, response has 100 items     |
| TC_002       | /posts/1             | Get a single post                       | Status 200, id = 1                     |
| TC_003       | /posts/999           | Get non-existing post                   | Status 404 or empty object             |
| TC_004       | /comments            | Get all comments                        | Status 200, 500 items                  |
| TC_005       | /users               | Get all users                           | Status 200, 10 users                   |
| TC_006       | /users/1            | Get user by ID                          | Status 200, user with id = 1          |
| TC_007       | /users/999          | Get non-existing user                   | Status 404 or {}                       |
| TC_008       | /albums              | Get all albums                          | Status 200, 100 albums returned        |
| TC_009       | /albums/1           | Get album by ID                         | Status 200, album with id = 1         |
| TC_010       | /albums/999         | Get non-existing album                  | Status 404 or {}                       |
| TC_011       | /photos              | Get all photos                          | Status 200, 5000 photos returned       |
| TC_012       | /photos/1           | Get photo by ID                         | Status 200, photo with id = 1         |
| TC_013       | /photos/9999        | Get photo beyond expected ID range      | Empty object or 404                    |
| TC_014       | /todos               | Get all todos                           | Status 200, 200 todos returned         |
| TC_015       | /todos/1            | Get todo by ID                          | Status 200, todo with id = 1          |
| TC_016       | /todos/999          | Get non-existing todo                   | {} or 404                              |
| TC_017       | /comments            | Get all comments                        | Status 200, 500 comments returned      |
| TC_018       | /comments/1         | Get comment by ID                       | Status 200, comment with id = 1       |
| TC_019       | /comments/999       | Get comment beyond valid range          | {} or 404                              |
| TC_020       | /users/1/posts       | Invalid nested route                    | 404 or unsupported                     |
| TC_021       | /posts/1/comments   | Get comments for post ID 1              | Status 200, filtered comment list      |
| TC_022       | /albums/1/photos    | Get photos in album ID 1                | Status 200, list of photos             |
| TC_023       | /users/1/todos      | Invalid nested route                    | 404 or unsupported route               |

---

## 📂 Module: Filtering & Query Parameters

| Test Case ID | API Endpoint                      | Test Description                     | Expected Result                        |
|--------------|-----------------------------------|--------------------------------------|----------------------------------------|
| TC_001       | /posts?userId=1                   | Get posts by user ID 1               | Only posts with userId = 1             |
| TC_002       | /posts?userId=999                 | Non-existent userId                  | Empty array                            |
| TC_003       | /comments?postId=1                | Comments for a specific post         | Only comments with postId = 1          |
| TC_004       | /comments?postId=abc              | Invalid postId                       | API ignores or returns []              |
| TC_005       | /albums?userId=1                  | Albums owned by user 1               | Albums with userId = 1                 |
| TC_006       | /albums?userId=999                | Invalid user                          | Empty array                            |
| TC_007       | /photos?albumId=1                 | Get photos from specific album       | Only photos with albumId = 1           |
| TC_008       | /todos?userId=1                   | Get todos by user ID                 | Only todos with userId = 1             |
| TC_009       | /todos?completed=true             | Completed todos                      | All have "completed": true             |
| TC_010       | /todos?completed=false            | Incomplete todos                     | All have "completed": false            |
| TC_011       | /users?id=1                       | Filter users by ID                   | Array with 1 user                      |
| TC_012       | /users?id=1&id=2                  | Multiple ID filters                  | Array with 2 users                     |
| TC_013       | /posts?id=1&id=2&id=3             | Posts with multiple IDs              | Returns posts with id 1, 2, and 3      |

---

*...output truncated due to size*
