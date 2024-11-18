// Global variable
var globalVariable = "Welcome";

// Outer function
function outer() {
    // Alert the content globalVariable
    alert(globalVariable);

    // Create a local variable wthin the outer
    var course = "Holberton";

    // Inner function
    function inner() {
        // alert the content of gloabalVariable and course and exclamation (concatenated)
        alert(globalVariable + " " + course);
        
        // Create a local variable within inner
        var exclamation = "!";

        // Inception function (inside inner)
        function inception() {
            // Alert the content of globalVariable, course and the exclamation (concatenate)
            alert(globalVariable + " " + course + exclamation);
        }

        // Call the inception function
        inception();
    }

    // Calling the inner function
    inner();
}

// Call the outer function in the main code
outer();