# Condor Elite Towncar Service CRM Database

![Tech Stack](https://img.shields.io/badge/Stack-Python%2FPSQL-darkgreen?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

A full-stack progressive web application designed for car trip reservation handling and clientele management

## Overview

This application, Condor Elite Towncar Reservation System, transforms the client trip booking and management process for a town car service. Developed specifically for Condor Elite's owner, the system replaces manual paper logs with a streamlined, digital interface.

The primary function is to serve as a single source of truth for all client reservations. It allows the owner to quickly input, view, and organize trip details—including pickup times, destinations, passenger names, and special notes and immediately review a prioritized list of the next five upcoming reserved trips, ensuring operational efficiency and eliminating errors common with physical records.

## Screenshots

### Login View: Login authentication

This is the screen the user sees before logging in

![Login Page](../assets/dashboard.JPEG)

### Dashboard View: Upcoming Reservations

This is the primary screen, showing the immediate trips

![Dashboard](../assets/dashboard.JPEG)

### Booking List View: All reservation entries

Sorted by most recent reservations, this is where the user can view past and upcoming reservations

![Booking List Page](../assets/reservations.PNG)

### Booking Form View: Input fields

Single page form that documents all trip variables including date, time, pick.dropoff locations. Client dropdown to ensure accurate data entry before submission to PostgreSQL database.

![Reservation Form](../assets/add_booking.JPEG)

### Client Form View

Form that documents and ensures accurate contact information is recordsd for repeated business

![Client Form](../assets/add_client.PNG)

### Reservation Detail View

This view Consolidates all necessary data for a specific trip

![Reservation Details Page](../assets/booking_details.PNG)

Key Features & Implementation
Custom PostgreSQL Data Model: Designed and implemented a robust relational database schema in PostgreSQL to manage three primary entities: Clients, Reservations, and Trips. This structure ensures data integrity and allows for efficient, complex queries (e.g., retrieving the next 5 upcoming trips).

RESTful API Development: Utilized the Python framework Django to build a comprehensive set of CRUD (Create, Read, Update, Delete) endpoints, specifically for reservation management and client updates.
Front-End Interactivity: Used vanilla JavaScript to enhance the user experience on the client-side, including features like real-time form validation on the reservation input page to reduce data entry errors.

Responsive Design: Employed Bootstrap 5 to structure the entire application, guaranteeing a fully responsive interface that is usable on both desktop and mobile devices for immediate trip review.

## Technical Stack

- **Backend & Framework:** Python, Django
- **Database:** PostgreSQL (Managed via Django ORM)
- **Frontend:** HTML5, JavaScript
- **Styling & UI:** Bootstrap 5, Custom CSS

## ⚙️ Quick Start (Local Installation)

To run the **Condor Elite Reservation System** locally, follow these steps. All commands are run from the project's root directory.

### 1. Project Setup and Dependencies

1.  **Clone the Repository and Navigate:**
    ```bash
    git clone [https://github.com/bjohn20/Condor_Towncar_CRM.git](https://github.com/bjohn20/Condor_Towncar_CRM.git)
    cd dcrm  # Assuming 'dcrm' is the project root after cloning
    ```
2.  **Create and Activate a Virtual Environment:** This isolates the project's Python dependencies.
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows, use: .\myenv\Scripts\activate
    ```
3.  **Install Required Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### 2. Database Configuration (Crucial for PostgreSQL/Django)

4.  **Set Environment Variables:** Create a file named **`.env`** in the root directory and add your secret and database connection details.
    ```
    # Example content for .env file
    SECRET_KEY=your_secure_random_key_here
    DATABASE_URL=postgres://user:password@localhost:5432/condor_reservations
    ```
    **(Note: Ensure your local PostgreSQL server is running.)**
5.  **Apply Database Migrations:** This builds the necessary tables in your PostgreSQL database.
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

### 3. Running the Application

6.  **Create a Superuser (Admin Account):** This account is necessary to log in and use the application.
    ```bash
    python manage.py createsuperuser
    ```
7.  **Start the Development Server:**
    ```bash
    python manage.py runserver
    ```
    The application will now be running and accessible in your web browser at: **`http://127.0.0.1:8000/`**.
