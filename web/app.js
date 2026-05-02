async function getRecommendation() {
  const userId = document.getElementById("userId").value;
  const city = document.getElementById("city").value;

  const res = await fetch(`http://localhost:5002/recommend?userId=${userId}&city=${city}`);
  const data = await res.json();

  document.getElementById("weather").innerText =
    `Weather: ${data.weather}`;

  document.getElementById("recommendation").innerText =
    `Recommendation: ${data.recommendation}`;
}
