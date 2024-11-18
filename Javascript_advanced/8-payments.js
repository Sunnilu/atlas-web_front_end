// Function to process payment
function processPayment(amount) {
    console.log(`Collecting payment of ${amount}`);
  }
  
  // Function to process the order
  function processOrder(orderId, amount) {
    console.log(`${orderId} is being processed`);
    processPayment(amount);  // Call processPayment function
    console.log(`${orderId} has been fully processed`);
  }
  
  // Main code execution
  console.log("Processing orders");
  processOrder(12321, 10.99);
  processOrder(12322, 12.99);
  processOrder(12323, 15.0);
  console.log("All the orders have been processed");
  