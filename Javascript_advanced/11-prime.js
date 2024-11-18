function countPrimeNumbers() {
    const isPrime = num => {
      if (num < 2) return false;
      for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
      }
      return true;
    };
  
    let primeCount = 0;
    for (let i = 2; i <= 100; i++) {
      if (isPrime(i)) {
        primeCount++;
      }
    }
  
    return primeCount;
  }
  
  // Measure the execution time for 100 executions using setTimeout
  const startTime = performance.now();
  
  function executeInBatch(count) {
    if (count <= 0) return;  // Base case: stop recursion when done
    
    // Use setTimeout to allow the call stack to clear before executing
    setTimeout(() => {
      countPrimeNumbers(); // Execute the function
      executeInBatch(count - 1); // Decrement and continue the process
    }, 0);
  }
  
  executeInBatch(100); // Start the process of executing 100 times
  
  // Measure the execution time after the 100 executions are scheduled
  setTimeout(() => {
    const endTime = performance.now();
    console.log(`Execution time of calculating prime numbers 100 times was ${endTime - startTime} milliseconds.`);
  }, 0);
  