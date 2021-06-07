// Add exploit
$(function () {
    $('#submetExploits').click(function () {
        $.ajax({
            url: '/addExploit',
            data: $('#ExploitForm').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                location.reload();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
//add Chevalier
$(function () {
    $('#AddChevalier').click(function () {

        $.ajax({
            url: '/addChevalier',
            data: $('#ChevalierForm').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                location.reload();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
// add Quete
$(function () {
    $('#submetQuete').click(function () {

        $.ajax({
            url: '/addQuete',
            data: $('#queteForm').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                location.reload();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
//Add admin
$(function () {
    $('#addAdmin').click(function () {

        $.ajax({
            url: '/addAdmin',
            data: $('#formAdmin').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                location.reload();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
// Add Etat
$(function () {
    $('#submetEtat').click(function () {
        $.ajax({
            url: '/addEtat',
            data: $('#EtatForm').serialize(),
            type: 'POST',
            success: function (response) {
                location.reload();
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
// Add Importance
$(function () {
    $('#submetImportance').click(function () {
        $.ajax({
            url: '/addImportance',
            data: $('#ImportanceForm').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
                location.reload();
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
// Delete Chevalier
$(function () {
    $('.deleteChevalier').click(function () {
        var idChevalier = $('.deleteChevalier').attr('id')
        $.ajax({
            url: '/deletChevalier',
            data: {idChevalier: idChevalier},
            type: 'POST',
            success: function (response) {
                if (response == 1)
                    location.reload();
                else
                    console.log(response)
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
// Update Chevalier
let idChevalierUpdate;
$('.getIdChevalier').click(function () {
    idChevalierUpdate = $(this).attr('id');
});
$('.updateChevalier').click(function () {

    $.ajax({
        url: '/updatChevalier',
        data: $('#ChevalierFormUpdate').serialize() + "&idChevalierUpdate=" + idChevalierUpdate,
        type: 'POST',
        success: function (response) {
            if (response == 1) {
                $('#myModal').modal('hide')
                location.reload();
            } else
                console.log(response)
        },
        error: function (error) {
            console.log(error);
        }
    });

});
