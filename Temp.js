var temps;
var i;
function setup() {
  //put what temperatures you want in Farenheit
  temps = [];
  noLoop();
}
function draw() {
  var i = 0;
  while (i < 12) {
    console.log(
      temps[i] + " degrees F which is " + nfc(5 * (temps[i] - 32) / 9, 2) + " degrees C and " + nfc(5 * (temps[i] - 32) / 9 + 273.15, 4) + " Kelvin"
    );
    i++; // i = i + 1
  }
}
