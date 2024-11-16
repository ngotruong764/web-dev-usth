// convert temperatures to and from Celsius and Fahrenheit:

// get degree_form
let degreeForm = document.getElementById('degree_form');
        degreeForm.addEventListener('submit', e => {
            e.preventDefault(); // Prevent form submission
            let degreeInput = document.getElementById('degree');
            let degree = parseFloat(degreeInput.value); // Parse input as a number

            // Celsius to Fahrenheit conversion
            let fahrenheit = 9/5 * degree + 32;

            // Display the result
            alert('Fahrenheit: ' + fahrenheit);
        });
