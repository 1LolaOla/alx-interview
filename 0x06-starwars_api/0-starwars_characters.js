#!/usr/bin/node
const util = require('util');
const request = util.promisify(require('request'));
const filmID = process.argv[2];

async function starwarsCharacters (filmId) {
  const endpoint = 'https://swapi-api.hbtn.io/api/films/' + filmId;
  let response = await (await request(endpoint)) .body;
  response = JSON.parse(response);
  const characters = response.characters;

  for (let i = 0; i < characters.length; i++) {
    const urlCharacter = characters[i];
<<<<<<< HEAD
    let character = await (await request(urlCharacter)).body;
=======
    let character await (await request (urlCharacter)) .body;
>>>>>>> 9a610c110e79e005b9afd16cb3129f5bdc54fa88
    character = JSON.parse(character);
    console.log(character.name);
  }
}

starwarsCharacters(filmID);
