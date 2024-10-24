# SOLID Principles Study Project

This project is a simple Python application designed to help you study and practice the SOLID principles of object-oriented design. The SOLID principles are a set of five design principles that help developers create more maintainable, understandable, and flexible software.

## SOLID Principles Overview

- **S**: Single Responsibility Principle (SRP)  
  A class should have only one reason to change.
  
- **O**: Open/Closed Principle (OCP)  
  Software entities should be open for extension, but closed for modification.
  
- **L**: Liskov Substitution Principle (LSP)  
  Objects of a superclass should be replaceable with objects of a subclass without affecting the functionality.
  
- **I**: Interface Segregation Principle (ISP)  
  Clients should not be forced to depend on interfaces they do not use.
  
- **D**: Dependency Inversion Principle (DIP)  
  High-level modules should not depend on low-level modules. Both should depend on abstractions.

## Project Structure
├── bad_srp # Bad examples
│ 
└── bad_srp.py 
├── good_srp # Good examples
│ 
└── good_srp.py 
├── model_repo # Models and repository classes 
│ 
├── developer.py 
│ 
├── manager.py 
│ 
├── member.py 
│ 
├── owner.py 
│ 
├── repository.py 
│ 
└── user.py 
├── repo # Repository layer 
│ 
├── reports 
│
│ 
├── parser.py 
│ 
│ 
└── reports_generator.py 
│ 
└── client.py 
├── main.py # Main entry point for running the project 
├── LICENSE 
├── README.md 
└── report.txt 

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Project

1. **Clone the repository** (or download the source code):
    ```bash
    git clone https://github.com/beatriz-cantilho/solid-principles-python
    ```

2. **Navigate to the project directory**:
    ```bash
    cd solid-principles-python
    ```

3. **Run the main program**:
    ```bash
    python3 main.py
    ```

   The `main.py` file will execute code samples demonstrating the SOLID principles.

### Project Details

- **bad_srp/bad_srp.py**: Contains an example of violating the Single Responsibility Principle (SRP).
- **good_srp/good_srp.py**: Contains a correct example adhering to SOLID.
- **model_repo/**: Contains classes representing the business logic and repository models, such as `User`, `Developer`, `Manager`, etc.
- **repo/**: Contains the repository layer for handling data-related operations, including report generation and parsing logic.
- **main.py**: Serves as the entry point, where you can run various examples to see SOLID principles in action.   

### Contributing

Feel free to fork this project, open issues, or submit pull requests if you'd like to contribute or if you spot any bugs.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.