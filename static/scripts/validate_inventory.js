function validateForm() {
    var inventoryId = document.getElementById("inventoryId").value;
    var medicationId = document.getElementById("medicationId").value;
    var quantity = document.getElementById("quantity").value;
    var location = document.getElementById("location").value;
    var expiryDate = document.getElementById("expiryDate").value;

    if (inventoryId.trim() === "") {
        alert("Inventory ID should not be Empty");
        return false;
      }
    if (medicationId.trim() === "") {
      alert("please enter a valid Drug ID");
      return false;
    }
  
    if (quantity.trim() === "" || quantity.trim().value<=0) {
        alert("please Enter valid amount of Inventory item");
        return false;
      }
    if (location.trim() === "" || location.trim().length<4) {
        alert("please enter a valid location");
        return false;
      }
    if (expiryDate.trim() === "") {
        alert("please Enter valid Expiration date");
        return false;
      }

      else
      {
        return true;
      }
    }