// Define welcomeMessage function
function welcomeMessage(fullName) {
    // Return a clousure that displays the welcome message
    return function() {
        alert("Welcome " + fullName);
    };    
}

// Creat the closure for each variable
var guillaume = welcomeMessage("Guillaume");
var alex = welcomeMessage("Alex");
var fred = welcomeMessage("Fred");

// Test these by calling them
guillaume();
alex();
fred();