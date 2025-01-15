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
let question_index = 0;

addQuestionButton.addEventListener("click", function() {
    const newQuestion = questionTemplate.content.cloneNode(true);
    newQuestion.querySelector('.question-input').name = 'questions[]'
    
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
    }
});

document.addEventListener("click", (e) => {
    if (e.target.closest(".question-answer-delete")) {
        const answer = e.target.closest(".question-answer");
        if (answer) {
            answer.remove();
        }
    }
});

document.addEventListener("click", (e) => {
    if (e.target.matches("#questionDeleteButton")) {
        const question = e.target.closest(".question-wrapper");
        if (question) {
            question.remove();
        }
    }
});
