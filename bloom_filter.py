import hashlib

class BloomFilter:
    def __init__(self, size=1000, num_hashes=3):
      
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
       
        hash_values = []
        for i in range(self.num_hashes):
            hash_value = int(hashlib.md5(f"{item}{i}".encode()).hexdigest(), 16) % self.size
            hash_values.append(hash_value)
        return hash_values

    def add(self, item):
       
        if not isinstance(item, str) or not item.strip():
            return  
        
        for hash_value in self._hashes(item):
            self.bit_array[hash_value] = 1

    def contains(self, item):
      
        if not isinstance(item, str) or not item.strip():
            return False  
        
        return all(self.bit_array[hash_value] for hash_value in self._hashes(item))


def check_password_uniqueness(bloom_filter, passwords):
  
    results = {}
    for password in passwords:
        if bloom_filter.contains(password):
            results[password] = "already in use"  
        else:
            results[password] = "unique" 
            bloom_filter.add(password) 
    return results


if __name__ == "__main__":
    
    bloom = BloomFilter(size=1000, num_hashes=3)

    existing_passwords = ["password123", "admin123", "qwerty123"]
    for password in existing_passwords:
        bloom.add(password)

    new_passwords_to_check = ["password123", "newpassword", "admin123", "guest"]
    results = check_password_uniqueness(bloom, new_passwords_to_check)

    for password, status in results.items():
        print(f"Password '{password}' — {status}.")
