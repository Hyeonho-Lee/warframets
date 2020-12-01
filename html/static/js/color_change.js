/* ----------------------------------------------------------- */
function change_bg_1(color_code) {
    var color_value = color_code;
    var color_bg = [];
    var color_bg_1 = [];
    var color_bg_2 = [];
    var color_bg_3 = [];
    var color_bg_4 = [];

    color_bg.push(document.querySelectorAll('.item_count'));
    for (var i = 0; i < color_bg[0].length; i++) {
        color_bg[0][i].style.borderBottom = '50px solid ' + String(color_value);
    }

    color_bg_1.push(document.querySelector('.header'));
    color_bg_1.push(document.querySelector('.header_logo'));
    color_bg_1.push(document.querySelector('.header_search'));
    color_bg_1.push(document.querySelector('.header_menu'));
    color_bg_1.push(document.querySelector('.header_info'));
    color_bg_1.push(document.querySelector('.footer'));
    color_bg_1.push(document.querySelector('.footer_box_0'));
    color_bg_1.push(document.querySelector('.footer_box_2'));
    color_bg_1.push(document.querySelector('.text_menus_0'));
    for (var i = 0; i < color_bg_1.length; i++) {
        color_bg_1[i].style.backgroundColor = String(color_value);
    }

    color_bg_2.push(document.querySelectorAll('.label'));
    for (var i = 0; i < color_bg_2[0].length; i++) {
        color_bg_2[0][i].style.backgroundColor = String(color_value);
    }

    color_bg_3.push(document.querySelector('.text_boxs'));
    color_bg_3.push(document.querySelector('.text_boxss'));
    for (var i = 0; i < color_bg_3.length; i++) {
        color_bg_3[i].style.border = '1px solid ' + String(color_value);
    }

    color_bg_4.push(document.querySelectorAll('.content_1_title'));
    for (var i = 0; i < color_bg_4[0].length; i++) {
        color_bg_4[0][i].style.borderBottom = '60px solid ' + String(color_value);
    }

    var color_bg_5 = document.querySelector('.auto_search_icon');
    color_bg_5.style.color = String(color_value);
}

function change_lb_1(color_code) {
    var color_value = color_code;
    var color_lb = [];
    var color_lb_1 = [];
    var color_lb_2 = [];

    color_lb.push(document.querySelector('.menu'));
    color_lb.push(document.querySelector('.html'));
    color_lb.push(document.querySelector('.content_1_main0'));
    color_lb.push(document.querySelector('.content_1_main1'));
    for (var i = 0; i < color_lb.length; i++) {
        color_lb[i].style.backgroundColor = String(color_value);
    }

    color_lb_1.push(document.querySelector('.content_0'));
    color_lb_1.push(document.querySelector('.content_1'));
    color_lb_1.push(document.querySelector('.content_2'));
    for (var i = 0; i < color_lb_1.length; i++) {
        color_lb_1[i].style.border = '5px solid ' + String(color_value);
    }
    
    color_lb_2.push(document.querySelectorAll('.items'));
    for (var i = 0; i < color_lb_2[0].length; i++) {
        color_lb_2[0][i].style.backgroundColor = String(color_value);
    }
}

function change_ft_1(color_code) {
    var color_value = color_code;
    var color_ft = [];
    var color_ft_1 = [];
    var color_ft_2 = [];
    var color_ft_3 = [];

    color_ft_1.push(document.querySelectorAll('.footer_link > a'));
    color_ft_1.push(document.querySelectorAll('.footer_dev > a'));
    color_ft_1.push(document.querySelectorAll('.footer_info > a'));
    for (var i = 0; i < color_ft_1[0].length; i++) {
        color_ft_1[0][i].style.color = String(color_value);
        color_ft_1[1][i].style.color = String(color_value);
        color_ft_1[2][i].style.color = String(color_value);
    }

    color_ft_2.push(document.querySelector('.footer_email'));
    color_ft_2.push(document.querySelector('.footer_count'));
    color_ft_2.push(document.querySelector('.header_color_box > i'));
    color_ft_2.push(document.querySelector('.header_color_box > p'));
    color_ft_2.push(document.querySelector('.header_language_box > i'));
    color_ft_2.push(document.querySelector('.header_language_box > p'));
    color_ft_2.push(document.querySelector('.icon_11 > i'));
    color_ft_2.push(document.querySelector('.text_menu'));
    for (var i = 0; i < color_ft_2.length; i++) {
        color_ft_2[i].style.color = String(color_value);
    }

    color_ft_3.push(document.querySelectorAll('.label > a'));
    color_ft_3.push(document.querySelectorAll('.content_1_title > a'));
    for (var i = 0; i < color_ft_3[0].length; i++) {
        color_ft_3[0][i].style.color = String(color_value);
        color_ft_3[1][i].style.color = String(color_value);
    }
}

