function validate_drug_Form() {
    var id = document.getElementById("id").value;
    var name = document.getElementById("name").value;
    var manufacturer = document.getElementById("manufacturer").value;
    var expirydate = document.getElementById("expirydate").value;

    if (id.trim() === "") {
        alert("Primary key should not be Empty");
        return false;
      }
    if (name.trim() === "" || name.trim().length<4) {
      alert("please enter a valid drug name");
      return false;
    }
  
      if (manufacturer.trim() === "" || manufacturer.trim().length<4) {
        alert("please Enter valid Manufacturer name");
        return false;
      }
      if (expirydate.trim() === "") {
        alert("please enter a valid expiration date");
        return false;
      }

      else
      {
        return true;
      }
    }