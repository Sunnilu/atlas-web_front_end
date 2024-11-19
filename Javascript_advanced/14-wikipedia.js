// Function to create a paragraph element and append it to the document body
function createElement(data) {
    // Create a paragraph element
    const p = document.createElement('p');
    
    // Set the content of the paragraph to the provided data
    p.textContent = data;
    
    // Append the paragraph to the body of the document
    document.body.appendChild(p);
}

// Function to query Wikipedia's API and execute a callback with the result
function queryWikipedia(callback) {
    // Create a new XMLHttpRequest object (vanilla JavaScript)
    const xhr = new XMLHttpRequest();

    // Configure the request: GET the data from Wikipedia's API
    xhr.open('GET', 'https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro&explaintext&redirects=1&titles=Stack%20Overflow&origin=*', true);

    // Set up the callback for when the request completes
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Parse the JSON response
            const response = JSON.parse(xhr.responseText);
            
            // Extract the page data from the response
            const page = response.query.pages;
            
            // Get the page ID (which is dynamically generated in the response)
            const pageId = Object.keys(page)[0];
            
            // Get the extract (summary) of the article
            const extract = page[pageId].extract;

            // Call the provided callback function with the extracted text
            callback(extract);  // Here, we invoke the callback function (createElement) with the extract
        } else {
            console.error('Error fetching data from Wikipedia.');
        }
    };

    // Send the request
    xhr.send();
}

// Separate the invocation of queryWikipedia from createElement
queryWikipedia(function(extract) {
    // This anonymous function serves as the callback to createElement
    createElement(extract);
});

