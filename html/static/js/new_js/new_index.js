function get_today() {
    var today = new Date();

    var year = today.getFullYear();
    var month = today.getMonth() + 1;
    var date = today.getDate();
    var week = Math.ceil(date / 7);
    
    var str_date = String(date);
    var str_week = String(week);
    var str_month = String(month);
    var str_year = String(year);

    function find_one_two(str_value) {
        if(str_value.length == 2) {
            var first = str_value.charAt(0);
            var second = str_value.charAt(1);
            return [first, second];
        }else {
            var first = "";
            var second = str_value;
            return [first, second];
        };
    }

    var str_result = find_one_two(str_date);
    var html_date_1 = document.getElementById("day_value_1");
    var html_date_2 = document.getElementById("day_value_2");
    
    html_date_1.innerHTML = str_result[0];
    html_date_2.innerHTML = str_result[1];
    
    var str_result = find_one_two(str_week);
    var html_week_1 = document.getElementById("week_value_1");
    var html_week_2 = document.getElementById("week_value_2");
    
    html_week_1.innerHTML = str_result[0];
    html_week_2.innerHTML = str_result[1];
    
    var str_result = find_one_two(str_month);
    var html_month_1 = document.getElementById("month_value_1");
    var html_month_2 = document.getElementById("month_value_2");
    
    html_month_1.innerHTML = str_result[0];
    html_month_2.innerHTML = str_result[1];
    
    var main_daily = document.getElementById("main_daily");
    main_daily.innerHTML = str_year + "-" + str_month + "-" + str_date;
    
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
    
    var today = new Date();
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
    var calender = document.querySelector('.calender');
    
    date_bar.style.display = "none";
    search_bar.style.display = "none";
    main_bar.style.display = "block";
    content.style.width = "70%";
    content.style.height = "60%";
    content.style.padding = "4% 15% 7% 15%";
    first_menu.style.display = "block";
    calender.style.display = "none";
}

function today_value_exit(){
    var date_bar = document.querySelector('.date_bar');
    var search_bar = document.querySelector('.search_bar');
    var main_bar = document.querySelector('.main_bar');
    var content = document.querySelector('.content');
    var first_menu = document.querySelector('.first_menu');
    var calender = document.querySelector('.calender');
    
    date_bar.style.display = "block";
    search_bar.style.display = "block";
    main_bar.style.display = "none";
    content.style.width = "60%";
    content.style.height = "55%";
    content.style.padding = "7% 20% 7% 20%";
    first_menu.style.display = "none";
    calender.style.display = "none";
}

function calender_open(){
    var calender = document.querySelector('.calender');
    calender.style.display = "block";
    goToday();
}

function calender_exit(){
    var calender = document.querySelector('.calender');
    calender.style.display = "none";
}

function calender(date_datas) {
    var today = new Date();
    var date_data = date_datas;

    var year = date_datas.getFullYear();
    var month = date_datas.getMonth();
    
    var prevLast = new Date(year, month - 1, 0);
    var thisLast = new Date(year, month, 0);
    
    var PLDate = prevLast.getDate();
    var PLDay = prevLast.getDay();

    var TLDate = thisLast.getDate();
    var TLDay = thisLast.getDay();
    
    var prevDates = [];
    var thisDates = [...Array(TLDate + 1).keys()].slice(1);
    var nextDates = [];
    
    if (PLDay !== 6) {
      for (let i = 0; i < PLDay + 1; i++) {
        prevDates.unshift(PLDate - i);
      }
    }

    for (let i = 1; i < 7 - TLDay; i++) {
      nextDates.push(i);
    }
    
    var dates = prevDates.concat(thisDates, nextDates);
    var firstDateIndex = dates.indexOf(1);
    var lastDateIndex = dates.lastIndexOf(TLDate);
    
    dates.forEach((date, i) => {
    const condition = i >= firstDateIndex && i < lastDateIndex + 1
                      ? 'thiss'
                      : 'other';

    dates[i] = "<div class='date'><span class='" + String(condition) + "'>" + String(date) + "</span></div>";
    });
    
    var first = [];
    var second = [];
    var third = [];
    
    date_datas.setMonth(date_datas.getMonth() - 2);
    var bedore_year = date_datas.getFullYear();
    var before_month = date_datas.getMonth() + 1;
    for(var i = 0; i < firstDateIndex; i++) {
        first.push(String(dates[i]).substring(38, String(dates[i]).length-13));
        dates[i] = "<div class='date' value='" + bedore_year + "-" + before_month + "-" + first[i] + "'onclick='search_result_date(this);'><span class='other'>" + first[i] + "</span></div>";
    };
    
    date_datas.setMonth(date_datas.getMonth() + 1);
    var today_year = date_datas.getFullYear();
    var today_month = date_datas.getMonth() + 1;
    for(var i = firstDateIndex; i < lastDateIndex + 1; i++) {
        second.push(String(dates[i]).substring(38, String(dates[i]).length-13));
        dates[i] = "<div class='date' value='" + today_year + "-" + today_month + "-" + second[i - first.length] + "'onclick='search_result_date(this);'><span class='thiss'>" + second[i - first.length] + "</span></div>";
    };
    
    date_datas.setMonth(date_datas.getMonth() + 1);
    var next_year = date_datas.getFullYear();
    var next_month = date_datas.getMonth() + 1;
    for(var i = lastDateIndex + 1; i < dates.length; i++) {
        third.push(String(dates[i]).substring(38, String(dates[i]).length-13));
        dates[i] = "<div class='date' value='" + next_year + "-" + next_month + "-" + third[i - first.length - second.length] + "'onclick='search_result_date(this);'><span class='other'>" + third[i - first.length - second.length] + "</span></div>";
    };

    document.querySelector('.dates').innerHTML = dates.join('');
}

function prevMonth() {
    var date = new Date();
    date.setMonth(date.getMonth());
    calender(date);
}

function nextMonth() {
    var date = new Date();
    date.setMonth(date.getMonth() + 2);
    calender(date);
}

function goToday() {
    var date = new Date();
    date.setMonth(date.getMonth() + 1);
    calender(date);
    
    /*var test = new Date();
    var year = test.getFullYear();
    var month = test.getMonth() + 1;
    var date = test.getDate();
    var str_date = year + "-" + month;
    
    test.setMonth(test.getMonth() - 1);
    
    var year = test.getFullYear();
    var month = test.getMonth() + 1;
    var date = test.getDate();
    var str_date = year + "-" + month;
    console.log(str_date);*/
}

function search_result_date(value) {
    var search = value.getAttribute('value');
    console.log(search);
}