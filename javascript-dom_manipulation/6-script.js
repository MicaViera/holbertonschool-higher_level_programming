const character = document.querySelector('#character');
const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";

function text_Content(json) {
    character.textContent = json.name;
}
fetch(url)
    .then(data => data.json())
    .then(text_Content)
