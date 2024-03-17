function openlogin(){
  document.getElementById('login-section').style.top = '12%';
  document.getElementById('login-section').style.borderRadius = '100px';
  document.getElementById('singup').style.opacity = '0.6';
  
}
function closelogin(){
  document.getElementById('login-section').style.top = '90%';
  document.getElementById('login-section').style.borderRadius = '250px';
  document.getElementById('singup').style.opacity = '1';

}