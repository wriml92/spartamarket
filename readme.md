# Spartamarket

&emsp;**Spartamarket**는 Django를 기반으로 한 간단한 온라인 마켓 프로젝트입니다. 회원 가입, 로그인/로그아웃, 프로필 관리와 상품 등록/수정/조회 등의 기능을 포함하고 있습니다.

## 목차

- [Spartamarket](#spartamarket)
  - [목차](#목차)
  - [프로젝트 구조](#프로젝트-구조)
  - [설치 및 실행 방법](#설치-및-실행-방법)
  - [주요 기능](#주요-기능)
  - [디렉토리 상세](#디렉토리-상세)
  - [개발 환경](#개발-환경)
    - [기여 방법](#기여-방법)

---

## 프로젝트 구조

```
.
├── .DS_Store
├── accounts
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── templates
│   │   └── accounts
│   │       ├── login.html
│   │       ├── profile.html
│   │       ├── profile_edit.html
│   │       └── signup.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── media
│   ├── product_images
│   └── profile_images
├── products
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   ├── models.py
│   ├── templates
│   │   └── products
│   │       ├── product_detail.html
│   │       ├── product_form.html
│   │       └── product_list.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── readme.md
├── spartamarket
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static
│   ├── .DS_Store
│   ├── css
│   ├── images
│   │   └── default_profile.png
│   └── js
└── templates
    └── base.html
```

---

## 설치 및 실행 방법

1. **프로젝트 클론**  
   ```bash
   git clone https://github.com/your-username/spartamarket.git
   cd spartamarket
   ```

2. **가상환경 설정(권장)**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # 또는
   venv\Scripts\activate     # Windows
   ```

3. **필요한 패키지 설치**  
   ```bash
   pip install -r requirements.txt
   ```
   > ※ `requirements.txt` 파일이 없을 경우, 직접 `Django`, `Pillow`(이미지 업로드 관련) 등 필요한 라이브러리를 설치하시고, 해당 파일을 생성하시는 것이 좋습니다.

4. **데이터베이스 마이그레이션**  
   ```bash
   python manage.py migrate
   ```

5. **개발 서버 실행**  
   ```bash
   python manage.py runserver
   ```
   > 브라우저에서 `http://127.0.0.1:8000` 접근

---

## 주요 기능

- **계정 관리(`accounts` 앱)**
  - 회원가입, 로그인/로그아웃, 프로필 조회/수정
  - Django 기본 인증 시스템 확장
- **상품 관리(`products` 앱)**
  - 상품 목록, 상품 상세 조회
  - 상품 등록 및 수정
  - 이미지 업로드(프로필, 상품 이미지 등)
- **템플릿 구성(`templates` 디렉토리 공용 + 각 앱 내 templates 폴더)**
  - `base.html`: 전역 레이아웃
  - `accounts/login.html`, `signup.html`, `profile.html` 등
  - `products/product_list.html`, `product_detail.html` 등
- **정적 파일(`static` 디렉토리)**
  - CSS, JS, 이미지 등

---

## 디렉토리 상세

- **accounts/**  
  - `models.py`: 사용자(프로필) 관련 모델 정의  
  - `forms.py`: 회원가입 폼, 프로필 수정 폼 등  
  - `views.py`: 회원가입, 로그인, 프로필 관리 로직  
  - `urls.py`: URL 라우팅 설정  
  - `templates/accounts/`: accounts 앱에서 사용하는 템플릿

- **products/**  
  - `models.py`: 상품 관련 모델 정의  
  - `forms.py`: 상품 등록/수정 폼  
  - `views.py`: 상품 목록, 상세, 등록, 수정 로직  
  - `urls.py`: URL 라우팅 설정  
  - `templates/products/`: products 앱에서 사용하는 템플릿

- **media/**  
  - `product_images/`: 상품 이미지 업로드 폴더  
  - `profile_images/`: 프로필 이미지 업로드 폴더

- **static/**  
  - 공용 CSS, JS, 이미지 파일 등 정적 자원 관리

- **templates/**  
  - `base.html`: 사이트 전역 레이아웃 템플릿  
  - 다른 앱에서 공용으로 사용될 가능성이 있는 템플릿이나, 프로젝트 레벨에서 관리하고 싶은 템플릿 등

- **spartamarket/**  
  - `settings.py`: Django 설정 파일  
  - `urls.py`: 프로젝트 전역 라우팅  
  - `wsgi.py`, `asgi.py`: 서버 구동 관련 설정 파일

- **manage.py**  
  - Django 명령어를 실행할 때 사용하는 스크립트

---

## 개발 환경

- **Python**: 3.10
- **Django**: 4.2
- **DB**: SQLite (개발/테스트 용도)
- **기타 라이브러리**: Pillow(이미지 처리), etc.

---

### 기여 방법

프로젝트에 기여를 원하시면 이슈를 생성하거나 Pull Request를 보내주세요.

**문의 사항**  
이메일: [your-email@example.com](mailto:your-email@example.com)  
프로젝트에 관해 궁금한 점이 있으면 언제든 연락 바랍니다.

---

이상으로 **spartamarket** 프로젝트의 예시 README입니다. 필요에 따라 내용을 자유롭게 수정/추가하셔서 사용하시면 됩니다. 감사합니다.