# Online Video Game Rental System

This is a web application built using MySQL, PHP, HTML, and CSS,Python Streamlit, where users can rent physical copies of video games and admins can manage the available games and perform CRUD operations. Part of the the admin dashboard is built using Streamlit.

## Screenshots
![image](https://user-images.githubusercontent.com/83999960/225119207-e767bdef-982f-4d29-919a-90c5869865e4.png)
![image](https://user-images.githubusercontent.com/83999960/225107349-b2f16f2d-6656-4f65-9632-aae80a5ca808.png)
![image](https://user-images.githubusercontent.com/83999960/225107421-815dedb6-9f93-4320-ade6-833fc396744e.png)
![image](https://user-images.githubusercontent.com/83999960/225107466-149c6388-65eb-447c-b203-ba5dd79d9c1a.png)
![image](https://user-images.githubusercontent.com/83999960/225107604-e89c3f49-349e-44b7-9cf7-0ce16d8c6532.png)
User Can now view his currently borrowed games in Return Now Section-
![image](https://user-images.githubusercontent.com/83999960/225107645-bc92dcc3-693a-4e45-bef1-87b8d6002b62.png)
Current and past Bookings
![image](https://user-images.githubusercontent.com/83999960/225107815-9e3eebd0-2120-49c3-989a-4268e6854580.png)
![image](https://user-images.githubusercontent.com/83999960/225107955-2105e3b1-584e-42ea-a8d6-f861c2a119dc.png)
### ADMIN Dashboard
![image](https://user-images.githubusercontent.com/83999960/225108069-66da4b7b-676e-4be5-b9a8-8b6e623f2665.png)
![image](https://user-images.githubusercontent.com/83999960/225108188-0c0c048a-9260-4e53-bd4c-8dbaffada5b4.png)
![image](https://user-images.githubusercontent.com/83999960/225108261-6fae1a02-352c-4c3b-af94-a85aa8b3ac3c.png)
![image](https://user-images.githubusercontent.com/83999960/225108311-d6c21d7a-44c6-4e38-a2d7-e67444415031.png)


## Features

- User login and registration
- Choose games from a list of available games
- Select the rental duration
- Rent games
- Return rented games
- Admin login to access dashboard
- Add, delete, and update games
- Execute SQL queries from the admin dashboard

## Technologies Used

- MySQL
- PHP
- HTML
- CSS
- XAMPP
- Streamlit

## Getting Started

To get started, follow these steps:

1. Install XAMPP on your system
2. Clone this repository into the `htdocs` folder in your XAMPP directory
3. Import the `videogamerental.sql` file into your MySQL server
4. Update the database credentials in `connection.php`
5. Run the XAMPP server
6. Navigate to `http://localhost/video-game-rental-system` in your web browser

To run the admin dashboard, follow these additional steps:

1. Install Streamlit using `pip install streamlit`
2. Navigate to the project directory in your terminal
3. Run `streamlit run dashboard.py`
4. The Streamlit app should open in your default web browser

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
