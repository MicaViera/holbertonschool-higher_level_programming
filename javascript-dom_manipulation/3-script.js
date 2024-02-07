document.querySelector('#toggle_header').addEventListener('click', () => {
  const header = document.querySelector('header');
  if (header.classList.contains('red')) {
    header.classList.remove('red');
  } else {
    header.classList.add('red');
  }
  header.classList.toggle('green');
});
