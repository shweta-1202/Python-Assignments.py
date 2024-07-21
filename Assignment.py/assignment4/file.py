#Creating first feedback file
with open("C:\\Users\\Shweta\\OneDrive\Desktop\\sir python\\feedback1.txt",'w') as file:
   file.write("Customer's Feedback in first file:")
   file.write("\n Shweta: 5 - Excellent Service!!")
   file.write("\n Asmi: 4 - Good Service, but could improve.")
   file.write("\n Krutika: 3 - Average Service, needs improvement.")

#Creating second feedback file
with open("C:\\Users\\Shweta\\OneDrive\\Desktop\\sir python\\feedback2.txt",'w') as file:
   file.write("Customer's Feedback in second file:")
   file.write("\n Dipak: 5 - Very Good Service!")
   file.write("\n Aaditi: 2 - Poor Service, must improve.")
   file.write("\n Pranjal: 3 - Average Service, needs improvement.")

#Creating third feedback file
with open("C:\\Users\\Shweta\\OneDrive\\Desktop\\sir python\\feedback3.txt",'w') as file:
   file.write("Customer's Feedback in third file:")
   file.write("\n Nirmohi: 5 - Efficient Service!")
   file.write("\n Diksha: 4 - Good Service!!.")
   file.write("\n Roshani: 3 - Average Service, needs improvement.")
   file.write("\n Goli: 2 - Very Poor Service, needs more improvement.")
   
   def read_feedback_files(files):
    feedback_data = []
    try:
        for file in files:
           with open(files[0], 'r') as f1, open(files[1], 'r') as f2, open(files[2], 'r') as f3:
                feedback_data.extend(f1.readlines())
                feedback_data.extend(f2.readlines())
                feedback_data.extend(f3.readlines())
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None
    return feedback_data
 
 
def proc_feedback_data(feedback_data):
    # Check if feedback_data is empty or None
    if not feedback_data:
        return None, None  # Return None, None if no data to process

    total_feedback = 0
    total_rating = 0.0
    feedback_entries = []

    # Process each line in feedback_data
    for line in feedback_data:
        parts = line.split(' - ')
        if len(parts) == 2:
            name_rating = parts[0].split(':')
            if len(name_rating) == 2:
                # Extract customer name, rating, and comment
                customer_name = name_rating[0].strip()
                rating = int(name_rating[1].strip())
                comment = parts[1].strip()

                # Append feedback entry to feedback_entries list
                feedback_entries.append({
                    'customer_name': customer_name,
                    'rating': rating,
                    'comment': comment
                })

                total_feedback = +1  # Increment total feedback count
                total_rating = +rating  # Add rating to total rating sum

    # Calculate average rating if there's any feedback
    if total_feedback > 0:
        avg_rating = total_rating / total_feedback   #formula
    else:
        avg_rating = 0.0

    return feedback_entries, avg_rating


def write_summary_file(feedback_entries, average_rating, output_file):
    # Check if feedback_entries is empty
    if not feedback_entries:
        return False  # Return False if no entries to write

    try:
        # Write summary data to output_file
        with open(output_file, 'w') as f:
            f.write(f"Total Feedback Entries: {len(feedback_entries)}\n")
            f.write(f"Average Rating: {average_rating:.2f}\n\n")

            f.write("Feedbacks:\n")
            for entry in feedback_entries:
                f.write(f"{entry['customer_name']}: {entry['rating']} - {entry['comment']}\n")
    except IOError as e:
        print(f"Error: {e}")
        return False  # Return False if there's an IOError

    return True  # Return True if writing was successful


def proc_feedback():
    files = [
        'feedback1.txt',
        'feedback2.txt',
        'feedback3.txt'
    ]
    output_file = 'feedback_summary.txt'

    # Step 1: Read data from files
    feedback_data = read_feedback_files(files)
    if feedback_data is None:
        return  # Exit function if reading files fails

    # Step 2: Process data
    feedback_entries, avg_rating = proc_feedback_data(feedback_data)
    if feedback_entries is None:
        print("No valid feedback data found.")
        return  # Exit function if no valid feedback data to process

    # Step 3: Write processed data to summary file
    if write_summary_file(feedback_entries, avg_rating, output_file):
        print(f"Summary written to {output_file}")
    else:
        print("Failed to write summary file.")


if __name__ == "__main__":
    proc_feedback()
    
    
