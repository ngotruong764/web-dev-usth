let lst_num_form = document.getElementById('lst_num_form');
lst_num_form.addEventListener('submit', e=>{
    e.preventDefault();
    let lst_num_text = document.getElementById('lst_num');
    let lst_num = lst_num_text.value.split(' ');    
    for (num in lst_num){
        num = Number(lst_num[num]);
        const para = document.createElement('p');
        if(num % 2 === 0){
            para.innerText = 'Number '+num+' is even';
    
        } else{
            para.innerText = 'Number '+num+' is odd';
        }
        document.body.appendChild(para);
    }
});