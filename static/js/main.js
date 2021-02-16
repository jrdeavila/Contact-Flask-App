const btnDelete = document.querySelectorAll('.btn-delete')
if(btnDelete){
    const btnArray = Array.from(btnDelete)
    btnArray.forEach(element => {
        element.addEventListener('click', (e) =>{
            if(!confirm('Are you sure you want to delete it?')){
                e.preventDefault();
            }
        })        
    });
}
