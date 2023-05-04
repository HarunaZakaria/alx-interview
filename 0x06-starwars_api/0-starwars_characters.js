#!/usr/bin/node
const request = require('request');

const movieID = process.argv[2];
const url = `https://swapi.dev/api/films/${movieID}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const movie = JSON.parse(body);
  const characters = movie.characters;

  console.log(`The characters in ${movie.title} are:`);

  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
