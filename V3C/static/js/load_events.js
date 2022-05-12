$(function () {
    $('.cal-day').on('click', function () {
        var day;
        $(this).children('.date').each(function(){
            day = $(this).text(); 
        });
        var month, year;
        $('#htmlcalendar tbody tr .month').each(function(){
            month = $(this).text().split(' ')[0]; 
            year = $(this).text().split(' ')[1];
        });
        date = day + " " + month + " " + year;
        //date = new Date(str)
        //console.log(date)
        $.ajax({
            url: 'ajax/load_events',
            type: 'get',
            data: {
                date: date
            },
            dataType : 'json',
            failure: function (response) {
                // alert the error if any error occured
                console.log(response.responseJSON.errors)
            },
            success: function(response){
                var list_html = '<ul class = "list-group-flush">';
                list_html += '<hr class="hr-custom">';
                for( var i=0; i <response.length; i++) {
                    list_html += '<li class = "list-group-item align-items-start">'+
                                '<div class="row">'+
                                '<div class = "col-sm-2">'+
                                '<div class = "c-date">'+
                                '<div class="fw-bold">'+
                                '<i class="bx bx-calendar" ></i>' + response[i].start_time.date;
                    if (response[i].end_time != null && response[i].start_time.date != response.end_time.date){
                        html_list += " - " + response[i].end_time.date;}
                    html_list += "</div>";
                    html_list += "</div>";
                    html_list += '<div class = "c-time">';
                    html_list += '<p><i class="bx bx-time-five"></i>' + response[i].start_time.time;
                    if (response[i].end_time != null){
                        html_list += " - " + response[i].end_time.time;}
                    html_list += '</p>';
                    html_list += '</div></div>';
                    html_list += '<div class="col-sm-10">';
                    html_list += '<div class="col-sm-10">';
                    html_list += '<div class = "conf_name">';
                    if (response[i].live == true){
                        html_list += '<span class = "badge bg-danger rounded-pill">LIVE</span>';}
                    html_list += response[i].name;
                    html_list += '<div class = "text-muted conf_text">{{conf.notes}}</div>'+
                                '</div></div>'+
                                '<div class="row">'+
                                '<div class="col">'+
                                '<div class = "detail-ref">'+
                                '<a href="{{conf.get_absolute_url}}"><i class="bx bx-link-external" ></i>&nbspПерейти</a>'+
                                '</div></div></div>'+
                                '</li>'+
                                '<hr class="hr-custom">'
                }
                list_html += '</ul>';
                $('#list-html').html(list_html);    
            }
        });
        
    });
});