function change_mu_1(color_code) {
    var color_value = color_code;
    var color_mu = [];
    var color_mu_1 = [];

    color_mu.push(document.querySelector('.text_boxss'));
    color_mu.push(document.querySelector('.text_boxss_1'));
    color_mu.push(document.querySelector('.text_boxss_2'));
    color_mu.push(document.querySelector('.text_boxss_3'));
    color_mu.push(document.querySelector('.mobile_menus'));
    for (var i = 0; i < color_mu.length; i++) {
        color_mu[i].style.backgroundColor = String(color_value);
    }
}

function change_wp_1(color_code) {
    var color_value = color_code;
    var color_wp = [];
    var color_wp_1 = [];

    color_wp.push(document.querySelector('.content_0'));
    color_wp.push(document.querySelector('.content_1'));
    color_wp.push(document.querySelector('.content_2'));
    for (var i = 0; i < color_wp.length; i++) {
        color_wp[i].style.backgroundColor = String(color_value);
    }
}

function change_ct_1() {
    var color_input_1 = document.getElementById("custom_color_1");
    var color_input_2 = document.getElementById("custom_color_2");
    var color_input_3 = document.getElementById("custom_color_3");
    var color_input_4 = document.getElementById("custom_color_4");
    var color_input_5 = document.getElementById("custom_color_5");
    var color_value_1 = color_input_1.value;
    var color_value_2 = color_input_2.value;
    var color_value_3 = color_input_3.value;
    var color_value_4 = color_input_4.value;
    var color_value_5 = color_input_5.value;
    
    change_bg_1(color_value_1);
    change_lb_1(color_value_2);
    change_ft_1(color_value_3);
    change_mu_1(color_value_4);
    change_wp_1(color_value_5);
}
/* ----------------------------------------------------------- */
function change_bg_2(color_code) {
    var color_value = color_code;
    var color_bg_1 = [];
    var color_bg_2 = [];
    var color_bg_3 = [];
    var color_bg_4 = [];
    var color_bg_6 = [];

    color_bg_1.push(document.querySelector('.header'));
    color_bg_1.push(document.querySelector('.header_logo'));
    color_bg_1.push(document.querySelector('.header_search'));
    color_bg_1.push(document.querySelector('.header_menu'));
    color_bg_1.push(document.querySelector('.header_info'));
    color_bg_1.push(document.querySelector('.footer'));
    color_bg_1.push(document.querySelector('.footer_box_0'));
    color_bg_1.push(document.querySelector('.footer_box_2'));
    color_bg_1.push(document.querySelector('.text_menus_0'));
    for (var i = 0; i < color_bg_1.length; i++) {
        color_bg_1[i].style.backgroundColor = String(color_value);
    }
    
    color_bg_2.push(document.querySelectorAll('.label'));
    for (var i = 0; i < color_bg_2[0].length; i++) {
        color_bg_2[0][i].style.backgroundColor = String(color_value);
    }
    
    color_bg_6.push(document.querySelectorAll('.info_0'));
    for (var i = 0; i < color_bg_6[0].length; i++) {
        color_bg_6[0][i].style.backgroundColor = String(color_value);
    }

    color_bg_3.push(document.querySelector('.text_boxs'));
    color_bg_3.push(document.querySelector('.text_boxss'));
    for (var i = 0; i < color_bg_3.length; i++) {
        color_bg_3[i].style.border = '1px solid ' + String(color_value);
    }

    var color_bg_5 = document.querySelector('.auto_search_icon');
    color_bg_5.style.color = String(color_value);
}

function change_lb_2(color_code) {
    var color_value = color_code;
    var color_lb = [];

    color_lb.push(document.querySelector('.menu'));
    color_lb.push(document.querySelector('.menu_1'));
    for (var i = 0; i < color_lb.length; i++) {
        color_lb[i].style.backgroundColor = String(color_value);
    }
}

