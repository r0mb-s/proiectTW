const addclass = document.getElementsByClassName('add-class-wrapper')[0];

addclass.addEventListener('click', () =>{
      const url = addclass.getAttribute('data-url');
      window.location.href = url;
});

function toggleDropdown() {
      
      const dropdown = document.getElementById('dropdown');
      dropdown.classList.toggle('open'); // Add/remove the "open" class
    }

const addQuestionButton = document.getElementById('addQuestionButton');
const questionContainer = document.getElementById('questionContainer');
const questionTemplate = document.getElementById('questionTemplate');

addQuestionButton.addEventListener('click', function() {
      const newQuestion = questionTemplate.content.cloneNode(true);
      questionContainer.appendChild(newQuestion);
});

document.addEventListener('click', function (e) {
      if (e.target.matches('#butondropdown')) {
        const dropdownContent = e.target.parentElement.nextElementSibling;
        dropdownContent.classList.toggle('open');
      }
    });
    

