function validateForm() {
    var password = document.getElementById("password").value;
    var email = document.getElementById("username").value;

    var emailRegex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    if (!email.match(emailRegex)) {
      alert("Invalid email");
      return false;
    }

    if (password.trim() === "" || password.trim().length<6) {
        alert("incorrect password");
        return false;
      }

      else
      {
        return true;
      }
    }