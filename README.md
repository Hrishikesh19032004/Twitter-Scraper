# Twitter Scraper with React and Flask
![image](https://github.com/user-attachments/assets/6ea16afb-83d7-4e6a-854c-16f1cffd4ccd)

## Overview

This project is a Twitter Scraper that allows users to fetch Twitter profile data for a given list of Twitter URLs. The data is retrieved via a Flask backend API that scrapes the necessary details, which are then displayed in the frontend built using React.

### Features

- Scrapes Twitter profiles using a Flask API.
- Displays the profile information in a grid of cards on the frontend.
- Provides details such as profile picture, username, bio, followers, following, location, and website.
- Responsive and user-friendly UI, optimized for displaying multiple profiles.

## Technologies Used

- **React**: A powerful JavaScript library for building user interfaces, chosen for its flexibility, component-based architecture, and ease of integrating with REST APIs.
- **Flask**: A lightweight Python web framework, selected for its simplicity in setting up the backend API to handle scraping requests.
- **Axios**: A promise-based HTTP client for making requests from the React frontend to the Flask backend.
- **CSS**: For styling the application and ensuring it is visually appealing and responsive.

## Why React and Flask?

### Why React?
1. **Component-based Architecture**: React allows breaking down the application into small reusable components (e.g., profile cards), making the code more modular and maintainable.
2. **Efficient Rendering**: React’s virtual DOM allows efficient updates and re-renders, ensuring a smooth user experience even with multiple profile cards being displayed.
3. **Easy Integration with APIs**: React's compatibility with tools like Axios makes it easy to fetch data from external APIs, such as our Flask backend.

### Why Flask?
1. **Lightweight and Simple**: Flask is a micro-framework that’s easy to set up and use, making it perfect for small to medium-sized applications like this one where we need to scrape and serve data from external sources.
2. **Flexibility**: Flask is unopinionated, meaning we can easily integrate various Python libraries (like BeautifulSoup for scraping) and structure the app based on our requirements.
3. **RESTful API Support**: Flask's simplicity in creating REST APIs allows seamless communication between the frontend (React) and backend (Flask).

## Data Flow

### 1. Frontend (React):
1. The user interacts with the React frontend, clicking the "Fetch Data" button.
2. A request is sent to the Flask backend using **Axios**.
3. The backend processes the request and scrapes the Twitter profile data.
4. The scraped data is returned as a JSON response to the React frontend.
5. React processes and stores the data in the component state using the **useState** hook.
6. The state is used to dynamically generate a series of cards for each user profile, displaying the relevant data (profile image, bio, followers count, etc.).

### 2. Backend (Flask):
1. The Flask server listens for POST requests from the React frontend.
2. Upon receiving a request with a list of Twitter URLs, Flask uses the **BeautifulSoup** library (or any scraping tool) to fetch data from the specified profiles.
3. The data is then processed, formatted, and sent back as a JSON response to the frontend.
4. Flask ensures that the scraping logic is handled asynchronously and is optimized for performance.
![Screenshot (353)](https://github.com/user-attachments/assets/3b67d458-d371-406c-88e6-d589cbbb5eda)

### Data Flow Diagram (High-Level Overview)

```plaintext
+------------------+    Request    +-------------------+
|                  | ------------> |                   |
|   React Frontend |               |    Flask Backend  |
|                  | <------------ |                   |
|  (User Clicks    |    Response   |                   |
|   "Fetch Data")  |               |                   |
+------------------+               +-------------------+
        |                                    |
        |                                    |
        V                                    V
  +-------------+                      +------------------+
  |  Display    |                      |   Scrape Twitter |
  |  Profile    |                      |   Data (BeautifulSoup) |
  |  Cards      |                      |   Process Data    |
  +-------------+                      +------------------+
```

### Example Data Flow:
1. **User Action**: The user clicks "Fetch Data".
2. **Frontend (React)**: React sends a POST request to the Flask API with a list of Twitter URLs.
3. **Backend (Flask)**: Flask scrapes the profile data and returns a JSON object with details (profile image, username, bio, etc.).
4. **Frontend (React)**: React stores the data in state and dynamically renders the profile cards.

## How to Run the Application

### Prerequisites:
- Node.js (for React)
- Python 3 (for Flask)
- npm (for managing JavaScript dependencies)

### Setup:

#### 1. **Frontend (React)**:
1. Clone the repository.
2. Navigate to the `frontend` directory.
3. Run the following commands to install dependencies and start the React app:
    ```bash
    npm install
    npm start
    ```

#### 2. **Backend (Flask)**:
1. Navigate to the `backend` directory.
2. Set up a virtual environment and activate it (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3. Install required Python libraries:
    ```bash
    pip install flask beautifulsoup4 requests
    ```
4. Start the Flask server:
    ```bash
    python app.py
    ```

The React frontend will be running on `http://localhost:3000`, and the Flask API will be running on `http://localhost:7000`.

### Notes:
- Ensure that the Flask API is up and running before fetching data from the frontend.
- The Twitter scraping logic may be subject to rate-limiting or changes in Twitter’s structure, so this might need updating periodically.

## Conclusion

This project combines the power of React and Flask to create a lightweight, responsive Twitter scraper. React's component-based architecture makes it ideal for creating dynamic, interactive user interfaces, while Flask provides a simple and efficient way to handle backend requests and web scraping. The combination of these technologies offers a robust solution for web scraping with a modern frontend.
