## ✍️ [위코드 x 원티드] 백엔드 프리온보딩 선발 과제: 게시판 CRUD API
#### Django 활용한 질문, 댓글, 좋아요 기능 구현
#### Contact: 박은혜, ehye0922@gmail.com, 010-5158-4536

#### 📌 URL
* 가상환경 정보

$ conda create -n pre_onboarding python=3.9.7

$ conda activate pre_onboarding

* 접속 정보

$ cd pre_onboarding

$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py runserver

* DB

DB: sqlite3

$ sqlite3 db.sqlite3

#### 📌 Endpoing 호출
1. PostingDetailView
* POST   /postings
* GET    /postings/<int:posting_id>
* PATCH  /postings/<int:question_id>
* DELETE /postings/<int:question_id>

2. PostingListView
* GET /postings/list

3. SignUpView
* POST /users/signup

4. SignInView
* POST /users/signin

#### 📌 API 명세 (ex.PostingListView)
#### * Sample Call:
$ http GET 127.0.0.1:8000/postings/list?pagination=0&limit=3

#### * Success Response:
* Code: 200 "Message": [{"posting_id": 1, "posting_title": "django"},....]
  
#### * Error Response:
* Code: 400 KeyError Content: { 'Message': 'Key_Error' }

#### 📌 과제 설명
📕 Postings app

* PostingDetailView
1. decorator를 통해 기본적으로 로그인 한 유저만 게시물을 등록, 수정, 삭제할 수 있도록 하였습니다.
2. 특정 게시물을 조회가능하며, 게시물 조회의 경우에는 데코레이터의 유무를 프론트단과의 협의를 통해 로그인하지 않은 유저도 게시물을 조회할 수 있도록 수정할 수 있습니다.
3. 게시물 수정과 삭제의 경우, 해당 게시물 작성자를 확인한 후 그 작성자만이 수정과 삭제가 가능하도록 구현했습니다.

* PostingListView
1. 페이지네이션을 구현하여 원하는 값을 지정해 그 값만큼 보여줄 수 있도록 구현하였습니다.
2. 게시물의 제목만 조회할 수 있습니다.

📕 Users app

* SignUpView
1. 정규식을 활용해 email과 password에 제약을 걸어주었습니다.
2. bcrypt를 활용해 비밀번호를 해쉬화 하였습니다.

* SignInView
1. 비밀번호 확인 후 db에 있는 사용자 정보와 일치하면 엑세스 토큰을 발행하였습니다.

* decorator(utils.py)
1. 로그인시 header에 담겨 받은 Authorization의 value값인 access_token을 확인한 후 복호화하여 user 정보를 확인하는 로직을 구현했습니다.
