function login(){
    a='admin'
	b='123'
	ins1=document.getElementById('username').value
	ins2=document.getElementById('password').value
     
	if(a==ins1 && b==ins2){
		window.location.replace("/dashboard")
	}
}