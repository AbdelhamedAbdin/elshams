// let typing_count = document.querySelectorAll(".typing-count span");
// const message_field = document.getElementById("contact-message");
// let closer_elem = document.querySelector('.message-field > .typing-count > span');
//
// if (message_field.textContent === "") {
//     closer_elem.textContent = 0;
// } else {
//     closer_elem.textContent = message_field.textContent.length;
// }
//
// // for (let i = 0; i < typing_count.length; i++) {
// message_field.onkeydown = function (e) {
//     number = Number(closer_elem.textContent);
//     const re = new RegExp('a,b,c,d,e,f,g,h,i');
//
//     if (e.code === 'Backspace') {
//         closer_elem.textContent = number - 1;
//         if (closer_elem.textContent < 0) {
//             closer_elem.textContent = 0
//         }
//     } else {
//         closer_elem.textContent = number + 1;
//     }
// }
//

// Set Dynamic Date
function dynamic_date() {
    const curr_year = document.getElementById("curr-year");
    const next_year = document.getElementById("next-year");

    date = new Date();
    curr_year.textContent = date.getFullYear();
    next_year.textContent = date.getFullYear() + 1;
}
dynamic_date()

// apply "*" on required field
const form_input = document.querySelectorAll(".form-group input");

form_input.forEach(input => {
        if (input.hasAttribute('required') && input.required === true) {
            let target_label = input.parentElement.querySelector("label > strong");

            if (target_label !== null) {
                target_label.innerHTML += "<span class='text-danger'>*</span>"
            }
        }
    }
)
// change the behavior of Admission form based on options
let joined_before = document.querySelectorAll(".joined_before");
let siblings_in = document.querySelectorAll(".sibl_in");
let mother_job = document.querySelectorAll(".mother_job");
let mother_qualif = document.querySelectorAll(".mother_qualif");
let father_qualif = document.querySelectorAll(".father_qualif");

const join_question = document.getElementById("join_question");
const siblings_question = document.getElementById("sibl_question");
const mother_job_question = document.getElementById("mother_job_question");
const mother_qualif_question = document.getElementById("mother_qualif");
const father_qualif_question = document.getElementById("father_qualif");


display_based_on_field(joined_before, join_question, "YES")
display_based_on_field(siblings_in, siblings_question, "YES")
display_based_on_field(mother_job, mother_job_question, "2")
display_based_on_field(mother_qualif, mother_qualif_question, "OTHER")
display_based_on_field(father_qualif, father_qualif_question, "OTHER")

// display fields based on its options
function display_based_on_field(fields, question_fields, target_value) {
    for (let i = 0; i < fields.length; i++) {

        let target_input = fields[i].querySelector("input");
        // display the inputs after loading the page if it's equal to target_value
        if (target_input.checked && target_input.value === target_value) {
            question_fields.classList.remove("d-none");
            for (inps of question_fields.querySelectorAll("input")) {
                inps.hidden = false;
            }
        }

        // display the inputs when onChange the radio behavior
        target_input.onchange = function (e) {
            if (e.target.checked && e.target.value === target_value) {
                question_fields.classList.remove("d-none");
                for (inps of question_fields.querySelectorAll("input")) {
                    inps.hidden = false
                }
            } else {
                question_fields.classList.add("d-none");
                for (inps of question_fields.querySelectorAll("input")) {
                    inps.hidden = true
                }
            }
        }
    }
}