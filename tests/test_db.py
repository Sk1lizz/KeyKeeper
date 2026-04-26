from src.database.db_manager import DatabaseManager
from src.utils.paths import get_base_path
from src.models.password_entry import EntryPassword

from pathlib import Path

def get_test_paths() -> Path:
    path = get_base_path() / "tests" / "db" 
    path.mkdir(parents=True, exist_ok=True)

    paths = path / "test.db"

    return paths

def test_db():
    path = get_test_paths()
    Manager = DatabaseManager(db_path=path)

    Manager.vacuum()
    
    entry = EntryPassword(
        title="Test5",
        username="Test@test.test5",
        password="TestPassword5",
        url="https://Test.test5",
        notes="Test note5",
        category="TEST5",
        favorite=0,
        id=6,
    )

    #result = Manager.add_entry(entry=entry)

    #result = Manager.delete_entry(5)

    #result = Manager.get_entry_by_id(6)
    result = Manager.get_all_entries()

    #result = Manager.delete_all_entries()

    #result = Manager.update_entry(entry=entry)


    #result = EntryPassword.to_dict(result)

    for data in result:
        print(data)

    #print(result)

    Manager.close()

def main():
    test_db()