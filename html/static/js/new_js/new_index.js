function get_today() {
    var today = new Date();

    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var date = today.getDate();
    var week = Math.ceil(date / 7);
    
    var html_date = document.getElementById("day_value");
    var html_week = document.getElementById("week_value");
    var html_month = document.getElementById("month_value");

    html_date.innerHTML = date;
    html_week.innerHTML = week;
    html_month.innerHTML = month;
    
    var month_char = document.getElementById("month_char");

    if(month == 1) {
        month_char.innerHTML = "Month Jan.";
    }else if(month == 2) {
        month_char.innerHTML = "Month Feb.";
    }else if(month == 3) {
        month_char.innerHTML = "Month Mar.";
    }else if(month == 4) {
        month_char.innerHTML = "Month Apr.";
    }else if(month == 5) {
        month_char.innerHTML = "Month May.";
    }else if(month == 6) {
        month_char.innerHTML = "Month Jun.";
    }else if(month == 7) {
        month_char.innerHTML = "Month Jul.";
    }else if(month == 8) {
        month_char.innerHTML = "Month Aug.";
    }else if(month == 9) {
        month_char.innerHTML = "Month Sep.";
    }else if(month == 10) {
        month_char.innerHTML = "Month Oct.";
    }else if(month == 11) {
        month_char.innerHTML = "Month Nov.";
    }else if(month == 12) {
        month_char.innerHTML = "Month Dec.";
    }else{
        console.log("error");
    };
}

function input_search(){
    var msg = document.getElementById("item_name").value;
    if (msg == ""){
        console.log("검색값 없음");
    }else {
        var links = 'result/' + String(msg);
        location.href = "/" + links;
    }
}

function today_value_open(){
    var date_bar = document.querySelector('.date_bar');
    var search_bar = document.querySelector('.search_bar');
    var main_bar = document.querySelector('.main_bar');
    var content = document.querySelector('.content');
    var first_menu = document.querySelector('.first_menu');
    
    date_bar.style.display = "none";
    search_bar.style.display = "none";
    main_bar.style.display = "block";
    content.style.width = "70%";
    content.style.height = "60%";
    content.style.padding = "3% 15% 7% 15%";
    first_menu.style.display = "block";
}

function today_value_exit(){
    var date_bar = document.querySelector('.date_bar');
    var search_bar = document.querySelector('.search_bar');
    var main_bar = document.querySelector('.main_bar');
    var content = document.querySelector('.content');
    var first_menu = document.querySelector('.first_menu');
    
    date_bar.style.display = "block";
    search_bar.style.display = "block";
    main_bar.style.display = "none";
    content.style.width = "60%";
    content.style.height = "55%";
    content.style.padding = "5% 20% 7% 20%";
    first_menu.style.display = "none";
}