import sqlite3
import pandas as pd
import pathlib

# Your code here....

def main():
    create_database()
    create_tables()
    insert_data_from_csv()

if __name__ == "__main__":
    main()
