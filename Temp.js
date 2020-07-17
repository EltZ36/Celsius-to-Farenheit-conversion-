var temps;
var i;
function setup() {
  temps = [212, 100, 1, 2, 10, 415, 150, 75, 77, 1000, 123, 124];
  noLoop();
}
function draw() {
  var i = 0;
  while (i < 12) {
    console.log(
      temps[i] + " degrees F which is " + nfc(5 * (temps[i] - 32) / 9, 2) + " degrees C and " + nfc(5 * (temps[i] - 32) / 9 + 273.15, 4) + " Kelvin"
    );
    i++; // i =i + 1
  }
}
