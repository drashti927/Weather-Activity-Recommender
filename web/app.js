async function getRecommendation() {
  try {
    const city = document.getElementById("city").value;
    const userId = document.getElementById("userId").value;

    const recRes = await fetch(
      `http://localhost:5002/recommend?userId=${userId}&city=${city}`
    );
    const rec = await recRes.json();

    const weatherRes = await fetch(
      `http://localhost:5000/weather?city=${city}`
    );
    const weather = await weatherRes.json();

    document.getElementById("weather").innerText =
      `Weather: ${weather.condition}, ${weather.tempC}°C`;

    document.getElementById("recommendation").innerText =
      `Recommendation: ${rec.recommendation}`;

    console.log("Weather:", weather);
    console.log("Recommendation:", rec);

  } catch (error) {
    console.error("Error:", error);
    alert("Backend not running or connection issue");
  }
}
