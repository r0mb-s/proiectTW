const addclass = document.getElementsByClassName('add-class-wrapper')[0];

addclass.addEventListener('click', () =>{
      const url = addclass.getAttribute('data-url');
      window.location.href = url;
});
