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
              document.documentElement.style.setProperty('--text-color', '#ffffff');
              document.documentElement.style.setProperty('--border-color', '#ffffff');
              document.documentElement.style.setProperty('--selected-tab-color', '#555555');
               // light color for text in dark mode
              document.body.style.backgroundColor = '#242424';
              document.querySelectorAll('.form-input').forEach(input => {
                  input.style.backgroundColor = '#333';
                  input.style.color = '#fff';
                  input.style.borderColor = '#555';
              });
              document.querySelectorAll('.form-button').forEach(button => {
                  button.style.backgroundColor = '#555';
                  button.style.color = '#fff';
              });
              document.querySelector('.logo-text').style.color = '#ffcc89';
          } else {
                localStorage.setItem('lightMode', modeCheck.checked);
              document.documentElement.style.setProperty('--background-color', '#242424');
              document.documentElement.style.setProperty('--text-color', '#242424');
              document.documentElement.style.setProperty('--border-color', '#242424');
              document.documentElement.style.setProperty('--selected-tab-color', '#d8d8d8');
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
              document.querySelector('.logo-text').style.color = 'rgb(225, 0, 0)';
          }
      }
  
      // Add event listener for the mode toggle checkbox
      modeCheck.addEventListener('change', toggleDarkMode);
  
      // Initialize dark mode based on the checkbox state
      toggleDarkMode();
  });