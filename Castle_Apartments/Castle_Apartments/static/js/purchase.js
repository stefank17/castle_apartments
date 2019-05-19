// Kóði fundin hjá W3schools: https://www.w3schools.com/howto/howto_js_form_steps.asp?

var currentTab = 0;
showTab(currentTab);

function showTab(n) { // Gerir takkana fyrir hvert tab og sýnir þau
  var x = document.getElementsByClassName("tab");
  x[n].style.display = "block";
  if (n == 0) {
    document.getElementById("prevBtn").style.display = "none";
  } else {
    document.getElementById("prevBtn").style.display = "inline";
  }
  if (n == (x.length - 1)) {
    document.getElementById("nextBtn").style.display = "none";
    document.getElementById("kaupaBtn").style.display = "inline";
    //document.getElementById("nextBtn").innerHTML = "Kaupa fasteign";
  } else {
    document.getElementById("kaupaBtn").style.display = "none";
    document.getElementById("nextBtn").style.display = "inline";
    //document.getElementById("nextBtn").innerHTML = "Næsta skref";
  }
  fixStepIndicator(n)
}

function nextPrev(n) { // Lætur þig fara á rétta form
  review();
  var x = document.getElementsByClassName("tab");
  if (n == 1 && !validateForm()) return false;
  x[currentTab].style.display = "none";
  currentTab = currentTab + n;
  if (currentTab >= x.length) { // Ef við erum komnir á seinasta skref gera þettaΩ
    document.getElementById("regForm").submit();
    return false;
  }
  showTab(currentTab);
}

function validateForm() { // Skoðar ef eitthvað input er tómt
  var x, y, i, valid = true;
  x = document.getElementsByClassName("tab");
  y = x[currentTab].getElementsByTagName("input");
  for (i = 0; i < y.length; i++) {
    if (y[i].value == "") {
      y[i].className += " invalid";
      valid = false;
    }
  }
  if (valid) {
    document.getElementsByClassName("step")[currentTab].className += " finish";
  }
  return valid;
}

// Gerir kúlurnar fyrir skrefin active meðað við hvar þú ert
function fixStepIndicator(n) {
  var i, x = document.getElementsByClassName("step");
  for (i = 0; i < x.length; i++) {
    x[i].className = x[i].className.replace(" active", "");
  }
  x[n].className += " active";
}

/* Kóði hér fyrir neðan skrifaði ég */
function review() {
  var number = document.getElementById('num').value
  var month = document.getElementById('month').value
  var year = document.getElementById('year').value
  var cvc = document.getElementById('cvc').value
  var home = document.getElementById('home').value
  var city = document.getElementById('city').value
  var country = document.getElementById('country').value
  var zip = document.getElementById('zip').value
  var ssn = document.getElementById('ssn').value

  reviewcountry=document.getElementById('reviewcountry')
  reviewcountry.options[0] = new Option(country, country);
  document.getElementById('reviewnum').value = number
  document.getElementById('reviewmonth').value = month
  document.getElementById('reviewyear').value = year
  document.getElementById('reviewcvc').value = cvc
  document.getElementById('reviewhome').value = home
  document.getElementById('reviewcity').value = city
  document.getElementById('reviewzip').value = zip
  document.getElementById('reviewssn').value = ssn
}