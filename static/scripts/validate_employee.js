function validateForm() {
    var name = document.getElementById("name").value;
    var contact = document.getElementById("contact").value;
    var sex = document.getElementById("sex").value;
    var address = document.getElementById("address").value;

    if (name.trim() === "" || name.trim().length<4) {
        alert("full name should be greater than 4 character");
        return false;
      }
      var phoneRegex = /^\d{10}$/;
      if (!contact.match(phoneRegex)) {
        alert("Invalid phone number");
        return false;
      }
      if (sex.trim() === "" || sex.trim().length<4) {
        alert("please select your gender");
        return false;
      }
      if (address.trim() === "" || address.trim().length<2) {
        alert("please enter a valid address");
        return false;
      }

      else
      {
        return true;
      }
    }