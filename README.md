## ✍️ [위코드 x 원티드] 백엔드 프리온보딩 선발 과제: 게시판 CRUD API

✔️ 글 작성, 글 확인, 글 목록 확인, 글 수정, 글 삭제가 되는 API

✔️ Contact: 박은혜, [ehye0922@gmail.com](mailto:ehye0922@gmail.com), 010-5158-4536

### 📌 초기 세팅

✔️ 가상환경 정보

$ conda create -n pre_onboarding python=3.8

$ conda activate pre_onboarding

✔️ 접속 정보

$ cd pre_onboarding

$ pip install -r requirements.txt

$ python [manage.py](http://manage.py/) migrate

$ python [manage.py](http://manage.py/) runserver

✔️ DB

DB: sqlite3

$ sqlite3 db.sqlite3

### 📌 Endpoint 호출

1. PostingDetailView
- 게시물 등록 POST /postings
- 게시물 조회 GET /postings/int:posting_id
- 게시물 수정 PATCH /postings/int:question_id
- 게시물 삭제DELETE /postings/int:question_id

2. PostingListView
- 게시물 목록 조회 GET /postings/list

3. SignUpView
- 회원가입 POST /users/signup

4. SignInView
- 로그인 POST /users/signin

### 📌 API 명세

📕 Postings app

(token은 헤더에 포함되어 있다는 가정)

1. 게시물 등록
```
* Sample Call:
  $ http POST 127.0.0.1:8000/postings title='test1', content='test1'
* Success Response: Code: 200 {"Message": "Success"}
* Error Response:
  Code: 400 KeyError Content: {"Message": "Key_Error"}
```

2. 게시물 조회

✔️ Sample Call:
$ http POST 127.0.0.1:8000/postings/1

✔️ Success Response:

* Code: 201 "Message": {"user_id": 1,
                      "user_name": "강민지",
                     "posting_id": 1,
                  "posting_title": "django",
                "posting_content": "장고는 프레임워크? 라이브러리?",
                     "created_at": "2021-10-26T04:33:54.408Z",
                     "updated_at": "2021-10-26T04:33:54.408Z"}

✔️ Error Response:
* Code: 404 KeyError Content: {"Message": "Does_Not_Exist_Error"}

3. 게시물 수정

✔️ Sample Call:
$ http PATCH 127.0.0.1:8000/postings/22 title='test12', content='test12'

✔️ Success Response:
* Code: 201 {"Message": "Success!"}

✔️ Error Response:
* Code: 401 KeyError Content: {"Message": "Unauthorized_User"}
* Code: 404 KeyError Content: {"Message": "Not_Existed_Error"}
* Code: 400 KeyError Content: {"Message": "Key_Error"}

4. 게시물 삭제

✔️ Sample Call:
$ http DELETE 127.0.0.1:8000/postings/22

✔️ Success Response:
* Code: 200 {"Message": "Success!"}

✔️ Error Response:
* Code: 401 KeyError Content: {"Message": "Unauthorized_User"}
* Code: 404 KeyError Content: {"Message": "Not_Existed_Error"}

5. 게시물 목록 조회

✔️ Sample Call:
$ http GET 127.0.0.1:8000/postings/list?pagination=4&offset=0

✔️ Success Response:
* Code: 200 {"Message": [{"posting_id": 14, "posting_title": "content21"},
            {"posting_id": 15, "posting_title": "content_test"},
            {"posting_id": 16, "posting_title": "content_test"}]}
    
✔️ Error Response:
* Code: 400 KeyError Content: {"Message": "Key_Error"}

📕 Users app

1.회원가입

✔️ Sample Call:
$ http POST 127.0.0.1:8000/users/signup name="가나다" email="test123456@gmail.com", password="test123456@@@@"

✔️ Success Response:
* Code: 201 {"Message": "Success"}

✔️ Error Response:
* Code: 400 KeyError Content: {"Message": "Key_Error"}
* Code: 400 KeyError Content: {"Message": "Invalid_Password"}
* Code: 400 KeyError Content: {"Message" : "Invalid_Email"}

2.로그인

✔️ Sample Call:
$ http POST 127.0.0.1:8000/users/signin name="가나다" email="test123456@gmail.com", password="test123456@@@@"

✔ Success Response:
* Code: 201 {"Access_Token": <access_token>}

✔️ Error Response:
* Code: 400 KeyError Content: {"Message": "Invalid_Token"}
* Code: 401 KeyError Content: {"Message": "Invalid_User"}
* Code: 400 KeyError Content: {"Message": "Key_Error"}
* Code: 400 KeyError Content: {"Message": "Decode_Error"}
* Code: 404 KeyError Content: {"Message": "Not_Found_Error"}

### 📌 과제 설명

📕 Postings app

✔️ PostingDetailView
1. decorator를 통해 기본적으로 로그인 한 유저만 게시물을 등록, 수정, 삭제할 수 있도록 하였습니다.
2. 특정 게시물을 조회가능하며, 프론트단과의 협의를 통해 로그인하지 않은 유저도 게시물을 조회할 수 있도록 구현 할 수 있습니다.
3. 게시물 수정과 삭제의 경우, 해당 게시물 작성자를 확인한 후 그 작성자만이 수정과 삭제가 가능하도록 구현했습니다.

✔️ PostingListView
1. 페이지네이션을 구현하여 원하는 값을 지정해 그 값만큼 보여줄 수 있도록 구현하였습니다.
2. 게시물의 제목만 조회할 수 있습니다.

📕 Users app

✔️ SignUpView
1. 정규식을 활용해 email과 password에 제약을 걸어주었습니다.
2. bcrypt를 활용해 비밀번호를 해쉬화 하였습니다.

✔️ SignInView
1. 비밀번호 확인 후 db에 있는 사용자 정보와 일치하면 엑세스 토큰을 발행하였습니다.

✔️ decorator([utils.py](http://utils.py/))
1. 로그인시 header에 담겨 받은 Authorization의 value값인 access_token을 확인한 후 복호화하여 user 정보를 확인하는 로직을 구현했습니다.
