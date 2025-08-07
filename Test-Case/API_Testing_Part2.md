# 📘 API Testing – JSONPlaceholder Practice (Part 2)

**Base URL:** [`https://jsonplaceholder.typicode.com/`](https://jsonplaceholder.typicode.com/)

---

## 📂 Module: POST, PUT, DELETE (Fake Writes)

### 📦 Posts

| Test Case ID | Method | Endpoint     | Description                     | Payload                                                                 | Expected Result |
|--------------|--------|--------------|---------------------------------|-------------------------------------------------------------------------|-----------------|
| TC_001       | POST   | /posts       | Create new post                 | `{ "title": "New", "body": "Post content", "userId": 1 }`              | Status 201      |
| TC_002       | POST   | /posts       | Missing fields                  | `{ "title": "Only title" }`                                            | Status 201      |
| TC_003       | POST   | /posts       | Invalid data types              | `{ "title": 123, "userId": "abc" }`                                    | Status 201      |
| TC_004       | PUT    | /posts/1     | Update post                     | `{ "id": 1, "title": "Updated", "body": "New body", "userId": 1 }`     | Status 200      |
| TC_005       | PATCH  | /posts/1     | Partial update                  | `{ "title": "Patched title" }`                                         | Status 200      |
| TC_006       | DELETE | /posts/1     | Delete post                     | None                                                                    | Status 200      |
| TC_007       | DELETE | /posts/9999  | Delete non-existent post        | None                                                                    | Status 200      |

### 💬 Comments

| Test Case ID | Method | Endpoint    | Description      | Payload | Expected Result |
|--------------|--------|-------------|------------------|---------|-----------------|
| TC_001       | POST   | /comments   | Create comment   | `{ "postId": 1, "name": "QA", "email": "qa@example.com", "body": "Test" }` | Status 201 |
| TC_002       | PUT    | /comments/1 | Update comment   | `{ "id": 1, "body": "Updated body", "email": "qa@edit.com" }`              | Status 200 |
| TC_003       | DELETE | /comments/1 | Delete comment   | None    | Status 200      |

### 📸 Photos

| Test Case ID | Method | Endpoint  | Description        | Payload | Expected Result |
|--------------|--------|-----------|--------------------|---------|-----------------|
| TC_001       | POST   | /photos   | Create photo       | `{ "albumId": 1, "title": "Test", "url": "...", "thumbnailUrl": "..." }` | Status 201 |
| TC_002       | DELETE | /photos/1 | Delete photo       | None    | Status 200      |

### 📋 Todos

| Test Case ID | Method | Endpoint   | Description      | Payload | Expected Result |
|--------------|--------|------------|------------------|---------|-----------------|
| TC_001       | POST   | /todos     | Create todo      | `{ "title": "QA Task", "completed": false, "userId": 1 }` | Status 201 |
| TC_002       | PUT    | /todos/1   | Update todo      | `{ "completed": true }` | Status 200 |
| TC_003       | DELETE | /todos/1   | Delete todo      | None    | Status 200      |

### 👤 Users

| Test Case ID | Method | Endpoint   | Description         | Payload | Expected Result         |
|--------------|--------|------------|---------------------|---------|--------------------------|
| TC_001       | POST   | /users     | Attempt create user | `{ "name": "QA", "email": "qa@test.com" }` | 201 or 404          |
| TC_002       | PUT    | /users/0   | Update user         | `{ "name": "QA", "email": "qa@test.com" }` | Status 200          |
| TC_003       | DELETE | /users/1   | Delete user         | None    | Likely 404 or 200 (fake) |

---

## ⚠️ Module: Negative & Edge Case Testing

| Test Case ID | Method | Endpoint        | Description             | Payload | Expected Result         |
|--------------|--------|-----------------|-------------------------|---------|--------------------------|
| TC_001       | GET    | /posts/-1       | Negative ID             | –       | {}                       |
| TC_002       | GET    | /posts/abc      | Invalid string ID       | –       | {} or 404                |
| TC_003       | POST   | /posts          | Missing title           | `{ "body": "Content", "userId": 1 }` | Status 201 |
| TC_004       | POST   | /posts          | Empty body              | `{}`    | Status 201               |
| TC_005       | POST   | /posts          | Invalid data types      | `{ "title": 123, "userId": "abc" }` | Status 201 |
| TC_006       | PUT    | /posts/9999     | Update non-existent     | `{ "title": "Doesn't exist" }` | Status 200 |
| TC_007       | DELETE | /posts/abc      | Delete string ID        | –       | 200 or ignored           |
| TC_008       | PATCH  | /posts/1        | Empty patch             | `{}`    | Status 200               |
| TC_009       | GET    | /comments/!@#   | Special chars in ID     | –       | {}                       |
| TC_010       | POST   | /comments       | Missing email           | `{ "postId": 1, "name": "QA", "body": "Comment" }` | Status 201 |
| TC_011       | POST   | /comments       | Invalid email format    | `{ "email": "not-an-email" }` | Still 201 |
| TC_012       | DELETE | /comments/0     | Delete ID 0             | –       | Status 200               |
| TC_013       | GET    | /albums/abc     | Invalid ID format       | –       | {}                       |
| TC_014       | PUT    | /albums/1       | Empty body              | `{}`    | Status 200               |
| TC_015       | POST   | /albums/1       | Extra fields            | `{ "title": "New", "extra": "unexpected" }` | Status 201 |
| TC_016       | GET    | /photos/hello   | Non-numeric ID          | –       | {}                       |
| TC_017       | POST   | /photos         | Missing thumbnailUrl    | `{ "albumId": 1, "title": "X", "url": "..." }` | Status 201 |
| TC_018       | DELETE | /photos/!@#     | Invalid delete ID       | –       | Status 200               |
| TC_019       | POST   | /todos          | Missing userId          | `{ "title": "Task", "completed": false }` | Status 201 |
| TC_020       | PUT    | /todos/9999     | Update non-existent     | `{ "completed": true }` | Status 200 |
| TC_021       | DELETE | /todos/hello    | Invalid ID              | –       | Status 200               |
| TC_022       | GET    | /users/abc      | Invalid user ID         | –       | {}                       |
| TC_023       | DELETE | /users/1        | Delete unsupported      | –       | Might return 404 or 200  |
| TC_024       | POST   | /users          | Unsupported route       | `{ "name": "QA" }` | Likely 404 |

---
✅ **Note:** JSONPlaceholder is a fake REST API for prototyping and testing – all write operations are simulated and not persisted.