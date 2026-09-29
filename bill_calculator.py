```python
# Simple Bill Calculator

# Ask the user for the price and quantity
price = float(input("Enter the price of one item: "))
quantity = int(input("Enter the quantity: "))

# Calculate the total
total = price * quantity

# Display a friendly summary using an f-string
print(f"{quantity} items at {price:.2f} each = {total:.2f}")
```

### Example Run

```text
Enter the price of one item: 50
Enter the quantity: 3
3 items at 50.00 each = 150.00
```

### GitHub Submission

Create a repository named:

```text
python-week-1-assignment
```

Upload:

```text
bill_calculator.py
```

Then submit your GitHub repository link.

**Note:** The assignment description says "Week 1" in the submission criteria, but the actual task is the **Simple Bill Calculator** you provided. Use the repository name your instructor specifically requires if they have given you one.
