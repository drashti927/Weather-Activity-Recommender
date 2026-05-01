async function getRecommendation() {
  try {
    const city = document.getElementById("city").value;
    const userId = document.getElementById("userId").value;

    const response = await fetch(
      `http://localhost:5002/recommend?userId=${userId}&city=${city}`
    );

    if (!response.ok) {
      throw new Error("Backend response failed");
    }

    const data = await response.json();

    document.getElementById("weather").innerText =
      `Location: ${data.location}`;

    document.getElementById("recommendation").innerText =
      `Recommendation: ${data.recommendation}`;

    console.log("SUCCESS:", data);

  } catch (error) {
    console.error(error);
    alert("Something went wrong connecting to backend");
  }
}
