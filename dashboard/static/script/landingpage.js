document.addEventListener('DOMContentLoaded', function() {
      // Select the checkbox that toggles dark mode
      const modeCheck = document.querySelector('.mode-check');
        if (localStorage.getItem('lightMode') === 'true'){
            modeCheck.checked = localStorage.getItem('lightMode');
        }else{
            localStorage.setItem('lightMode', modeCheck.checked);
        }
      
      // Function to toggle dark mode
      function toggleDarkMode() {
          if (modeCheck.checked) {
            localStorage.setItem('lightMode', modeCheck.checked);
              document.documentElement.style.setProperty('--background-color', '#242424');
              document.documentElement.style.setProperty('--light-titles-color', 'rgb(253, 179, 2)');
              document.documentElement.style.setProperty('--subtitle-color', '#ffffff');
              document.documentElement.style.setProperty('--form-shadow', '3px 0px 30px rgba(255, 255, 255, 0.7)'); // light color for text in dark mode
              document.body.style.backgroundColor = '#242424';
              document.querySelectorAll('.form-input').forEach(input => {
                  input.style.backgroundColor = '#333';
                  input.style.color = '#fff';
                  input.style.borderColor = '#555';
              });
              document.querySelectorAll('.form-button').forEach(button => {
                  button.style.backgroundColor = 'rgb(253, 179, 2)';
                  button.style.color = '#242424';
              });
          } else {
              // Revert to light mode styles
              localStorage.setItem('lightMode', modeCheck.checked);
              document.documentElement.style.setProperty('--background-color', '#ffffff');
              document.documentElement.style.setProperty('--light-titles-color', 'rgb(225, 0, 0)');
              document.documentElement.style.setProperty('--subtitle-color', '#242424');
              document.documentElement.style.setProperty('--form-shadow', '3px 0px 30px rgba(0, 0, 0, 0.7)');
              document.body.style.backgroundColor = '#ffffff';
              document.querySelectorAll('.form-input').forEach(input => {
                  input.style.backgroundColor = '#fff';
                  input.style.color = '#000';
                  input.style.borderColor = '#c5c5c5';
              });
              document.querySelectorAll('.form-button').forEach(button => {
                  button.style.backgroundColor = '#e10000';
                  button.style.color = '#fff';
              });
          }
      }
  
      // Add event listener for the mode toggle checkbox
      modeCheck.addEventListener('change', toggleDarkMode);
  
      // Initialize dark mode based on the checkbox state
      toggleDarkMode();

      function switchForms(){
        if (document.getElementsByClassName('signin-form')[0].classList.contains('hide')){
            document.getElementsByClassName('signin-form')[0].classList.remove('hide')
            document.getElementsByClassName('login-form')[0].classList.add('hide')
        } else {
            document.getElementsByClassName('signin-form')[0].classList.add('hide')
            document.getElementsByClassName('login-form')[0].classList.remove('hide')
        }
        console.log("click")
      }

      document.querySelectorAll('.alternative-create span')[0].addEventListener('click', switchForms);
      document.querySelectorAll('.alternative-create span')[1].addEventListener('click', switchForms);

      const googleButton = document.getElementsByClassName('alternative-picture-wrapper')[0];
        console.log(googleButton);
        googleButton.addEventListener('click', () =>{
      const url = googleButton.getAttribute('data-url');
      window.location.href = url;
        });
  });
  