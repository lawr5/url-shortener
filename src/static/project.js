//open form
const openForm = document.getElementById("form-input");
const openbtn = document.getElementById('openform');
openbtn.onclick = function() {
    if (openForm.style.display = "none") {
    openForm.style.display = "block"
    }
};
//closes form
const closeForm = document.getElementById("form-input");
const closebtn = document.getElementById("closeform");
closebtn.onclick = function() {
    if (closeForm.style.display != "none") {
    closeForm.style.display = "none"
    }
};

//add short_url input custom message
const short_url_msg = document.getElementById("short_url_input");

short_url_msg.addEventListener("input", (event) => {
  if (short_url_msg.validity.patternMismatch) {
    short_url_msg.setCustomValidity("Field cannot be blank and only contain letters, numbers, and dashes.");
  } else {
    short_url_msg.setCustomValidity("");
  }
});

//add long_url input custom message
const long_url_msg = document.getElementById("long_url_input");

long_url_msg.addEventListener("input", (event) => {
  if (long_url_msg.validity.typeMismatch) {
    long_url_msg.setCustomValidity("Url must contain the http:// or https:// scheme.");
  } else {
    long_url_msg.setCustomValidity("");
  }
});


  
//open edit form
const editforms = [...document.querySelectorAll(".edit-form")];
const editbtns = document.querySelectorAll(".edit-btn");
const closebtns = document.querySelectorAll(".close-edit");

console.log(editbtns)





// function openFunction() {
//     getform = document.querySelector('.edit-form').style.display = 'block';
// };


// function openFunction(){
//     var id = "edit-form{{url.id}}";
//     var edit_form = document.getElementById(id);
//     if (edit_form.style.display = 'none'){
//         edit_form.style.display = 'block'
//     }
// };


// editforms.forEach((edit_form) => {
//         editforms.forEach(e => e.style.display === {});
// });

// function openFunction(){
//     if (editforms.style.display === 'none'){
//     editforms.style.display = 'block'
//     }
// };


// window.onload = function() {
//     editbtns.forEach(el => el.addEventListener('click', openFunction));
//   };

// editforms.forEach((edit_form) => {
//         editforms.forEach(e => e.style.display = 'none');
// });



// [].forEach.call(editbtns, function(btn) {
    
//     btn.addEventListener('click', function(event) {
      
//       alert(this.innerText + " Clicked!");
//     })
//   })
