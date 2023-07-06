function showPopupMessage(message) {
  alert(message);
}

// Event listener for successful update
document.getElementById("updateButton").addEventListener("click", function(event) {
  event.preventDefault(); // Prevent default form submission

  // Get the form data
  var formData = new FormData(document.getElementById("employeeForm"));
  var employeeId = formData.get("employee_id");
  var name = formData.get("name");
  var contact = formData.get("contact");
  var sex = formData.get("sex");
  var address = formData.get("address");

  // Create an object with the form data
  var updateData = {
    employee_id: employeeId,
    name: name,
    contact: contact,
    sex: sex,
    address: address
  };

  // Perform the update operation
  // You can use AJAX to send the form data to the server for processing
  $.ajax({
    url: "/update_employee", // Replace with your server endpoint
    type: "POST",
    data: updateData,
    success: function(response) {
      if (response.success) {
        // Show popup message on successful update
        showPopupMessage(response.message);
        
        // Reset the form
        document.getElementById("employeeForm").reset();
      } else {
        // Show error message
        showPopupMessage("Failed to update employee.");
      }
    },
    error: function(xhr, textStatus, errorThrown) {
      // Show error message
      showPopupMessage("An error occurred during the update operation.");
      console.error("Error:", errorThrown);
    }
  });
});