//
let array_num_form = document.getElementById('arr_num_form');
array_num_form.addEventListener('submit', e =>{
    e.preventDefault();
    let arrStr = document.getElementById('arr_num');
    let origin  = arrStr.value.split(' ');
    let arr_num =arrStr.value.split(' ');
    arr_num.sort();
    prompt("Sort " + origin + " to "+ arr_num);
});