Inventory Management System
Overview
This is an Inventory Management System built using Python and Django, designed to help you efficiently manage and keep track of your inventory. Whether you run a small business or need to organize personal belongings, this system will streamline your inventory control process.

Features
Product Creation: Add new products to your inventory with ease. Provide essential details such as product name, description, quantity, SKU and location.

What's New?

New Graph visualization feature to visualize your inventory products:
the graph includes the quantities of the products as well as to the counts of the added products.

QR Code Integration: Each product/item can be assigned a unique QR code. The QR code enables quick identification and retrieval of product details, simplifying inventory management.

Installation
Ensure you have Python installed. You can download it from the official website: https://www.python.org/downloads/

Clone this repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/Elkrypton/inventory.git
Navigate to the project directory:

bash
Copy code
cd inventory-management
Install the required dependencies:

Copy code
pip install -r requirements.txt
Run the development server:

Copy code
python manage.py runserver
Access the application by visiting http://localhost:8000 in your web browser.

Usage
Creating a Product:

Go to the "Add Product" section in the application.
Fill in the product details, such as name, description, quantity, SKU and location.
Click the "Submit" button to add the product to your inventory.
Assigning a QR Code:

Once you have added products to your inventory, navigate to the "View Items" section.
Select a product from the list and you will be able to retrieve all details of the product including the QR Code.
The QR code will be created and associated with the selected product, making it easily accessible for future identification.
Contribution
Contributions are welcome and encouraged! If you have any ideas for improvements or find any issues, please feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Contact
For any inquiries or support, you can contact the project maintainers at rochdielmajdoub@gmail.com.
