// Function that creates a classroom of students
function createClassRoom(numbersOfStudents) {
    // Array to store closures
    const students = [];
  
    // Function that returns a closure for each student
    function studentSeat(seat) {
      return function() {
        return seat;
      };
    }
  
    // Loop through the number of students and create a closure for each seat
    for (let i = 0; i < numbersOfStudents; i++) {
      students.push(studentSeat(i + 1));  // Seat numbers start at 1, so we use i + 1
    }
  
    // Return the array of closures
    return students;
  }
  
  // Create a classroom with 10 students
  const classRoom = createClassRoom(10);
  
  // Test: Calling the closures and logging their return values
  console.log(classRoom[0]());  // Should log: 1
  console.log(classRoom[3]());  // Should log: 4
  console.log(classRoom[9]());  // Should log: 10
  