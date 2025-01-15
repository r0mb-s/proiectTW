document.addEventListener("click", (e) =>{
      if (e.target.matches("#gradeButton")){
          button = e.target;
          url = button.getAttribute('data-url');
          window.location.href = url;
          console.log("am apasta");
      }
  })
  