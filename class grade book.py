class GradeBook:

  def __init__(self, data):
    self.data = data  # Dictionary of {student_name: score}

  def class_average(self):
    if not self.data:
      return 0
    return sum(self.data.values()) / len(self.data)

  def top_scorer(self):
    if not self.data:
      return None, None
    top_name = max(self.data, key=self.data.get)
    return top_name, self.data[top_name]

  def last_scorer(self):
    if not self.data:
      return None, None
    low_name = min(self.data, key=self.data.get)
    return low_name, self.data[low_name]

  def lookup_student(self, name):
    for k, v in self.data.items():
      if k.lower() == name.lower():
        return k, v
    return None

  def search_students(self, query):
    return {k: v for k, v in self.data.items() if query.lower() in k.lower()}


def run_search_mechanism(grade_book):
  while True:
    print("\n--- GRADE BOOK SEARCH MECHANISM ---")
    print("1. Look up a single student's exact score")
    print("2. Search names containing specific letters")
    print("3. View class statistics (Average, Top, Bottom)")
    print("4. Exit")

    choice = input("\nEnter your choice (1-4): ").strip()

    if choice == "1":
      name = input("Enter the student's exact name: ").strip()
      result = grade_book.lookup_student(name)
      if result:
        print(f"\nFound: {result[0]} has a score of {result[1]}")
      else:
        print(f"\nStudent '{name}' not found.")

    elif choice == "2":
      query = input("Enter search characters: ").strip()
      results = grade_book.search_students(query)
      if results:
        print(f"\nMatches found ({len(results)}):")
        for name, score in results.items():
          print(f" - {name}: {score}")
      else:
        print(f"\nNo student names contain '{query}'.")

    elif choice == "3":
      avg = grade_book.class_average()
      top_n, top_s = grade_book.top_scorer()
      low_n, low_s = grade_book.last_scorer()
      print(f"\nClass Average: {avg:.2f}")
      print(f"Top Scorer: {top_n} ({top_s})")
      print(f"Lowest Scorer: {low_n} ({low_s})")

    elif choice == "4":
      print("\nExiting search mechanism. Goodbye!")
      break
    else:
      print("\nInvalid choice. Please enter a number between 1 and 4.")


# Initialize data and run
students_data = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "Diana": 95,
    "Evan": 63,
}
my_grade_book = GradeBook(students_data)

# Start the interactive search terminal
run_search_mechanism(my_grade_book)
