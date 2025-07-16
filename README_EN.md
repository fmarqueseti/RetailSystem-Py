# RetailSystem-Py

**RetailSystem-Py** is an educational sales management system developed in Python. This project was built as part of the course *"Python from Beginner to Advanced + Artificial Intelligence"*, taught by **Caio Sampaio** from the **Pythonando** platform.

The system offers two versions:
- Text-based interface (console mode)
- Graphical interface using **Tkinter**

Additionally, it integrates with a MySQL relational database.

---

## 📌 Objectives

- Practice core and advanced Python programming concepts
- Integrate relational databases with Python applications
- Develop graphical user interfaces (GUIs) using Tkinter.
- Apply best practices such as code modularization and internationalization

---

## 📁 Project Structure

```
RetailSystem-Py/
│
├── doc/
│   ├── DER.png                 # Entity-Relationship Diagram
│   ├── schema.sql              # Database creation and initial load script
└── src/
    ├── txt/                    # Text-based interface version
    │   ├── myERP.py            # Main script file
    │   ├── mysql_conn.py       # Database connection details (MySQL)
    │   ├── myUtil.py           # Utility functions
    │   ├── ordersMenu.py       # Orders menu
    │   ├── productsMenu.py     # Products menu
    │   └── statisticsMenu.py   # Sales statistics menu (graphs/charts)
    │
    ├── tkinter/                # Graphical interface version (Tkinter)
        ├── myERP.py            # Main application script file
        ├── connection.py       # Database connection class (MySQL)
        ├── login.py            # Login/Signup class
        ├── mainMenu.py         # Main menu class
        ├── ordersList.py       # Orders management class
        ├── productsMenu.py     # Product menu class
        └── statistics.py       # Sales statistics class (graphs/charts)
```

---

## 🧠 Database Structure

The system uses a MySQL relational database with the following main entities:

- **Product**: Product registration with name, ingredients, category, and price
- **Order Item**: Sales record of undelivered items
- **Order History**: Historical sales records of delivered items
- **User**: Access control and authentication

The `schema.sql` script located in the `doc` directory can be used to create and populate the database with sample data.

---

## ⚙️ Business Rules

- Product registration, update, and removal, organized by category
- Sales tracking with delivery status updates
- Sales statistics by revenue and quantity (via charts)

---

## 🌐 Internationalization

The system has been fully adapted to the **English** language, including:
- Complete translation of menus and system messages
- Renaming of database fields and structures
- Standardization of filenames and module names in English

---

## 🧩 Requirements

To run the system, the following Python packages must be installed:

```bash
pip install pymysql matplotlib
```

---

## 🚀 How to Run

### Text-based Interface:

```bash
python3 myERP.py
```

Make sure your MySQL database is configured and accessible. Use the `schema.sql` script to set it up.

---

## 🤝 Contributions

Contributions are welcome and encouraged!  
Feel free to:

- Open **issues** for suggestions or improvements
- Submit **pull requests** with bug fixes or new features
- Share ideas to further enhance the project

---

## 📄 License

This project is licensed under the MIT License.  
See the [licence](https://github.com/fmarqueseti/RetailSystem-Py?tab=MIT-1-ov-file) for more information.

---

## 📚 Credits

Course: *Python from Beginner to Advanced + Artificial Intelligence*  
Instructor: **Caio Sampaio** — [Pythonando](https://www.pythonando.com.br)

Developed and enhanced by: [**Fábio Marques**](https://www.linkedin.com/in/fmrqs/)

---