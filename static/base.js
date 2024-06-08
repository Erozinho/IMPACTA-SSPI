        // Função que verifica se o comprimento do texto no h1 é diferente de zero
        function verificarH1() {
            const h1 = document.getElementById('sid');
            const login = document.getElementById('login')
            const li = document.getElementById('cadastro');

            // Verifica se a tag h1 contém texto (comprimento do texto é diferente de zero)
            if (h1.textContent.length !== 0) {
                li.style.display = 'block';
                login.textContent = "Logout";
            }
        }

        // Executa a função ao carregar a página
        window.onload = verificarH1;

function loginredirect() {
    const login = document.getElementById('login')
    if (login.textContent == "Entrar") {window.location.href = "/login"}
    else {window.location.href = "/logout"}
    }
function homeredirect() { window.location.href = "/";}