import sqlite3
import check_data
# Connect to SQLite database (or create it)
conn = sqlite3.connect('esg_data.db')
cursor = conn.cursor()

# Create tables
def create_tables():
    # Company table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS company_table (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )''')
    
    # Norm Tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS e_norm_table (
        id INTEGER PRIMARY KEY,
        norm TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS s_norm_table (
        id INTEGER PRIMARY KEY,
        norm TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS g_norm_table (
        id INTEGER PRIMARY KEY,
        norm TEXT NOT NULL
    )''')
    
    # Category Tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS e_category_table (
        id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS s_category_table (
        id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS g_category_table (
        id INTEGER PRIMARY KEY,
        category_name TEXT NOT NULL
    )''')
    
    # Data Tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS e_data_table (
        company_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        norm_id INTEGER NOT NULL,
        value TEXT,
        PRIMARY KEY (company_id, category_id, norm_id),
        FOREIGN KEY (company_id) REFERENCES company(id),
        FOREIGN KEY (category_id) REFERENCES e_category_table(id),
        FOREIGN KEY (norm_id) REFERENCES e_norm_table(id)
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS s_data_table (
        company_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        norm_id INTEGER NOT NULL,
        value TEXT,
        PRIMARY KEY (company_id, category_id, norm_id),
        FOREIGN KEY (company_id) REFERENCES company(id),
        FOREIGN KEY (category_id) REFERENCES s_category_table(id),
        FOREIGN KEY (norm_id) REFERENCES s_norm_table(id)
    )''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS g_data_table (
        company_id INTEGER NOT NULL,
        category_id INTEGER NOT NULL,
        norm_id INTEGER NOT NULL,
        value TEXT,
        PRIMARY KEY (company_id, category_id, norm_id),
        FOREIGN KEY (company_id) REFERENCES company(id),
        FOREIGN KEY (category_id) REFERENCES g_category_table(id),
        FOREIGN KEY (norm_id) REFERENCES g_norm_table(id)
    )''')

def insert_company(company_list):
    for company in company_list:
        company_id, company_name = company.split(' - ')
        cursor.execute("INSERT INTO company_table (id, name) VALUES (?, ?)", (company_id, company_name))

# Insert into category and norm table
def insert_cateegory_norm(data, category_table, norm_table):
    for category, norms in data.items():
        cursor.execute(f"INSERT INTO {category_table} (category_name) VALUES (?)", (category,))
        
        for norm in norms:
            cursor.execute(f"INSERT INTO {norm_table} (norm) VALUES (?)", (norm,))
            
# Create tables
create_tables()
company_list = ['2330 - 台積電', '3711 - 日月光投控', '2454 - 聯發科', '2303 - 聯電', '2379 - 瑞昱']
insert_company(company_list)

E_data, S_data, G_data = check_data.check(company_list)
# Populate tables with sample data
insert_cateegory_norm(E_data, 'e_category_table', 'e_norm_table')
insert_cateegory_norm(S_data, 's_category_table', 's_norm_table')
insert_cateegory_norm(G_data, 'g_category_table', 'g_norm_table')

# Commit and close connection
conn.commit()
conn.close()

print("Database and tables created and populated successfully.")