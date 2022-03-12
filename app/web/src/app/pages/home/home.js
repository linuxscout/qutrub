import React, {useState} from "react"
import * as axios from "axios"
import Toastify from 'toastify-js'
import tashaphyne from "../../../assets/image/projects/tashaphyne.png"
import ayaspell from "../../../assets/image/projects/ayaspell.png"
import adawat from "../../../assets/image/projects/adawat.png"
import pyarabic from "../../../assets/image/projects/pyarabic.png"
import radif from "../../../assets/image/projects/radif.png"

axios.defaults.baseURL = 'http://127.0.0.1:5000';

const Home = () => {

    const [all_times, handle_all_times] = useState(true)
    const [json_table, set_json_table] = useState(undefined)
    const [result_area, set_result_area] = useState(undefined)
    const [modal_body, set_modal_body] = useState(undefined)
    const [modal_title, set_modal_title] = useState(undefined)

    const toggel_adawat = () => {
        let adawat_area = document.getElementById("adawat-area")

        if (adawat_area.classList.contains('d-none')) {
            adawat_area.classList.remove('d-none');
        } else {
            adawat_area.classList.add('d-none');
        }
    }

    const random_text = () => {
        let input_text_field = document.getElementById('input-text-field');

        axios.post('ajaxGet', {
            data: { "response_type": 'get_random_text' },
        })
            .then(function (response) {
                input_text_field.value = response.data.text;
                input_text_field.focus();
            })
            .catch(function (error) {
                console.log(error);
                set_view_error();
            });
    }

    const set_view_error = () => {
        let result_area = (
            <div className="loading d-flex flex-column justify-content-center align-items-center text-danger"
            style={{minHeight: '150px'}}>
            <div className="avatar bg-white avatar-md mb-0">
                <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                    viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                    stroke-linecap="round" stroke-linejoin="round">
                    <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                    <path stroke="red" d="M12 9v2m0 4v.01" />
                    <path stroke="red"
                        d="M5 19h14a2 2 0 0 0 1.84 -2.75l-7.1 -12.25a2 2 0 0 0 -3.5 0l-7.1 12.25a2 2 0 0 0 1.75 2.75" />
                </svg>
            </div>
            <h4 className="mt-0 ">حدث خطأ</h4>
            </div>
        );
        set_result_area(result_area);
    }

    const remove_text = () => {
        let input_text_field = document.getElementById('input-text-field');
        input_text_field.value = "";
    }

    const request_data = () => {

        let config_data = load_config_data();
        // init clear view
        set_view_empty_input();
        if (config_data['text'] == '') {
            set_view_empty_input();
            return;
        }

        // update url of the page
        //  https://qutrub.arabeyes.org/?verb=خرج
        update_url(config_data['text']);

        set_view_loading();
        axios.post('ajaxGet', {
            data: config_data,
        })
            .then(function (response) {
                console.log(response);
                set_view_done(response);
                set_json_table(response.data.result);
            })
            .catch(function (error) {
                console.log(error);
                set_view_error();
            });
    }

    const set_view_loading = () => {
        let result_area = (
            <div className="loading d-flex flex-column justify-content-center align-items-center"
            style={{minHeight: '150px'}}>
            <div className="loader"></div>
            <h4 className="mt-3 text-primary">تحميل ...</h4>
            </div>
        );
        set_result_area(result_area);
    }

    const _update_modal = (table) => {
        let input_text_field = document.getElementById('input-text-field');
        let modal_title_content= (<>تصريف للفعل <span className='text-primary'>{input_text_field.value}</span></>);
        set_modal_title(modal_title_content)
        set_modal_body(table);
    }

    const update_url = (verb) => {
        if (history.pushState) {
            var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + `?verb=${verb}`;
            window.history.pushState({path:newurl},'',newurl);
        }
    }

    const set_view_done = (response) => {
        let option_view = _build_options();
        let table_view = _build_table(response.data.result);

        view_suggestions(response.data.suggest);
        let verb_info = <h3>{response.data.verb_info}</h3>;

        let result_area = []
        result_area.push(verb_info)
        result_area.push(option_view)
        result_area.push(table_view)

        set_result_area(result_area);
        _update_modal(table_view);
    }

    const _build_table = (result) => {
        let tabel_content = [];

        tabel_content.push(_get_header(result['0']));
        tabel_content.push(_get_body(result));

        return (
            <div className="table-responsive">
                <table className="table table-vcenter card-table">
                    {tabel_content}
                </table>
            </div>
        );
    }

    const _get_header = (data) => {
        let headers = [];
        for (let index in data) {
            headers.push(<th className="text-primary table-head-title">{data[index]}</th>);
        }

        return <thead><tr>{headers}</tr></thead>;
    }

    const _get_body_row = (items) => {
        let row = [];
        for (let index in items) {
            row.push(<td className="curson-pointer" onClick={copy_text(items[index])} title={`نسخ الفعل ${items[index]}`} >{items[index]}</td>);
        }

        return <tr>{row}</tr>;
    }

    const _get_body = (data) => {
        let rows = [];
        for (let index in data) {
            if (index == 0) continue;
            rows.push(_get_body_row(data[index]));
        }

        return <tbody>{rows}</tbody>;
    }

    const copy_text = (text) => {
        navigator.clipboard.writeText(text);
        show_alert("تم نسخ الفعل " + text);
    }

    const _build_options = () => {
        return (<div className="container d-flex pt-1 pb-1ss" title="تكبير">
            <button href="#" className="btn btn-outline me-2" data-bs-toggle="modal" data-bs-target="#modal-tasrif-view">
                <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="10" cy="10" r="7" /><line x1="7" y1="10" x2="13" y2="10" /><line x1="10" y1="7" x2="10" y2="13" /><line x1="21" y1="21" x2="15" y2="15" /></svg>
                         <span>تكبير</span>
            </button>
            <button className="btn btn-outline  text-black dropdown me-2 " title="نسخ" >
            <span  className="dropdown-toggle text-black"  data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> نسخ الجدول</span>
                              <div className="dropdown-menu dropdown-menu-end">
                                <a className="dropdown-item" onClick={copy_as_html} >نسخ ك HTML</a>
                                <a className="dropdown-item" onClick={copy_as_csv} >نسخ ك csv</a>
                              </div>
            </button>
            <button href="#" className="btn btn-outline me-2 " onClick={share_page_link}>
            <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><circle cx="6" cy="12" r="3" /><circle cx="18" cy="6" r="3" /><circle cx="18" cy="18" r="3" /><line x1="8.7" y1="10.7" x2="15.3" y2="7.3" /><line x1="8.7" y1="13.3" x2="15.3" y2="16.7" /></svg>
                     <span>مشاركة</span>
            </button>
        </div>);
    }

    const share_page_link = () => {
        let link = location.href;
        navigator.clipboard.writeText(link);

        show_alert("تم نسخ رابط الموقع")
    }

    const copy_as_html = () => {
        let table = generate_html_table();
        navigator.clipboard.writeText(table);

        show_alert(" تم نسخ الجدول ك html")
    }

    const generate_html_table = () => {
        alert(json_table)
        if (json_table == undefined || json_table == null || json_table == "") {
            return;
        }

        let raw_table = '<table>';

        for (let row_index in json_table) {
            if (json_table.hasOwnProperty(row_index)) {
                let row = '<tr>'
                for (let cell_index in json_table[row_index]) {
                    if (json_table[row_index].hasOwnProperty(cell_index)) {
                        let cell = null;
                        if (row_index == 0) {
                            cell = `<th>${json_table[row_index][cell_index]} </th>`

                        } else {
                            cell = `<td>${json_table[row_index][cell_index]} </td>`
                        }

                        row += cell;
                    }
                }
                row += "</tr>"
                raw_table += row;
            }
        }
        raw_table += "</table>"

        return raw_table;
    }

    const copy_as_csv = () => {
        let csv = generate_csv_table()
        navigator.clipboard.writeText(csv);

        show_alert(" تم نسخ الجدول ك csv")
    }

    const generate_csv_table = () => {
        if (json_table == undefined || json_table == null || json_table == "") {
            return;
        }

        let raw_table = '';

        for (let row_index in json_table) {
            if (json_table.hasOwnProperty(row_index)) {
                let row = ''
                for (let cell_index in json_table[row_index]) {
                    if (json_table[row_index].hasOwnProperty(cell_index)) {
                        let cell = `${json_table[row_index][cell_index]},`
                        row += cell;
                    }
                }
                row += "\n"
                raw_table += row;
            }
        }

        return raw_table;
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

    const view_suggestions = (data) => {
        let suggest_area = document.getElementById('suggest-area');

        // if data is empty don't show suggest area
        if (data == null || data == undefined || data.length < 1) {
            suggest_area.innerHTML = ``;
            return;
        }

        let html = ``;
        for (let index in data) {
            html += `<li className="curson-pointer" >&nbsp;<span className="text-primary" onclick="request_data_suggest('${data[index].verb}', '${data[index].haraka}', ${data[index].transitive})">${data[index].verb} &nbsp; ${data[index].future}</span></li>`;
        }
        suggest_area.innerHTML = `
        <h4 className="mt-0 ">هل تقصد؟ </h4>
        <ul className="mb-0" >`+ html + `</ul>`;
    }

    const set_view_empty_input = () => {
        // by set null as argument the suggested view area will be hidden
        view_suggestions(null);

        let result_area = (
            <div className="loading d-flex flex-column justify-content-center align-items-center text-yellow"
            style={{minHeight: "150px"}}>
            <div className="avatar bg-white avatar-md mb-0">
                <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none" stroke-linecap="round" stroke-linejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M4 20h4l10.5 -10.5a1.5 1.5 0 0 0 -4 -4l-10.5 10.5v4" /><line x1="13.5" y1="6.5" x2="17.5" y2="10.5" /></svg>
            </div>
            <h4 className="mt-0 ">أدخل النص أولا</h4>
            </div>
        );
        set_result_area(result_area);
    }

    const load_config_data = () => {
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

    const toggel_adawat_times = () => {
        let adawat_area = document.getElementById("adawat-times-area")

        if (all_times) {
            handle_all_times(false)
            adawat_area.classList.add('d-none');
        } else {
            handle_all_times(true)
            adawat_area.classList.remove('d-none');
        }
    }

    return (
    <>
        <div className="page-wrapper mb-2" style={{minHeight: '90vh'}}>
            <div className="container-fluid mt-2">
                <div className="row">
                    <div className="col-12 col-md-12 col-lg-9">
                        <div className="card">
                            <div className="container d-flex pt-1 pb-1 justify-content-end" title="أدوات">
                                <button className="btn btn-outline me-2 " onClick={toggel_adawat}>
                                <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                        viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                        <path d="M3 21h4l13 -13a1.5 1.5 0 0 0 -4 -4l-13 13v4"></path>
                                        <line x1="14.5" y1="5.5" x2="18.5" y2="9.5"></line>
                                        <polyline points="12 8 7 3 3 7 8 12"></polyline>
                                        <line x1="7" y1="8" x2="5.5" y2="9.5"></line>
                                        <polyline points="16 12 21 17 17 21 12 16"></polyline>
                                        <line x1="16" y1="17" x2="14.5" y2="18.5"></line>
                                </svg>
                                    <span> أدوات</span>
                                </button>
                                <button className="btn btn-outline me-2 " title="فعل عشوائي" onClick={random_text}>

                                    <svg xmlns="http://www.w3.org/2000/svg" className="icon me-0 me-md-2" width="24" height="24"
                                        viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                        <line x1="21" y1="17" x2="3" y2="17"></line>
                                        <path d="M6 10l-3 -3l3 -3"></path>
                                        <line x1="3" y1="7" x2="21" y2="7"></line>
                                        <path d="M18 20l3 -3l-3 -3"></path>
                                    </svg>
                                    <span className="d-none d-sm-block"> فعل عشوائي</span>
                                </button>
                                <button className="btn btn-outline me-2 " data-bs-toggle="modal" data-bs-target="#modal-simple"
                                    title="مساعدة">

                                    <svg xmlns="http://www.w3.org/2000/svg" className="icon me-0 me-md-2" width="24" height="24"
                                        viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                        <circle cx="12" cy="12" r="9"></circle>
                                        <line x1="12" y1="17" x2="12" y2="17.01"></line>
                                        <path d="M12 13.5a1.5 1.5 0 0 1 1 -1.5a2.6 2.6 0 1 0 -3 -4"></path>
                                    </svg>
                                    <span className="d-none d-sm-block">مساعدة</span>
                                </button>
                                <button className="btn btn-outline me-2 " title="مسح" onClick={remove_text}>
                                    <svg xmlns="http://www.w3.org/2000/svg" className="icon me-0 me-md-2" width="24" height="24"
                                        viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                        stroke-linecap="round" stroke-linejoin="round">
                                        <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                        <line x1="18" y1="6" x2="6" y2="18"></line>
                                        <line x1="6" y1="6" x2="18" y2="18"></line>
                                    </svg>
                                    <span className="d-none d-sm-block"> مسح</span>
                                </button>
                            </div>
                        </div>
                        <div className="card mt-2 pt-2 pb-2">
                            <div className="container">
                                <form onSubmit={(event) => {event.preventDefault()}}>
                                    <label className="form-label mb-0 text-primary ">أدخل الفعل</label>
                                    <input id="input-text-field" type="text" className="form-control " name="example-text-input"
                                        placeholder="أدخل الفعل ..." autofocus="" />
                                    <div className="container-fluid d-flex mt-2 ">
                                        <a type="button" className="btn btn-primary me-2  d-none d-md-block"
                                            style={{maxHeight: '40px'}} onClick={request_data}>تصريف الفعل</a>
                                        <div id="adawat-area" className="container-fluid  mb-0 mb-md-2 pt-2 d-none">
                                            <div className="mb-md-3 mb-0">
                                                <div className="form-label text-primary">أدوات</div>
                                                <div>
                                                    <label className="form-check form-check-inline">
                                                        <input id="transitive-checkbox-input" className="form-check-input"
                                                            type="checkbox" checked />
                                                        <span className="form-check-label">متعدي </span>
                                                    </label>
                                                    <label className="form-check form-check-inline">
                                                        <input id="all-checkbox-input" className="form-check-input" type="checkbox"
                                                            onClick={toggel_adawat_times} checked={all_times} />
                                                        <span className="form-check-label">كل الأزمنة</span>
                                                    </label>
                                                    <div id="adawat-times-area"
                                                        className="border pt-2 p-1 mb-2 rounded-1 pb-0 d-none">
                                                        <label className="form-check form-check-inline">
                                                            <input id="past-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label">الماضي </span>
                                                        </label>
                                                        <label className="form-check form-check-inline">
                                                            <input id="future-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label">المضارع </span>
                                                        </label>
                                                        <label className="form-check form-check-inline">
                                                            <input id="imperative-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label">الأمر </span>
                                                        </label>
                                                        <label className="form-check form-check-inline">
                                                            <input id="passive-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label"> المبني للمجهول </span>
                                                        </label>
                                                        <label className="form-check form-check-inline">
                                                            <input id="future_moode-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label"> المضارع المنصوب و المجزوم </span>
                                                        </label>
                                                        <label className="form-check form-check-inline">
                                                            <input id="confirmed-checkbox-input" className="form-check-input"
                                                                type="checkbox" checked />
                                                            <span className="form-check-label">المؤكد </span>
                                                        </label>
                                                    </div>
                                                </div>
                                                <label className="form-check form-check-inline ps-0">
                                                    <span className="form-check-label">حركة عين المضارع
                                                        <select id="future_type-select-input" className="form-select-inline">
                                                            <option defaultValue="فتحة" selected>الفتحة</option>
                                                            <option defaultValue="ضمة"> "الضمة</option>
                                                            <option defaultValue="كسرة"> "الكسرة</option>
                                                        </select>
                                                        للفعل الثلاثي فقط
                                                    </span>
                                                </label>
                                            </div>
                                        </div>
                                    </div>
                                    <a type="button" className="btn btn-primary me-2 d-md-none d-block"
                                        onClick={request_data}>تصريف الفعل</a>

                                </form>
                            </div>
                        </div>

                        <div className="card mt-2 mb-3">
                            <div id="suggest-area" className="suggest p-2">
                            </div>
                            <div id="result-area" className="result" style={{minHeight: '150px'}}>
                                {result_area}
                            </div>
                        </div>
                    </div>
                    <div className="col-md-3 d-none d-lg-block">
                        <div className="card mb-2">
                            <div className="container pt-2 pb-1">
                                <h3 className="text-primary mb-1 "> ماهو قُطْرُب ؟</h3>
                                <p>
                                برنامج قطرب <b>لتصريف الأفعال العربية</b>، في الأزمنة ويسندها إلى الضمائر.
            قطرب برنامج مفتوح المصدر، يوفّر للمستخدم استعمالا مجانيا، في شكل موقع وب، وبرنامج لسطح المكتب.
        وللمطورين يُستخدم كمكتبة برمجية من الموقع أو على مكتبات بيثون.
        يصرّف قطرب الأفعال العربية بسهولة ويسر، ويساعد المستخدم في التعلم، وتصحيح معلوماته.

                                    <a href="{{ url_for('doc')}}"> المزيد عن قطرب</a>
                                </p>

                            </div>
                        </div>
                        <div className="card mb-2">
                            <div className="container pt-2 pb-1">
                                <h3 className="text-primary mb-1 ">تحميل قُطْرُب</h3>
                                <a href="http://sourceforge.org/projects/qutrub"><img src="https://img.shields.io/sourceforge/dt/qutrub.svg"/> </a>
                                <div className="container mb-3 d-flex align-items-center justify-content-center">
                                    <a href="{{ url_for('download') }}" className="btn btn-outline-info ">
                                        <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24"
                                            viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" fill="none"
                                            stroke-linecap="round" stroke-linejoin="round">
                                            <path stroke="none" d="M0 0h24v24H0z" fill="none"></path>
                                            <path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2 -2v-2"></path>
                                            <polyline points="7 11 12 16 17 11"></polyline>
                                            <line x1="12" y1="4" x2="12" y2="16"></line>
                                        </svg>
                                        <span> تحميل</span>
                                    </a>
                                </div>


                            </div>
                        </div>
                        <div className="card mb-2" style={{minHeight: '300px'}}>
                            <div className="container pt-2 pb-2">
                                <h3 className="text-primary">مشاريع أخرى</h3>
                                <div className="row">
                                    <div className="col-4">
                                        <img className="me-2"
                                            src={tashaphyne} alt=""
                                            srcset="" />
                                    </div>
                                    <div className="col-8 align-items-center d-flex">
                                        <a href="http://pypi.python.org/pypi/Tashaphyne/"> تاشفين: التجذيع الخفيف للنصوص
                                            العربية</a>
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-4">
                                        <img className="me-2" src={ayaspell}
                                            alt="" srcset="" />
                                    </div>
                                    <div className="col-8 align-items-center d-flex">
                                        <a href="http://ayaspell.sf.net/">آية سبل، القاموس العربي الحر للتدقيق الإملائي</a>
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-4">
                                        <img src={adawat} alt=""
                                            srcset="" />
                                    </div>
                                    <div className="col-8 align-items-center d-flex">
                                        <a href="http://adawat.sf.net/">أدوات النص العربي</a>
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-4">
                                        <img src={pyarabic} alt=""
                                            srcset="" />
                                    </div>
                                    <div className="col-8 align-items-center d-flex">
                                        <a href="http://pypi.python.org/pypi/PyArabic/">مكتبة برمجية للغة العربية بلغة بيثون</a>
                                    </div>
                                </div>

                                <div className="row">
                                    <div className="col-4">
                                        <img src={radif} alt=""
                                            srcset="" />
                                    </div>
                                    <div className="col-8 align-items-center d-flex">
                                        <a href="http://radif.sf.net/">معجم المترادفات والأضداد والقوافي والجموع</a>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div className="modal modal-blur fade" id="modal-simple" tabIndex="-1" style={{display: 'none'}} aria-hidden="true">
            <div className="modal-dialog modal-dialog-centered" role="document">

                <div className="modal-content">
                    <div className="modal-header">
                        <h5 className="modal-title">مساعدة</h5>
                        <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                        <ul>
                            <li>أكتب الفعل في الخانة، ثم اضغط على زر <span className="text-primary">تصريف الفعل</span>.</li>

                            <li>انتظر حتى تظهر النتيجة.</li>

                            <li>اضغط على <span className="text-primary">فعل عشوائي</span> للحصول على اقتراحات أخرى.</li>

                            <li>اضغط على زر <span className="text-primary">أدوات</span> أخرى للحصول على خدمات أخرى.</li>
                        </ul>
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn me-auto" data-bs-dismiss="modal">غلق</button>

                    </div>
                </div>
            </div>
        </div>

        <div className="modal modal-blur fade" id="modal-tasrif-view" tabIndex="-1" aria-hidden="false">
            <div className="modal-dialog modal-full-width modal-dialog-centered" role="document">
                <div className="modal-content">
                    <div className="modal-header">
                    <h5 className="modal-title">{modal_title}</h5>
                    <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                    </div>
                    <div className="modal-body">
                        {modal_body}
                    </div>
                    <div className="modal-footer">
                        <button type="button" className="btn me-auto" data-bs-dismiss="modal">غلق</button>
                    </div>
                </div>
            </div>
        </div>
    </>
   )
}

export default Home
