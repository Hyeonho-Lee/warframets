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
        dates[i] = "<div class='date' name='date_value' value='" + bedore_year + "-" + before_month + "-" + first[i] + "'onclick='search_result_date(this);'><span class='other'>" + first[i] + "</span></div>";
    };
    
    date_datas.setMonth(date_datas.getMonth() + 1);
    var today_year = date_datas.getFullYear();
    var today_month = date_datas.getMonth() + 1;
    for(var i = firstDateIndex; i < lastDateIndex + 1; i++) {
        second.push(String(dates[i]).substring(38, String(dates[i]).length-13));
        dates[i] = "<div class='date' name='date_value' value='" + today_year + "-" + today_month + "-" + second[i - first.length] + "'onclick='search_result_date(this);'><span class='thiss'>" + second[i - first.length] + "</span></div>";
    };
    
    date_datas.setMonth(date_datas.getMonth() + 1);
    var next_year = date_datas.getFullYear();
    var next_month = date_datas.getMonth() + 1;
    for(var i = lastDateIndex + 1; i < dates.length; i++) {
        third.push(String(dates[i]).substring(38, String(dates[i]).length-13));
        dates[i] = "<div class='date' name='date_value' value='" + next_year + "-" + next_month + "-" + third[i - first.length - second.length] + "'onclick='search_result_date(this);'><span class='other'>" + third[i - first.length - second.length] + "</span></div>";
    };

    document.querySelector('.dates').innerHTML = dates.join('');
}

var cal_now = new Date();

function prevMonth() {
    var today = document.getElementById("today");
    if(cal_now.getMonth() - 1 == 0) {
        cal_now.setMonth(cal_now.getMonth() - 2);
        var y_m_today = String(cal_now.getFullYear()) + "-" + String(cal_now.getMonth() + 1);
        today.innerHTML = y_m_today;
        cal_now.setMonth(cal_now.getMonth() + 1);
    }else {
        cal_now.setMonth(cal_now.getMonth() - 1);
        var y_m_today = String(cal_now.getFullYear()) + "-" + String(cal_now.getMonth());
        today.innerHTML = y_m_today;
    }

    calender(cal_now);
    all_date();
}

function nextMonth() {
    if(cal_now.getMonth() + 1 > 12) {
        var prev_month = new Date(cal_now.getFullYear(), cal_now.getMonth() + 1, 1);
        cal_now = new Date(prev_month.getFullYear(), prev_month.getMonth(), 1);
    }else {
        cal_now = new Date(cal_now.getFullYear(), (cal_now.getMonth()), 1);
    }
    
    var today = document.getElementById("today");
    var y_m_today = String(cal_now.getFullYear()) + "-" + String(cal_now.getMonth() + 1);
    today.innerHTML = y_m_today;
    
    cal_now.setMonth(cal_now.getMonth() + 1);
    calender(cal_now);
    all_date();
}

function goToday() {
    var date = new Date();
    cal_now = new Date(date.getFullYear(), (date.getMonth()), 1);
    
    var today = document.getElementById("today");
    var y_m_today = String(cal_now.getFullYear()) + "-" + String(cal_now.getMonth() + 1);
    today.innerHTML = y_m_today;

    cal_now.setMonth(cal_now.getMonth() + 1);
    calender(cal_now);
    all_date();
}

function result_exit() {
    location.href = "/";
}

function delay() {
    var menu = document.querySelector('.open_menu');
    menu.style.display = "none";
}

function open_menu(){
    var menu = document.querySelector('.open_menu');
    menu.style.display = "block";
    menu.style.animationName = "movemenu_0";
    menu.style.animationDuration = "0.5s";
    menu.style.animationDirection = "normal";
}

function close_menu(){
    var menu = document.querySelector('.open_menu');
    menu.style.animationName = "movemenu_1";
    menu.style.animationDuration = "0.5s";
    menu.style.animationDirection = "normal";
    setTimeout("delay()", 450);
}