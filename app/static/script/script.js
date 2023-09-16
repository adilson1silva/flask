// Quando a página carregar completamente
window.addEventListener('load', function(){
    //obtenha a altura do conteúdo
    var contentHeight = document.querySelector(".content").offsetheight

    //Obtenha a altura da janela do navegador
    var windowHeight = window.innerHeight;

    // se a altura do conteúdo for menor do que a altura da janela, mostre o footer
    if (contentHeight < windowHeight){
        document.querySelector("footer").classList.remove("hidden")
    }
});