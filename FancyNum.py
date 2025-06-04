def is_sequence(num_str):
    # Check for ascending or descending sequence of digits
    ascending = all(int(num_str[i]) + 1 == int(num_str[i+1]) for i in range(len(num_str)-1))
    descending = all(int(num_str[i]) - 1 == int(num_str[i+1]) for i in range(len(num_str)-1))
    return ascending or descending

def is_same_number(num_str):
    return len(set(num_str)) == 1

def is_repeated_pairs(num_str):
    # Check for pattern like AABB
    return num_str[0] == num_str[1] and num_str[2] == num_str[3] and num_str[1] != num_str[2]

def is_palindrome(num_str):
    return num_str == num_str[::-1]

def is_catchy(num_str):
    return (is_sequence(num_str) or 
            is_same_number(num_str) or 
            is_repeated_pairs(num_str) or
            is_palindrome(num_str))

def generate_fancy_numbers(start, end):
    fancy_numbers = []
    for num in range(start, end + 1):
        num_str = f"{num:04d}" 
        if is_catchy(num_str):
            fancy_numbers.append(num_str)
    return fancy_numbers

def main():
    print("Fancy Car Number Generator (4-digit numbers)")
    start = int(input("Enter start of range (4-digit number): "))
    end = int(input("Enter end of range (4-digit number): "))

    if start < 0 or end < 0 or len(str(start)) > 4 or len(str(end)) > 4 or start > end:
        print("Please enter a valid range of four-digit numbers.")
        return

    fancy_numbers = generate_fancy_numbers(start, end)

    print(f"\nFancy numbers between {start:04d} and {end:04d}:")
    for number in fancy_numbers:
        print(number)

if __name__ == "__main__":
    main()
