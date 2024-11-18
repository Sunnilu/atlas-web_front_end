// function that returns the number of prime 
function countPrimeNumbers() {
     const isPrime = num => {
        if (num <2) return false;
        for (let i =2; i <=Math.sqrt(num); i++) {
            if (num % i === 0) return false;
        }
     };

     let primeCount = 0;
     for (let i = 2; i <= 100; i++) {
        if (isPrime(i)) {
            primeCount++;
        }
     }

     return primeCount;
}

// Measure the execution time
const startTime = preformance.now();
const primeCount = countPrimeNumbers();
const endTime = performance.now();

console.log('Prime numbers count: ${primeCount}');
console.log('Execution time of printing countPrimeNumber was ${endTime - startTime} millisecond.');