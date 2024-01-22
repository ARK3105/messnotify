from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import io

driver = webdriver.Chrome()  # Replace with your preferred browser

driver.get("https://mess.iiit.ac.in")  # Replace with actual URL

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

username_field = driver.find_element(By.ID, "username")  # Replace with appropriate locators
password_field = driver.find_element(By.NAME, "password")
login_button = driver.find_element(By.NAME, "submit")



########   TYPE USERNAME AND PASSWORD HERE  #############


username_field.send_keys("")  #PUT USERNAME AS <usename>@s OR <username>@r SINCE THE PAGE AUTOCOMPLETES IT

# WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "username")))
password_field.send_keys("")
login_button.click()


##############

        


# Wait for the sidebar to be present
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#sidebar1')))

# Click on the "View Mess Registration" link using CSS selector
mess_registration_link = driver.find_element(By.CSS_SELECTOR, '#sidebar1 a[href="student_view_registration.php"]')
mess_registration_link.click()

# Wait for the content to be present (you might need to adjust this)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'content')))


# Your further actions or assertions can be added here

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'calendar')))

table_element = driver.find_element(By.CLASS_NAME, 'calendar')

table_df = pd.read_html(io.StringIO(table_element.get_attribute('outerHTML')))[0]



table_df.to_csv('calendar_data.csv', index=False)

driver.get("https://iiit-mess.in/")  # Replace with actual URL

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'MuiTable-root')))

# Find the table element using its class name
table_element2 = driver.find_element(By.CLASS_NAME, 'MuiTable-root')

# Use pandas to read the HTML table and convert it to a DataFrame
table_df2 = pd.read_html(io.StringIO(table_element2.get_attribute('outerHTML')))[0]

# Save the DataFrame to a CSV file
table_df2.to_csv('mess_data.csv', index=False)

driver.quit()


#time.py

from datetime import datetime, time

# Define the time interval
start_time = time(15, 0)   # 8:00 AM
end_time = time(16, 0)    # 12:00 PM

# Get the current time
current_time = datetime.now().time()

current_hour = current_time.hour
current_time = current_time.min

# Get the current date and time
current_datetime = datetime.now()

# Extract and print the current day as an integer
current_day = current_datetime.day

#time.py



if current_hour < 9:
    meal = 'B'
elif current_hour < 2:
    meal = 'L'
else:
    meal = 'D'



#mess.py
    
import csv

def find_entry(day, meal_type, file_path='calendar_data.csv'):
    with open(file_path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        # Skip the header row
        next(reader, None)
        
        for row in reader:
            for r in row:
                if r:
                    day_number, meals = r.split(maxsplit=1)
                    if int(day_number) != day:
                        continue
                    
                    for meal in meals.split(")"):
                        if meal.endswith(meal_type):
                            return meal[:-2].strip()
                    

    # If no matching entry is found
    return None

# Example usage
day_input = current_day
meal_type_input = meal


result = find_entry(day_input, meal_type_input)
if result == "Yuktahaar":
    mess_name = "Yuktahar"
elif result == "Kadamb":
    mess_name = "Kadamba"
elif result == "South":
    mess_name = "SouthMess"
elif result == "North":
    mess_name = "NorthMess"

# Now mess_name contains the appropriate value based on the conditions



#mess.py
    


#menu.py
    

    

   

def get_menu_items(meal_type, mess_type, file_path='mess_data.csv'):
    mess_type=mess_name
    
    ret = []
    with open(file_path) as f:
        rows = csv.reader(f)
        ind = next(rows).index(mess_type)
        for row in rows:
            if row[0].startswith(meal_type):
                ret.append(row[ind])
  
    
    return ret

# Example usage
meal_type_input = meal
mess_type_input = result

query_input = f"{meal_type_input} {mess_type_input}"
menu_items = get_menu_items(meal_type_input, mess_type_input)

if menu_items:
    if meal=='D':
        food = "dinner"
    if meal == 'L':
        food = "lunch"
    if meal == 'B':
        food = "breakfast"
    
    # print(f"The menu items for {food} at {result} are: {', '.join(menu_items)}")
else:
    print(f"No menu items found for {query_input}")


#menu.pyMeal,NorthMess,SouthMess,Kadamba,Yuktahar
    

#msg.py
    
from twilio.rest import Client

account_sid = 'ACff60809ae10b73af839448dbab7bf162'
auth_token = 'fa469688f03cbb2aba5227535bc937c2'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17079690833',  # Removed single quotes around the phone number
    body=f"The menu items for {food} at {result} are: {', '.join(menu_items)}",



    ##########   TYPE YOUR PHONE NUMBER HERE   #########
    to=''        

)

print(message.sid)

#msg.py

        
        





# input("Press Enter to close the browser")

# Quit the driver to close the browser window

# Perform other actions as needed
