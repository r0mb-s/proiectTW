const addclass = document.getElementsByClassName("add-class-wrapper")[0];

console.log("asdas")

addclass.addEventListener("click", () => {
    const url = addclass.getAttribute("data-url");
    window.location.href = url;
});

function toggleDropdown() {
    const dropdown = document.getElementById("dropdown");
    dropdown.classList.toggle("open"); // Add/remove the "open" class
}

const addQuestionButton = document.getElementById("addQuestionButton");
const questionContainer = document.getElementById("questionContainer");
const questionTemplate = document.getElementById("questionTemplate");
const questionFormular = document.getElementById("questionFormular");
let question_index = 0;
let answer_index = 0;

addQuestionButton.addEventListener("click", function() {
    const newQuestion = questionTemplate.content.cloneNode(true);
    newQuestion.querySelector('.question-input').name = `question_${question_index}`;   
    question_index += 1;
    questionContainer.appendChild(newQuestion);
});

document.addEventListener("click", function(e) {
    if (e.target.matches("#butondropdown")) {
        const dropdownContent =
            e.target.parentElement.parentElement.nextElementSibling;
        dropdownContent.classList.toggle("open");
    }
});

document.addEventListener("click", (e) => {
    if (e.target.closest(".question-answer-add")) {
        const questionDropdownContent = e.target.closest(
            ".question-dropdown-content",
        );
        const answerTemplate = document.querySelector("#answerTemplate");

        if (questionDropdownContent && answerTemplate) {
            // Clone the answer template content
            const answerContent = answerTemplate.content.cloneNode(true);

            // Insert the answer content above the "Add Answer" button
            const addAnswerButton = questionDropdownContent.querySelector(
                ".question-answer-add",
            );

            questionDropdownContent.insertBefore(answerContent, addAnswerButton);
        }
        
        const allAnswers = questionDropdownContent.querySelectorAll('.answer');
        let answerNumber = 0;

        const closeQuestionIndex = e.target.closest(".question-wrapper").querySelector(".question-input").name.split('_')[1];
        allAnswers.forEach(answer => {
            answer.name = `answer_${closeQuestionIndex}_${answerNumber}`
            answerNumber++;
        });


    }
});



document.addEventListener("click", (e) => {
    if (e.target.closest(".question-answer-delete")) {
        const answer = e.target.closest(".question-answer");
        const parentQuestionWrapper = answer.parentElement;
        const closeQuestionIndex = e.target.closest(".question-wrapper").querySelector(".question-input").name.split('_')[1];
        if (answer) {
            answer.remove();
        }

        const allAnswers = parentQuestionWrapper.querySelectorAll(".question-answer");
        let answerNumber = 0;


        allAnswers.forEach(answerElement => {
            answerElement.querySelector('input').name = `answer_${closeQuestionIndex}_${answerNumber}`
            answerNumber++;
        });
    }
});

document.addEventListener("click", (e) => {
    if (e.target.matches("#questionDeleteButton")) {
        const question = e.target.closest(".question-wrapper");
        if (question) {
            question.remove();
            question_index--;
        }

        questionContainers = questionFormular.querySelectorAll('.question-wrapper');
        for (index = 0; index < question_index; index++){
            questionUpdate = questionContainers[index].querySelector(".question-input");
            questionUpdate.name = `question_${index}`;
            answersForQuestion = questionContainers[index].querySelector(".question-dropdown-content").querySelectorAll(".question-answer");

            let answerNumber = 0;
            answersForQuestion.forEach(answerElement =>{
                answerElement.querySelector(".answer").name = `answer_${index}_${answerNumber}`;
                answerNumber++;
            });
        }
        
    }
});

document.addEventListener("change", (e) =>{
    if (e.target.closest(".question-answer-check-wrapper")){
        const checkBox = e.target;
        if (checkBox.checked){
            answerChecked = e.target.closest(".question-answer").querySelector(".answer");
            answerChecked.name += "+"
        } else{
            answerUnchecked = e.target.closest(".question-answer").querySelector(".answer");
            answerUnchecked.name = answerUnchecked.name.replace("+", "");
        }
    }
});