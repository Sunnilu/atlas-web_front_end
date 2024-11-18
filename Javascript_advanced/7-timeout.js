console.log("Start of the execution queue");

// Loop to log iteration numbers from 1 to 100
for (let i = 1; i <= 100; i++) {
    console.log(i);
}

console.log("End of the loop printing");

// Use setTimeout with delay 0 to log the final message asynchronously
setTimeout(() => {
    console.log("Final code block to be executed");
}, 0);
