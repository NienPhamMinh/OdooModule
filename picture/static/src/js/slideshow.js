import publicWidget from 'web.public.widget';

publicWidget.registry.SlideShow = publicWidget.Widget.extend({
    selector: '.slide-show',

//     /**
//      * @override
//      */
    start() {
    //    let images = this.el.querySelector('#images')
    //    if (images) {
 
    //         this.rpc({
    //             route:'/slideshow/',
    //             params:{}
    //         }).then(data=>{
    //             let html=''
    //             data.forEach(hinh => {
                        
    //                     html +=<div class="mySlides fade">
    //                     <img src="data:image/png;base64,${hinh.image}" style="width:100%"/>
    //                     <div class="text">Caption Text</div>
    //                   </div>
                    
    //             })
    //             images.innerHTML = html
    //         })
    //     }
    },
});

// export default publicWidget.registry.SlideShow;
// odoo.define('SlideShow.script', function (require) {
//     'use strict';
//     var ajax = require('web.ajax');

//     $(document).ready(function () {
//         ajax.jsonRpc("/slideshow/", 'call', {})
//             .then(function (data) {
//                 var imgElement = document.getElementById('images');
//                 imgElement.src = data.image_url;
                
//             });
//     });
// });
