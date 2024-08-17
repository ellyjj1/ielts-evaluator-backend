# Magic 7+ IELTS Writing Evaluator

## 1. Introduction

Magic 7+ is an AI-powered tool designed to help IELTS candidates improve their writing skills. It evaluates your essays based on four key aspects: Task Achievement and Response, Coherence and Cohesion, Lexical Resources, and Grammatical Range and Accuracy. By using this tool, you can receive detailed feedback and a score that mimics the evaluation standards of IELTS examiners.

Front-end: https://github.com/ellyjj1/ielts-evaluator-frontend

Back-end: https://github.com/ellyjj1/ielts-evaluator-backend

## 2. How to Install

### Backend (Django)

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/yourusername/ielts-writing-evaluator.git
## 2. How to Install

### Backend (Django)

1. **Navigate to the Project Directory**:
    ```sh
    cd ielts-writing-evaluator-backend
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```

4. **Install the Required Packages**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**:
    - Create a `.env` file in the project root and add your environment variables:
        ```env
        SECRET_KEY=your_django_secret_key
        CHATGPT_API_KEY=your_openai_api_key
        ```

### Frontend (React)

1. **Navigate to the Frontend Directory**:
    ```sh
    cd ielts-writing-evaluator-frontend
    ```

2. **Install the Required Packages**:
    ```sh
    npm install
    ```

3. **Set Up Environment Variables**:
    - Create a `.env` file in the frontend root and add:
        ```env
        REACT_APP_BASE_URL=http://localhost:8000/
        REACT_APP_CHATGPT_API_KEY=your_openai_api_key
        ```

## 3. How to Start

### Backend (Django)

1. **Run Migrations**:
    ```sh
    python manage.py migrate
    ```

2. **Start the Django Development Server**:
    ```sh
    python manage.py runserver
    ```

### Frontend (React)

1. **Start the React Development Server**:
    ```sh
    npm start
    ```

The React app will start on `http://localhost:3000/` and the Django backend will run on `http://localhost:8000/`.

## 4. How to Use

1. **Access the Application**:
    - Open your browser and go to `http://localhost:3000/`.

2. **Evaluate Your Writing**:
    - Navigate to the writing evaluation page.
    - Paste or type your IELTS essay into the text area.
    - Click "Submit" to receive detailed feedback and scores.

3. **Review Feedback**:
    - Review the feedback provided by the AI, which will include suggestions for improvement and overall scores based on IELTS standards.
