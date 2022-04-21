const formulario = document.getElementById('inicio');
const inputs = document.querySelectorAll('#inicio input');

const expresiones = {
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    password: /^.{4,12}$/, // 4 a 12 digitos.
}
const validarInicio = (e) => {
    switch (e.target.name) {
        case "emailini":
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('inicio_emailini').classList.remove('formulario__inicio-incorrecto');
                document.getElementById('inicio_emailini').classList.add('formulario__inicio-correcto');
                document.querySelector('#inicio_emailini .formulario__input-error-ini').classList.remove('formulario__input-error-ini-activo');

            } else {
                document.getElementById('inicio_emailini').classList.add('formulario__inicio-incorrecto');
                document.getElementById('inicio_emailini').classList.remove('formulario__inicio-correcto')
                document.querySelector('#inicio_emailini .formulario__input-error-ini').classList.add('formulario__input-error-ini-activo');

            }
            break;
        case "password":
            if (expresiones.password.test(e.target.value)) {
                document.getElementById('inicio_password').classList.remove('formulario__inicio-incorrecto');
                document.getElementById('inicio_password').classList.add('formulario__inicio-correcto');
                document.querySelector('#inicio_password .formulario__input-error-ini').classList.remove('formulario__input-error-ini-activo');
            } else {
                document.getElementById('inicio_password').classList.add('formulario__inicio-incorrecto');
                document.getElementById('inicio_password').classList.remove('formulario__inicio-correcto');
                document.querySelector('#inicio_password .formulario__input-error-ini').classList.add('formulario__input-error-ini-activo');
            }

            break;
    }
}
inputs.forEach((input) => {
    input.addEventListener('keyup', validarInicio);
    input.addEventListener('blur', validarInicio);

});
inicio.addEventListener('submit', (e) => {
    e.preventDefault();
});