const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
// function signin(){
// 	a='test@test.com'
// 	b='123'
// 	ins1=document.getElementById('ins1').value
// 	ins2=document.getElementById('ins2').value
     
// 	if(a==ins1 && b==ins2){
// 		window.location.replace("/home")
// 	}
// }	