function change_ft_2(color_code) {
    var color_value = color_code;
    var color_ft = [];
    var color_ft_1 = [];
    var color_ft_2 = [];
    var color_ft_3 = [];

    color_ft_1.push(document.querySelectorAll('.footer_link > a'));
    color_ft_1.push(document.querySelectorAll('.footer_dev > a'));
    color_ft_1.push(document.querySelectorAll('.footer_info > a'));
    for (var i = 0; i < color_ft_1[0].length; i++) {
        color_ft_1[0][i].style.color = String(color_value);
        color_ft_1[1][i].style.color = String(color_value);
        color_ft_1[2][i].style.color = String(color_value);
    }

    color_ft_2.push(document.querySelector('.footer_email'));
    color_ft_2.push(document.querySelector('.footer_count'));
    color_ft_2.push(document.querySelector('.header_color_box > i'));
    color_ft_2.push(document.querySelector('.header_color_box > p'));
    color_ft_2.push(document.querySelector('.header_language_box > i'));
    color_ft_2.push(document.querySelector('.header_language_box > p'));
    color_ft_2.push(document.querySelector('.icon_11 > i'));
    color_ft_2.push(document.querySelector('.text_menu'));
    for (var i = 0; i < color_ft_2.length; i++) {
        color_ft_2[i].style.color = String(color_value);
    }

    color_ft_3.push(document.querySelectorAll('.label > a'));
    color_ft_3.push(document.querySelectorAll('.content_1_title > a'));
    for (var i = 0; i < color_ft_3[0].length; i++) {
        color_ft_3[0][i].style.color = String(color_value);
        color_ft_3[1][i].style.color = String(color_value);
    }
}

function change_mu_2(color_code) {
    var color_value = color_code;
    var color_mu = [];
    var color_mu_1 = [];

    color_mu.push(document.querySelector('.text_boxss'));
    color_mu.push(document.querySelector('.text_boxss_1'));
    color_mu.push(document.querySelector('.text_boxss_2'));
    color_mu.push(document.querySelector('.text_boxss_3'));
    color_mu.push(document.querySelector('.mobile_menus'));
    for (var i = 0; i < color_mu.length; i++) {
        color_mu[i].style.backgroundColor = String(color_value);
    }
}

function change_wp_2(color_code) {
    var color_value = color_code;
    var color_wp = [];
    var color_wp_1 = [];
    
    color_wp_1.push(document.querySelector('.info_4'));
    color_wp_1.push(document.querySelector('.notice_bg'));
    for (var i = 0; i < color_wp_1.length; i++) {
        color_wp_1[i].style.color = String(color_value);
    }
}

function change_ct_2() {
    var color_input_1 = document.getElementById("custom_color_1");
    var color_input_2 = document.getElementById("custom_color_2");
    var color_input_3 = document.getElementById("custom_color_3");
    var color_input_4 = document.getElementById("custom_color_4");
    var color_input_5 = document.getElementById("custom_color_5");
    var color_value_1 = color_input_1.value;
    var color_value_2 = color_input_2.value;
    var color_value_3 = color_input_3.value;
    var color_value_4 = color_input_4.value;
    var color_value_5 = color_input_5.value;
    
    change_bg_2(color_value_1);
    change_lb_2(color_value_2);
    change_ft_2(color_value_3);
    change_mu_2(color_value_4);
    change_wp_2(color_value_5);
}
/* ----------------------------------------------------------- */
function change_bg_3(color_code) {
    var color_value = color_code;
    var color_bg_1 = [];
    var color_bg_2 = [];
    var color_bg_3 = [];
    var color_bg_4 = [];
    var color_bg_6 = [];

    color_bg_1.push(document.querySelector('.header'));
    color_bg_1.push(document.querySelector('.header_logo'));
    color_bg_1.push(document.querySelector('.header_search'));
    color_bg_1.push(document.querySelector('.header_menu'));
    color_bg_1.push(document.querySelector('.header_info'));
    color_bg_1.push(document.querySelector('.footer'));
    color_bg_1.push(document.querySelector('.footer_box_0'));
    color_bg_1.push(document.querySelector('.footer_box_2'));
    color_bg_1.push(document.querySelector('.text_menus_0'));
    color_bg_1.push(document.querySelector('.labels'));
    color_bg_1.push(document.querySelector('.labelss'));
    color_bg_1.push(document.querySelector('.labelsss'));
    color_bg_1.push(document.querySelector('.market_button'));
    color_bg_1.push(document.querySelector('.calculator_button'));
    color_bg_1.push(document.querySelector('.csv_button'));
    color_bg_1.push(document.querySelector('.name_button'));
    color_bg_1.push(document.querySelector('.table_button > table'));
    for (var i = 0; i < color_bg_1.length; i++) {
        color_bg_1[i].style.backgroundColor = String(color_value);
    }
    
    color_bg_2.push(document.querySelectorAll('.label'));
    for (var i = 0; i < color_bg_2[0].length; i++) {
        color_bg_2[0][i].style.backgroundColor = String(color_value);
    }
    
    color_bg_6.push(document.querySelectorAll('.info_0'));
    for (var i = 0; i < color_bg_6[0].length; i++) {
        color_bg_6[0][i].style.backgroundColor = String(color_value);
    }

    color_bg_3.push(document.querySelector('.text_boxs'));
    color_bg_3.push(document.querySelector('.text_boxss'));
    for (var i = 0; i < color_bg_3.length; i++) {
        color_bg_3[i].style.border = '1px solid ' + String(color_value);
    }

    var color_bg_5 = document.querySelector('.auto_search_icon');
    color_bg_5.style.color = String(color_value);
}

