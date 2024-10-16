import sqlite3
import read_data

# Connect to SQLite database (or create it)
conn = sqlite3.connect('esg_data.db')
cursor = conn.cursor()

# Get company list and read data
company_list = ['2330 - 台積電', '3711 - 日月光投控', '2454 - 聯發科', '2303 - 聯電', '2379 - 瑞昱']
company_data = read_data.read_company_data(company_list)

# Extract company names
company_name = []
for company in company_list:
    id, name = company.split(' - ')
    company_name.append(name)

# Function to check if category exists in the corresponding category table
def category_exists(category, topic):
    if topic == '環境':
        cursor.execute('SELECT id FROM e_category_table WHERE category_name = ?', (category,))
    elif topic == '社會':
        cursor.execute('SELECT id FROM s_category_table WHERE category_name = ?', (category,))
    elif topic == '治理':
        cursor.execute('SELECT id FROM g_category_table WHERE category_name = ?', (category,))
    return cursor.fetchone() is not None  # Return True if exists, False otherwise

# Function to check if norm exists in the corresponding norm table
def norm_exists(norm, topic):
    if topic == '環境':
        cursor.execute('SELECT id FROM e_norm_table WHERE norm = ?', (norm,))
    elif topic == '社會':
        cursor.execute('SELECT id FROM s_norm_table WHERE norm = ?', (norm,))
    elif topic == '治理':
        cursor.execute('SELECT id FROM g_norm_table WHERE norm = ?', (norm,))
    return cursor.fetchone() is not None  # Return True if exists, False otherwise

# Function to insert data into the respective data table only if category and norm exist
def insert_data(company_id, topic, category, norm, value):
    # Check if category exists
    if not category_exists(category, topic):
        print(f"Skipping {topic} - {category} - {norm}: Category not found")
        return

    # Check if norm exists
    if not norm_exists(norm, topic):
        print(f"Skipping {topic} - {category} - {norm}: Norm not found")
        return

    if topic == '環境':  # Insert into e_data_table
        cursor.execute('''
            INSERT INTO e_data_table (company_id, category_id, norm_id, value)
            VALUES (
                (SELECT id FROM company_table WHERE name = ?),
                (SELECT id FROM e_category_table WHERE category_name = ?),
                (SELECT id FROM e_norm_table WHERE norm = ?),
                ?
            )''', (company_id, category, norm, value))

    elif topic == '社會':  # Insert into s_data_table
        cursor.execute('''
            INSERT INTO s_data_table (company_id, category_id, norm_id, value)
            VALUES (
                (SELECT id FROM company_table WHERE name = ?),
                (SELECT id FROM s_category_table WHERE category_name = ?),
                (SELECT id FROM s_norm_table WHERE norm = ?),
                ?
            )''', (company_id, category, norm, value))

    elif topic == '治理':  # Insert into g_data_table
        cursor.execute('''
            INSERT INTO g_data_table (company_id, category_id, norm_id, value)
            VALUES (
                (SELECT id FROM company_table WHERE name = ?),
                (SELECT id FROM g_category_table WHERE category_name = ?),
                (SELECT id FROM g_norm_table WHERE norm = ?),
                ?
            )''', (company_id, category, norm, value))

# Insert data into tables
index = 0
for company in company_data:
    name = company_name[index]
    company_id = cursor.execute('SELECT id FROM company_table WHERE name = ?', (name,)).fetchone()[0]

    for data in company:
        topic = data[0]
        category = data[1]
        norm = data[2]
        value = data[3] if topic == '環境' else data[4]
        print(f"{name},{topic},{category},{norm},{value}")
        # Insert the data into the appropriate table based on the topic
        insert_data(name, topic, category, norm, value)

    index += 1

# Commit the changes and close the connection
conn.commit()
conn.close()
