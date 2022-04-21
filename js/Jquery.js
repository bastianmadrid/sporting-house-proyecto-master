$(document).ready(function() {
    $("#registro_for").validate({
        rules: {
            nombre: {
                required: true,
                minlength: 3
            },
            email: {
                required: true,
                email: true
            },

        },
        messages: {
            nombre: {
                required: "Debe ingresar su nombre",
                minlength: "Es necesario un minimo de 3 caracteres"
            },
            email: {
                required: "Debe ingresar el correo",
                email: "El correo no es valido"
            },

        }
    });
    $('#pass1').keyup(function(e) {
        var pass1 = $('#pass1').val();
        var pass2 = $('#pass2').val();
        if (pass1 == pass2) {
            $('#error2').text("Coinciden").css("color", "green");

        } else {
            $('#error2').text("No coinciden").css("color", "red");

        }
        if (pass2 == "") {
            $('#error2').text("No se puede dejar en blanco").css("color", "red");

        }
    });
});