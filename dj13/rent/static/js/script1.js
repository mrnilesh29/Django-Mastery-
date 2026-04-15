let selectedCar = "";

function bookCar(car) {
  selectedCar = car;

  document.getElementById("booking").style.display = "block";
  document.getElementById("carName").innerText = `Selected Car: ${car}`;

  document.getElementById("booking").scrollIntoView({ behavior: "smooth" });
}

function confirmBooking() {
  let name = document.getElementById("name").value.trim();
  let date = document.getElementById("date").value;

  if (name === "" || date === "") {
    alert("⚠️ Please fill all details");
    return;
  }

  if (name.length < 3) {
    alert("⚠️ Name must be at least 3 characters");
    return;
  }

  let today = new Date().toISOString().split("T")[0];
  if (date < today) {
    alert("⚠️ Select a valid future date");
    return;
  }

  alert(`✅ Booking Confirmed!
Name: ${name}
Car: ${selectedCar}
Date: ${date}`);

  document.getElementById("booking").style.display = "none";
}