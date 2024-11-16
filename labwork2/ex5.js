function calculate(operation){
    let num1 = document.getElementById('first-num');
    let num2 = document.getElementById('second-num');
    let result = 0;
    if(operation === 'multiply'){
        result = num1.value * num2.value;
    } else{
        result = num1.value / num2.value;
    }

    document.getElementById('res').innerText = "The Result is: " + result;
}