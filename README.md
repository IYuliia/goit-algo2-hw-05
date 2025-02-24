### **Task 1: Checking Password Uniqueness Using a Bloom Filter**  

Create a function to check the uniqueness of passwords using a **Bloom filter**. This function should determine whether a password has been used before without storing the actual passwords.  

---

### **Technical Requirements**  

1. **Implement a `BloomFilter` class** that allows adding elements to the filter and checking whether an element exists in the filter.  

2. **Implement the `check_password_uniqueness` function**, which uses an instance of `BloomFilter` to check a list of new passwords for uniqueness. It should return the uniqueness check result for each password.  

3. **Ensure proper handling of all data types**. Passwords should be processed as plain strings without hashing. Empty or invalid values should be accounted for and handled appropriately.  

4. **Optimize for large datasets**, using minimal memory while maintaining efficiency.  


### **Task 2: Comparing HyperLogLog Performance with Exact Unique Count**  

Create a script to compare the exact counting of unique elements with counting using **HyperLogLog**.  

---

### **Technical Requirements**  

1. **Load a dataset** from a real log file (`lms-stage-access.log`) containing **IP address** information.  

2. **Implement a method** to **accurately count unique IP addresses** using a **set** data structure.  

3. **Implement a method** to **estimate unique IP addresses** using **HyperLogLog**.  

4. **Compare the methods** in terms of **execution time** and performance.