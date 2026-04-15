let selectedBike = "";

function bookBike(bike) {
  selectedBike = bike;

  document.getElementById("booking").style.display = "block";
  document.getElementById("bikeName").innerText = `Selected Bike: ${bike}`;

  // Smooth scroll
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
    alert("⚠️ Please select a valid future date");
    return;
  }

  alert(`✅ Booking Confirmed!
Name: ${name}
Bike: ${selectedBike}
Date: ${date}`);

  // Reset form
  document.getElementById("name").value = "";
  document.getElementById("date").value = "";
  document.getElementById("booking").style.display = "none";
}