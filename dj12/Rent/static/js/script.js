let selectedBike = "";

function bookBike(bike) {
  selectedBike = bike;
  document.getElementById("booking").style.display = "block";
  document.getElementById("bikeName").innerText = "Selected Bike: " + bike;
}

function confirmBooking() {
  let name = document.getElementById("name").value;
  let date = document.getElementById("date").value;

  if (name === "" || date === "") {
    alert("Please fill all details");
    return;
  }

  alert(`Booking Confirmed!
Name: ${name}
Bike: ${selectedBike}
Date: ${date}`);

  document.getElementById("booking").style.display = "none";
}