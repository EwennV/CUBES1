
$(document).ready(function () {
    $('#myTable').DataTable({
        "language": {
            'lengthMenu': "Afficher _MENU_ résultats par page",
            'zeroRecords': "Aucune donnée correspondante",
            'info': 'Page _PAGE_ sur _PAGES_',
            'infoEmpty': 'Aucune données',
            'infoFiltered': 'Filtre appliqué sur _MAX_ résultats',
            'search': 'Rechercher',
            "paginate": {
                "first":      "Premier",
                "last":       "Dernier",
                "next":       "Prochaine",
                "previous":   "Précédente"
            },
        }
    })
})