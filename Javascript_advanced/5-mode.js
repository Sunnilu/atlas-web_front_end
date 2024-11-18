<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Change Modes</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            transition: all 0.3s ease;
        }
    </style>
</head>
<body>
    <script>
        // Change Mode Function
        function changeMode(size, weight, transform, background, color) {
    return function() {
        document.body.style.fontSize = `${size}px`;
        document.body.style.fontWeight = weight;
        document.body.style.textTransform = transform;
        document.body.style.backgroundColor = background;
        document.body.style.color = color;
    {"}"};
}

        // Main Function to initialize elements and button actions
        function main() {
            // Create a paragraph with welcome text
            const para = document.createElement('p');
            para.textContent = "Welcome Atlas!";
            document.body.appendChild(para);

            // Create buttons for different modes
            const spookyButton = document.createElement('button');
            spookyButton.textContent = 'Spooky';
            const darkModeButton = document.createElement('button');
            darkModeButton.textContent = 'Dark mode';
            const screamModeButton = document.createElement('button');
            screamModeButton.textContent = 'Scream mode';

            // Append buttons to the body
            document.body.appendChild(spookyButton);
            document.body.appendChild(darkModeButton);
            document.body.appendChild(screamModeButton);

            // Define the change mode functions
            const spooky = changeMode(9, 'bold', 'uppercase', 'pink', 'green');
            const darkMode = changeMode(12, 'bold', 'capitalize', 'black', 'white');
            const screamMode = changeMode(12, 'normal', 'lowercase', 'white', 'black');

            // Add event listeners to the buttons
            spookyButton.addEventListener('click', spooky);
            darkModeButton.addEventListener('click', darkMode);
            screamModeButton.addEventListener('click', screamMode);
        {"}"}

        // Call the main function to set up the page
        document.addEventListener('DOMContentLoaded', main);
    </script>
</body>
</html>
