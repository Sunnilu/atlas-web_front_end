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
  
  // Measure the execution time for 100 executions
  const startTime = performance.now();
  
  for (let i = 0; i < 100; i++) {
    countPrimeNumbers(); // Execute the function 100 times
  }
  
  const endTime = performance.now();
  
  console.log(`Execution time of calculating prime numbers 100 times was ${endTime - startTime} milliseconds.`);
  