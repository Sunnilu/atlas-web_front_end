function welcome(firstName, lastName) {
    // Create the fullName variable by combining firstName and lastName
    var fullName = firstName + ' ' + lastName;
  
    // Define the displayFullName function
    function displayFullName() {
      // Display the alert with the full name
      alert('Welcome ' + fullName + '!');
    }
  
    // Call displayFullName at the end of welcome function
    displayFullName();
  }
  
  // Test the function by calling it with 'Holberton' and 'School'
  welcome('Holberton', 'School');
  
