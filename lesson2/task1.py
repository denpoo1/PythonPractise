import os

def compute_sum_and_count(input_dir):
    total_sum = 0
    total_count = 0

    for item in os.listdir(input_dir):
        item_path = os.path.join(input_dir, item)

        if os.path.isfile(item_path) and item.endswith('.txt'):
            with open(item_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    for word in line.split():
                        try:
                            number = int(word)
                            total_sum += number
                            total_count += 1
                        except ValueError:
                            pass

        elif os.path.isdir(item_path):
            subdirectory_sum, subdirectory_count = compute_sum_and_count(item_path)
            total_sum += subdirectory_sum
            total_count += subdirectory_count

    return total_sum, total_count

def get_directory_path():
    directory_path = input("Enter the directory path: ")
    return directory_path

def main():
    directory_path = get_directory_path()

    if not os.path.exists(directory_path):
        print("The specified path does not exist.")
        return

    total_sum, total_count = compute_sum_and_count(directory_path)
    print("Total sum of numbers:", total_sum)
    print("Total count of numbers:", total_count)

if __name__ == "__main__":
    main()
