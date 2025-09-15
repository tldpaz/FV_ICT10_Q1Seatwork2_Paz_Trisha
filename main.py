# This code uses PyScript (https://pyscript.net/) for Python in the browser.
# Bootstrap CSS framework is used for styling (https://getbootstrap.com/).
# Google Fonts (Poppins) is used for typography (https://fonts.google.com/specimen/Poppins).
# Python dictionary/list syntax from official Python docs (https://docs.python.org/3/tutorial/datastructures.html).
# PyScript display/document usage from PyScript documentation (https://docs.pyscript.net/latest/reference/display.html).
# HTML/CSS structure inspired by Bootstrap documentation and examples.

from pyscript import display, document  # PyScript import

restaurant_name = "About Our Menu!"         # string
owner_name = "Trisha Paz"                   # string
year_established = 2025                     # integer
popular_item_price = 199.99                 # float
has_delivery = True                         # boolean
product_names = ["Classic Burger", "Veggie Wrap", "Chicken Salad"]  # list of strings
business_hours = {"Mon-Fri": "9am-9pm", "Sat-Sun": "10am-8pm"}      # dictionary
menu_prices = {                             # dictionary
    "Classic Burger": 199.99,
    "Veggie Wrap": 149.99,
    "Chicken Salad": 179.99,
    "Fries": 79.99,
    "Iced Tea": 49.99
}
common_allergens = ["Peanuts", "Dairy", "Gluten"]  # list of strings
tax_rate = 0.08                                    # float

# Display at least 5 data points on the webpage using PyScript display()
display(restaurant_name, target="storeName")  # string displayed
display(f"Owner: {owner_name}", target="ownerName")  # string displayed
display(f"Est. {year_established}", target="yearFounded")  # integer displayed as string
display(f"Popular Item Price: ₱{popular_item_price}", target="output1")  # float displayed as string

# Display product names as a string (for reference, see PyScript display docs)
display(f"Products: {', '.join(product_names)}", target="output2")  # list displayed as string

# Display delivery info (boolean to string)
display(f"Delivery Available: {'Yes' if has_delivery else 'No'}", target="output3")  # boolean displayed as string

# Display business hours (dictionary to string)
hours = "; ".join([f"{day}: {time}" for day, time in business_hours.items()])
display(f"Business Hours: {hours}", target="output4")  # dict displayed as string

# Display allergens
display(f"Common Allergens: {', '.join(common_allergens)}", target="output6")  # list displayed as string

# Display tax rate
display(f"Tax Rate: {tax_rate*100}%", target="output7")  # float displayed as percentage

# Calculator function for adding numbers (PyScript event handling)
def adding_numbers(event):
    num1 = document.querySelector("#input1").value  # string
    num2 = document.querySelector("#input2").value  # string
    try:
        result = float(num1) + float(num2)          # float
        display(f"Result: {result}", target="output_calc", append=False)
    except ValueError:
        display("Please enter valid numbers.", target="output_calc", append=False)

# Product images (sources from Bing and The Spruce Eats, see URLs)
product_images = [
    "https://tse3.mm.bing.net/th/id/OIP.Xab5JRx1J3Nv68srGYcvmQHaHa?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",   # Classic Burger
    "https://www.thespruceeats.com/thmb/FSvSeBUSzDD0Wa6-TiXYDLFZx5c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/vegetarian-wraps-88177231-5abc4a71119fa80037df58f8.jpg",     # Veggie Wrap
    "https://tse4.mm.bing.net/th/id/OIP.B2ELzkjkjEsz7BotmblcIgHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"     # Chicken Salad
    # "" for Fries and Iced Tea (no image provided)
]


# Display product names as a list with images (see PyScript DOM manipulation docs)
product_list_html = ""
for name, img in zip(product_names, product_images):
    product_list_html += f'<li class="d-flex align-items-center mb-2"><img src="{img}" alt="{name}" class="me-2 rounded" width="40" height="40">{name}</li>'

document.getElementById("product_list").innerHTML = product_list_html

# Display menu prices as a list (see PyScript DOM manipulation docs)
menu_list_html = ""
for item, price in menu_prices.items():
    menu_list_html += f'<li class="d-flex align-items-center mb-2"><span class="fw-bold me-2">{item}:</span> ₱{price}</li>'

document.getElementById("menu_list").innerHTML = menu_list_html

# References:
# - PyScript: https://pyscript.net/
# - PyScript display/documentation: https://docs.pyscript.net/latest/reference/display.html
# - Bootstrap: https://getbootstrap.com/
# - Google Fonts (Poppins): https://fonts.google.com/specimen/Poppins
# - Python official documentation: https://docs.python.org/3/tutorial/datastructures.html
# - Bing Images: https://www.bing.com/images

# - The Spruce Eats: https://www.thespruceeats.com/
