import csv
import sys
import random


def main():
    check_arguements() #check command-line arguements
    Ids = list() #empty list for containing ids

    try:
        with open(sys.argv[1], "r") as read_file:
            reader = csv.DictReader(read_file)   #open file to read hired positions

            for row in reader:
                position = row["hired_position"] #catching positions
                initials = generate_initials(position) #generating initials
                number = random.randint(100, 999)
                id = generate_id(initials, str(number)) #combine initial with random number to generate id
                if id not in Ids:
                    Ids.append(id) #add in list
                else:
                    continue

        with open(sys.argv[2], "w", newline="") as write_file: #open file to write headers
            writer = csv.DictWriter(
                write_file,
                fieldnames=["name", "hired_position", "decided_salary", "id"],
            )
            writer.writeheader()  # Write header row

            with open(sys.argv[1], "r") as read_file:
                reader = csv.DictReader(read_file)

                i = 0
                for row in reader:
                    writer.writerow(
                        {
                            "name": row["name"],
                            "hired_position": row["hired_position"],
                            "decided_salary": row["decided_salary"], #write whole data with ids
                            "id": Ids[i],
                        }
                    )
                    i += 1

    except FileNotFoundError:
        sys.exit("CSV File Not Found 😥")

    option = input("\nDo You Want to Show the IDs on Terminal as Well (yes/no)? ")
    if ask_ids(option):
        print("\nIDs:", *Ids, "\n")   #asking to show ids on terminal or not.
    else:
        sys.exit("IDs Generated In Your Desired CSV File 😊")


def check_arguements():
    if len(sys.argv) < 3:
        sys.exit("Too Few Command-Line Arguments 🙁")
    if len(sys.argv) > 3:
        sys.exit("Too Many Command-Line Arguments ☹️")
    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV File 😥")


def generate_initials(s):
    return s[0]


def generate_id(initial, s):
    return initial + s


def ask_ids(option):
    if option.lower() == "yes":
        return True
    return False


if __name__ == "__main__":
    main()
