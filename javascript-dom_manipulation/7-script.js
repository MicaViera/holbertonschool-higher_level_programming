const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url)

  .then(response => response.json())
  .then(data => {
    const movies = data.results;
    const ul = document.querySelector('#list_movies');

    for (const movie of movies) {
      const li = document.createElement('li');
      li.textContent = movie.title;
      ul.appendChild(li);
    }
  });
