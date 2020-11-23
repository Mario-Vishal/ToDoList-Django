// //selectors
// const todoInput =document.querySelector('.todo-input');
// const todoButton =document.querySelector('.todo-button');
// const todoList =document.querySelector('.todo-list');
// const filterOption = document.querySelector('.filter-todo');
// //Event Listeners
// name=prompt("Enter Your Name!");
// document.querySelector('span').innerText=name.toUpperCase();
// const d = new Date();
// const days=['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday'];

// document.querySelector('.day').innerHTML="Today is "+days[d.getDay()]+"!!";
// todoButton.addEventListener('click',addTodo);
// todoList.addEventListener('click',delcheck);
// filterOption.addEventListener('click',filterTodo);

// //Functions

// function addTodo(event){
//     const todoDiv = document.createElement("div");
//     const newTodo = document.createElement('li');
//     // const completedButton =document.createElement('button');
//     //Preventform from submitting
//     event.preventDefault();
//     if (todoInput.value!=="" && todoInput.value!=="Write Something!!"){
    
//     //ToDO Div
//     // const todoDiv = document.createElement("div");
//     todoDiv.classList.add("todo");
//     //create li
//     // const newTodo = document.createElement('li');
//     newTodo.innerText=todoInput.value;
//     newTodo.classList.add('todo-item');
//     todoDiv.appendChild(newTodo);
//     //check mark button
//     const completedButton =document.createElement('button');
//     completedButton.innerHTML = '<i class="fas fa-check"></i>';
//     completedButton.classList.add('complete-btn');
//     todoDiv.appendChild(completedButton);
//     //thrash mark button
//     const thrashButton =document.createElement('button');
//     thrashButton.innerHTML = '<i class="fas fa-trash"></i>';
//     thrashButton.classList.add('thrash-btn');
//     todoDiv.appendChild(thrashButton);

//     //append to list
//     todoList.appendChild(todoDiv);

//     //clear Todo Input value
//     todoInput.value="";
//     }
//     else{
        
//         todoInput.value="Write Something!!";
//         todoInput.classList.add('fun');

//         setTimeout(crazy,200);

//     }
// }

// function delcheck(e){
//     const item =e.target;
//     console.log(e.target);
//     const bd=document.querySelector('body');
//     //Delete
//     if (item.classList[0]==="thrash-btn"){
//         const todo1=item.parentElement;
//         //animation
//         todo1.classList.add("fall");
//         bd.classList.add('red-back');
//         todo1.addEventListener('transitionend',function(){
//             todo1.remove();
//             bd.classList.remove('red-back');
//         });       
//     }
//     //check mark
//     if (item.classList[0]=="complete-btn"){
//         const todo1 = item.parentElement;
//         bd.classList.add('green-back');
//         todo1.classList.toggle('completed');
//         todo1.addEventListener('transitionend',function(){

//         bd.classList.remove('green-back');
        

//     });
// }
// }

// function crazy(e){
//     todoInput.classList.remove('fun');
//     todoInput.value="";
// }

const delBtn = document.querySelector('.thrash-btn');

delBtn.onclick = () =>{
    console.log("deleted");
    this.disabled = true;
}