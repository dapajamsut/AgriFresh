class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = []
        # Check if the key already exists and update it
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        # If key does not exist, append the new key-value pair
        self.table[index].append([key, value])

    def delete(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return False
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                self.table[index].pop(i)
                return True
        return False

    def search(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            return None
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def display(self):
        for i, pairs in enumerate(self.table):
            if pairs:
                print(f"Index {i}: {pairs}")

# Create a HashTable instance
db = HashTable(10)

# Insert data into the hash table
db.insert("name", "John Doe")
db.insert("name", "Sum ting wong")
db.insert("email", "john@example.com")
db.insert("phone", "123-456-7890")
db.insert("Adress", "Wazero Street")

# Display the hash table
db.display()

# Search for a key
print("Search 'email':", db.search("email"))
print("Search 'Adress' :", db.search("Adress"))
print("Search 'Age':", db.search("Age"))
# Delete a key
print("Delete 'phone':", db.delete("phone"))

# Display the hash table after deletion
db.display()
