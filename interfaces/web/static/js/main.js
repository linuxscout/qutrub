

function toggel_adawat() {
    let adawat_area = document.getElementById("adawat-area")

    if (adawat_area.classList.contains('d-none')) {
        adawat_area.classList.remove('d-none');
    } else {
        adawat_area.classList.add('d-none');
    }
}

function toggel_adawat_times(element) {
    let adawat_area = document.getElementById("adawat-times-area")

    if (element.checked) {
        adawat_area.classList.add('d-none');
    } else {
        adawat_area.classList.remove('d-none');
    }
}

function random_text() {

    let input_text_field = document.getElementById('input-text-field');

    var config = {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    axios.post('/ajaxGet', {
        data: { "response_type": 'get_random_text' },
    })
        .then(function (response) {
            console.log(response)
            input_text_field.value = response.data.text;
        })
        .catch(function (error) {
            console.log(error);
            set_view_error();
        });
}


function remove_text() {
    let input_text_field = document.getElementById('input-text-field');
    input_text_field.value = "";
}

/*-----------------------*/


function load_config_data() {
    // text 
    let input_text_field = document.getElementById('input-text-field');

    // adawat 
    let all_input = document.getElementById('all-checkbox-input');
    let transitive_input = document.getElementById('transitive-checkbox-input');

    // times
    let past_input = document.getElementById('past-checkbox-input');
    let future_input = document.getElementById('future-checkbox-input');
    let imperative_input = document.getElementById('imperative-checkbox-input');
    let passive_input = document.getElementById('passive-checkbox-input');
    let future_moode_input = document.getElementById('future_moode-checkbox-input');
    let confirmed_input = document.getElementById('confirmed-checkbox-input');

    let future_type_input = document.getElementById('future_type-select-input');


    let config_data = {
        'text': input_text_field.value, 'action': 'Conjugate',
        'all': all_input.checked, 'transitive': transitive_input.checked, 'past': past_input.checked, 'future': future_input.checked,
        'imperative': imperative_input.checked, 'future_moode': future_moode_input.checked, 'confirmed': confirmed_input.checked,
        'passive': passive_input.checked, 'future_type': 'فتحة'
    }

    for (let option of future_type_input.children) {
        if (option.selected) {
            config_data["future_type"] = option.value;
            break;
        }
    }

    return config_data;
}


function request_data() {

    let config_data = load_config_data();

    if (config_data['text'] == '') {
        set_view_empty_input();
        return;
    }

    var config = {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    set_view_loading();
    axios.post('/ajaxGet', {
        data: config_data,
    })
        .then(function (response) {
            console.log(response);
            set_view_done(response)
        })
        .catch(function (error) {
            console.log(error);
            set_view_error();
        });
}
//~ function request_data_suggest(verb, transitive, future_type) {
function request_data_suggest(verb, future_type, transitive) {

    let config_data = {
        'text': verb, 'action': 'Conjugate',
        'all': 1, 'transitive': transitive, 'future_type': future_type
        //~ 'all': true, 'transitive': true, 'future_type': future_type
    };

    if (config_data['text'] == '') {
        set_view_empty_input();
        return;
    }

    var config = {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    set_view_loading();
    axios.post('/ajaxGet', {
        data: config_data,
    })
        .then(function (response) {
            console.log(response);
            set_view_done(response)
        })
        .catch(function (error) {
            console.log(error);
            set_view_error();
        });
}


function set_view_loading() {
    let result_area = document.getElementById('result-area');
    result_area.innerHTML = `
    <div class="loading d-flex flex-column justify-content-center align-items-center"
    style="min-height: 150px;">
    <div class="loader"></div>
    <h4 class="mt-3 text-primary">تحميل ...</h4>
    </div>
    `;
}

function set_view_error() {
    let result_area = document.getElementById('result-area');
    result_area.innerHTML = `
    <div class="loading d-flex flex-column justify-content-center align-items-center text-danger"
    style="min-height: 150px;">
    <div class="avatar bg-white avatar-md mb-0">
        <!-- Download SVG icon from http://tabler-icons.io/i/alert-triangle -->
        <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24"
            viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
            stroke-linecap="round" stroke-linejoin="round">
            <path stroke="none" d="M0 0h24v24H0z" fill="none" />
            <path stroke="red" d="M12 9v2m0 4v.01" />
            <path stroke="red"
                d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75" />
        </svg>
    </div>
    <h4 class="mt-0 ">حدث خطأ</h4>
</div>
    `;
}

function set_view_empty_input() {
    let result_area = document.getElementById('result-area');
    result_area.innerHTML = `
    <div class="loading d-flex flex-column justify-content-center align-items-center text-yellow"
    style="min-height: 150px;">
    <div class="avatar bg-white avatar-md mb-0">
        <!-- Download SVG icon from http://tabler-icons.io/i/pencil -->
        <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 20h4l10.5 -10.5a1.5 1.5 0 0 0 -4 -4l-10.5 10.5v4" /><line x1="13.5" y1="6.5" x2="17.5" y2="10.5" /></svg>
    </div>
    <h4 class="mt-0 ">أدخل النص أولا</h4>
</div>
    `;
}

function view_suggestions(data) {
    // if data is empty don't show suggest area
    if (data == null || data == undefined || data.length < 1) {
        return;
    }

    let result_area = document.getElementById('suggest-area');
    let html = ``;
    for (let index in data) {
        html += `<li class="curson-pointer" >&nbsp;<span class="text-primary" onclick="request_data_suggest('${data[index].verb}', '${data[index].haraka}', ${data[index].transitive})">${data[index].verb} &nbsp; ${data[index].future}</span></li>`;
    }
    result_area.innerHTML = `
    <h4 class="mt-0 ">هل تقصد؟ </h4>
    <ul class="mb-0" >`+ html + `</ul>`;
}

function set_view_done(response) {
    // let fake_data = {
    //     "0": {
    //         "0": "الضمائر",
    //         "1": "الماضي المعلوم",
    //         "2": "المضارع المعلوم",
    //         "3": "المضارع المجزوم",
    //         "4": "المضارع المنصوب",
    //         "5": "المضارع المؤكد الثقيل",
    //         "6": "الأمر",
    //         "7": "الأمر المؤكد",

    //     },
    //     "1": {
    //         "0": "أنا",
    //         "1": "خَرَجْتُ",
    //         "2": "أَخْرَجُ",
    //         "3": "أَخْرَجْ",
    //         "4": "أَخْرَجَ",
    //         "5": "أَخْرَجَنَّ",
    //         "6": "",
    //         "7": "",

    //     },
    //     "2": {
    //         "0": "نحن",
    //         "1": "خَرَجْنَا",
    //         "2": "نَخْرَجُ",
    //         "3": "نَخْرَجْ",
    //         "4": "نَخْرَجَ",
    //         "5": "نَخْرَجَنَّ",
    //         "6": "",
    //         "7": "",

    //     },
    //     "3": {
    //         "0": "أنت",
    //         "1": "خَرَجْتَ",
    //         "2": "تَخْرَجُ",
    //         "3": "تَخْرَجْ",
    //         "4": "تَخْرَجَ",
    //         "5": "تَخْرَجَنَّ",
    //         "6": "اِخْرَجْ",
    //         "7": "اِخْرَجَنَّ",

    //     },

    // };

    let result_area = document.getElementById('result-area');

    let option_view = _build_options();
    let table_view = _build_table(response.data.result);
    // print suggestions
    console.log("Suggedtions", response.data.suggest);
    view_suggestions(response.data.suggest);
    result_area.innerHTML = option_view + table_view;
    _update_modal(table_view);


}

function _build_options() {
    return `<div class="container d-flex pt-1 pb-1 " title="أدوات">
        <a href="#" class="btn btn-outline me-2 " data-bs-toggle="modal" data-bs-target="#modal-tasrif-view">
            <!-- Download SVG icon from http://tabler-icons.io/i/eye -->
            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="10" cy="10" r="7" /><line x1="7" y1="10" x2="13" y2="10" /><line x1="10" y1="7" x2="10" y2="13" /><line x1="21" y1="21" x2="15" y2="15" /></svg>      
                     <span>تكبير</span>
        </a>
<!-- 
        <a href="#" class="btn btn-white" data-bs-toggle="modal" data-bs-target="#modal-full-width">
            Full width modal
          </a> 
        <a href="#" class="btn btn-outline me-2  " onclick="_print_table()">
            <svg xmlns="http://www.w3.org/2000/svg" class="icon me-0 me-md-2" width="24" height="24"
                viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path
                    d="M17 17h2a2 2 0 0 0 2 -2v-4a2 2 0 0 0 -2 -2h-14a2 2 0 0 0 -2 2v4a2 2 0 0 0 2 2h2" />
                <path d="M17 9v-4a2 2 0 0 0 -2 -2h-6a2 2 0 0 0 -2 2v4" />
                <rect x="7" y="13" width="10" height="8" rx="2" />
            </svg>
            <span class="d-none d-sm-block"> طباعة</span>

        </a>
        <a href="#" class="btn btn-outline me-2 " title="نص عشوائي">
            <svg xmlns="http://www.w3.org/2000/svg" class="icon " width="24" height="24"
                viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M14 3v4a1 1 0 0 0 1 1h4" />
                <path
                    d="M11.5 21h-4.5a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v5m-5 6h7m-3 -3l3 3l-3 3" />
            </svg> 
            <span class="d-sm-none d-block">JSON</span>
            <span class="d-none d-sm-block"> إستخراج صيغة JSON</span>
        </a>

        <a href="#" class="btn btn-outline me-2 " title="نص عشوائي" >
           
            <svg xmlns="http://www.w3.org/2000/svg" class="icon" width="24" height="24"
                viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                stroke-linecap="round" stroke-linejoin="round">
                <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                <path d="M14 3v4a1 1 0 0 0 1 1h4" />
                <path
                    d="M11.5 21h-4.5a2 2 0 0 1 -2 -2v-14a2 2 0 0 1 2 -2h7l5 5v5m-5 6h7m-3 -3l3 3l-3 3" />
            </svg> 
            <span class="d-sm-none d-block">CSV</span>
            <span class="d-none d-sm-block"> إستخراج صيغة CSV</span>
        </a> -->
    </div>`;
}

function _build_table(result) {

    let tabel_content = "";

    tabel_content += _get_header(result['0']);
    delete result["0"];
    tabel_content += _get_body(result);

    return `
    <div class="table-responsive">
        <table class="table table-vcenter card-table">
            ${tabel_content}
        </table>
    </div>

    `;
}


function _get_header(data) {
    headers = "";
    for (let index in data) {
        headers += `<th class="text-primary table-head-title">${data[index]}</th>`;
    }

    return `<thead><tr>${headers}</tr></thead>`;
}

function _get_body(data) {
    let rows = "";
    for (let index in data) {
        rows += _get_body_row(data[index]);
    }

    return `<tbody>${rows}</tbody>`;
}

function _get_body_row(items) {
    let row = "";
    for (let index in items) {
        row += `<td class="curson-pointer" onclick="copy_text('${items[index]}')" title="نسخ الفعل ${items[index]} " >${items[index]}</td>`
    }

    return `<tr>${row}</tr>`;
}

function _update_modal(table) {
    let modal_view = document.getElementById('modal-tasrif-view');
    let modal_title = modal_view.getElementsByClassName('modal-title')[0];
    let modal_body = modal_view.getElementsByClassName('modal-body')[0];

    let input_text_field = document.getElementById('input-text-field');
    modal_title.innerHTML = ` تصريف للفعل <span class='text-primary'>${input_text_field.value}</span>`;


    modal_body.innerHTML = table;
}



function copy_text(text) {
    /* Copy the text inside the text field */
    navigator.clipboard.writeText(text);
    /* Alert the copied text */
    show_alert("تم نسخ الفعل " + text);
}


function show_alert(text) {
    Toastify({
        text: text,
        duration: 2000,
        className: "info text-primary border border-primary border-1 rounded-2  ",
        style: {
            background: "white",
            'direction': 'rtl',
            'text-align': 'right',
        }
    }).showToast();
}


// TODO: add pring version for later
/*
function _print_table() {
    let config_data = load_config_data();

    config_data['response_type'] = 'pdf';

    var config = {
        headers: {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        }
    }

    axios.post('/ajaxGet', {
        data: config_data,
    })
        .then(function (response) {
         //   console.log(response);
            var a = window.open('', '', '');
            a.document.write(response.data);
            a.document.close();
            a.print();
        })
        .catch(function (error) {
            console.log(error);
        });
}*/
