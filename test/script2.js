let btn=document.querySelector('input[type="submit"]');
btn.addEventListener("click",function()
{
    let userName=document.querySelector('input[type="text"]').value;
    let Password=document.querySelector('input[type="password"]').value;
    if(userName=="admin"&&Password=="password")
    {
        localStorage.setItem("username",userName);
        localStorage.setItem("password",Password);
        localStorage.setItem("accesso","approvato");
        window.close();
    }else
    {
        localStorage.setItem("accesso","negato");
        alert("Passwiord o/e Nome utentte mancanti o errati");
    }
})