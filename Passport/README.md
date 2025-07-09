# Digital Passport System – COMP517 Coursework

MSc Data Science and Artificial Intelligence  
University of Liverpool

This project implements a digital passport system in Python, developed as part of the COMP517 module. The aim was to design a `Passport` class that models digital passport data using object-oriented programming principles and complies with modern software development standards.

## Features

The `Passport` class provides:

- Object-oriented structure with class and instance variables
- Automatic assignment of unique passport numbers using a class-level counter
- Date handling using Python's `datetime` and compliance with ISO 8601 format
- Personal information encapsulation (name, birth date, nationality, expiry date)
- Future extensibility for travel tracking and authentication systems

## Functionality

Each passport object contains core identity data and includes:

- `__init__`: Initializes a passport instance with validated date fields
- `passport_id`: Automatically assigned unique identifier
- (Expected) Additional methods such as:
  - `is_valid`: Check if the passport is still valid
  - `check_data`: Verify personal identity information
  - `summary`: Return a human-readable passport overview
  - `stamp`: Record visits to countries
  - `countries_visited`, `times_visited`: Track and count entries
  - `sum_square_visits`: Calculate travel activity score

> Note: Some methods may be included in extended or bonus implementations.

## Testing

Test cases are provided within the `if __name__ == "__main__"` block for demonstration and validation purposes.  
The class is modular and can be imported into other systems for reuse and testing.

## Disclaimer

This project was submitted as part of assessed coursework and is shared for **educational and portfolio purposes only**.  
Please **do not reuse or submit this code for academic credit**.

## Attribution

- Module: COMP517 – Programming
- Program: MSc Data Science and AI
- Institution: University of Liverpool
- Author: Jintaek Uh
- © 2025 Jintaek Uh
