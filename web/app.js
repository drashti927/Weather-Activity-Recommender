async function getRecommendation() {

  const city = document.getElementById("city").value;
  const userId = document.getElementById("userId").value;

  const rec = await fetch(
    `http://localhost:5002/recommend?userId=${userId}&city=${city}`
  ).then(r => r.json());

  const weather = await fetch(
    `http://localhost:5000/weather?city=${city}`
  ).then(r => r.json());

  document.getElementById("weather").innerText =
    `Weather: ${weather.condition}, ${weather.tempC}°C`;

  document.getElementById("recommendation").innerText =
    `Recommendation: ${rec.recommendation}`;

  document.getElementById("body").className =
    weather.condition.includes("rain") ? "rain" :
    weather.condition.includes("cloud") ? "clouds" : "clear";
}