function change_lb_3(color_code) {
    var color_value = color_code;
    var color_lb = [];
    var color_lb_1 = [];

    color_lb.push(document.querySelector('.menu'));
    for (var i = 0; i < color_lb.length; i++) {
        color_lb[i].style.backgroundColor = String(color_value);
    }
    
    color_lb_1.push(document.querySelector('.content_0'));
    color_lb_1.push(document.querySelector('.content_1'));
    color_lb_1.push(document.querySelector('.content_2'));
    for (var i = 0; i < color_lb_1.length; i++) {
        color_lb_1[i].style.border = '5px solid ' + String(color_value);
    }
}

function change_ft_3(color_code) {
    var color_value = color_code;
    var color_ft = [];
    var color_ft_1 = [];
    var color_ft_2 = [];
    var color_ft_3 = [];

    color_ft_1.push(document.querySelectorAll('.footer_link > a'));
    color_ft_1.push(document.querySelectorAll('.footer_dev > a'));
    color_ft_1.push(document.querySelectorAll('.footer_info > a'));
    for (var i = 0; i < color_ft_1[0].length; i++) {
        color_ft_1[0][i].style.color = String(color_value);
        color_ft_1[1][i].style.color = String(color_value);
        color_ft_1[2][i].style.color = String(color_value);
    }

    color_ft_2.push(document.querySelector('.footer_email'));
    color_ft_2.push(document.querySelector('.footer_count'));
    color_ft_2.push(document.querySelector('.header_color_box > i'));
    color_ft_2.push(document.querySelector('.header_color_box > p'));
    color_ft_2.push(document.querySelector('.header_language_box > i'));
    color_ft_2.push(document.querySelector('.header_language_box > p'));
    color_ft_2.push(document.querySelector('.icon_11 > i'));
    color_ft_2.push(document.querySelector('.text_menu'));
    for (var i = 0; i < color_ft_2.length; i++) {
        color_ft_2[i].style.color = String(color_value);
    }

    color_ft_3.push(document.querySelectorAll('.label > a'));
    color_ft_3.push(document.querySelectorAll('.content_1_title > a'));
    for (var i = 0; i < color_ft_3[0].length; i++) {
        color_ft_3[0][i].style.color = String(color_value);
        color_ft_3[1][i].style.color = String(color_value);
    }
}

function change_mu_3(color_code) {
    var color_value = color_code;
    var color_mu = [];
    var color_mu_1 = [];

    color_mu.push(document.querySelector('.text_boxss'));
    color_mu.push(document.querySelector('.text_boxss_1'));
    color_mu.push(document.querySelector('.text_boxss_2'));
    color_mu.push(document.querySelector('.text_boxss_3'));
    color_mu.push(document.querySelector('.mobile_menus'));
    for (var i = 0; i < color_mu.length; i++) {
        color_mu[i].style.backgroundColor = String(color_value);
    }
}

function change_wp_3(color_code) {
    var color_value = color_code;
    var color_wp = [];
    var color_wp_1 = [];
    var color_wp_2 = [];
    
    color_wp_1.push(document.querySelector('.content_0'));
    color_wp_1.push(document.querySelector('.content_1'));
    color_wp_1.push(document.querySelector('.content_2'));
    for (var i = 0; i < color_wp_1.length; i++) {
        color_wp_1[i].style.backgroundColor = String(color_value);
    }
}

function change_ct_3() {
    var color_input_1 = document.getElementById("custom_color_1");
    var color_input_2 = document.getElementById("custom_color_2");
    var color_input_3 = document.getElementById("custom_color_3");
    var color_input_4 = document.getElementById("custom_color_4");
    var color_input_5 = document.getElementById("custom_color_5");
    var color_value_1 = color_input_1.value;
    var color_value_2 = color_input_2.value;
    var color_value_3 = color_input_3.value;
    var color_value_4 = color_input_4.value;
    var color_value_5 = color_input_5.value;
    
    change_bg_3(color_value_1);
    change_lb_3(color_value_2);
    change_ft_3(color_value_3);
    change_mu_3(color_value_4);
    change_wp_3(color_value_5);
}
/* ----------------------------------------------------------- */