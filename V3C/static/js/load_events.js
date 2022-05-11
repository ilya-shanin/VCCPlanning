$(function () {
    $('.cal-day').on('click', function () {
        var day = $(this).getElementsByClassName('date').val();
        var title = $('#htmlcalendar').getElementsByClassName('month');
        var month, year = title.split(' ');
        date = new Date(year, month, day)
        $.ajax({
            url: '',
            type: 'get',
            data: {
                date: date
            },
            dataType : 'json',
            failure: function (response) {
                // alert the error if any error occured
                console.log(response.responseJSON.errors)
            }
        });
        
    });
});