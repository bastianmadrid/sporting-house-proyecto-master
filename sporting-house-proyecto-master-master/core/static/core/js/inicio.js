const formulario = document.getElementById('inicio');
const inputs = document.querySelectorAll('#inicio input');

const expresiones = {
    correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$/,
    password: /^.{4,12}$/, // 4 a 12 digitos.
}
const camposs = {
    emailini: false,
    password: false
}
const validarInicio = (e) => {
    switch (e.target.name) {
        case "emailini":
            if (expresiones.correo.test(e.target.value)) {
                document.getElementById('inicio_emailini').classList.remove('formulario__inicio-incorrecto');
                document.getElementById('inicio_emailini').classList.add('formulario__inicio-correcto');
                document.querySelector('#inicio_emailini .formulario__input-error-ini').classList.remove('formulario__input-error-ini-activo');
                camposs['emailini'] = false;

            } else {
                document.getElementById('inicio_emailini').classList.add('formulario__inicio-incorrecto');
                document.getElementById('inicio_emailini').classList.remove('formulario__inicio-correcto')
                document.querySelector('#inicio_emailini .formulario__input-error-ini').classList.add('formulario__input-error-ini-activo');
                camposs['emailini'] = true;
            }
            break;
        case "password":
            if (expresiones.password.test(e.target.value)) {
                document.getElementById('inicio_password').classList.remove('formulario__inicio-incorrecto');
                document.getElementById('inicio_password').classList.add('formulario__inicio-correcto');
                document.querySelector('#inicio_password .formulario__input-error-ini').classList.remove('formulario__input-error-ini-activo');
                camposs['password'] = false;
            } else {
                document.getElementById('inicio_password').classList.add('formulario__inicio-incorrecto');
                document.getElementById('inicio_password').classList.remove('formulario__inicio-correcto');
                document.querySelector('#inicio_password .formulario__input-error-ini').classList.add('formulario__input-error-ini-activo');
                camposs['password'] = true;

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
    if (campos.password && campos.emailini) {
        inicio.reset();
        document.getElementById('formulario_inicio_exito').classList.add('formulario_inicio_exito');
        setTimeout(() => {
            document.getElementById('formulario_inicio_exito').classList.remove('formulario__mensaje-exito-activo');
        }, 5000);
    } else {
        document.getElementById('formulario__mensaje').classList.add('formulario__mensaje-activo');
    }
});