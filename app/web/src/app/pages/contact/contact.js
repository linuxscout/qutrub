import React, { useEffect } from "react";

const Contact = () => {

   const handleDisqus = () => {
      /* * * CONFIGURATION VARIABLES: EDIT BEFORE PASTING INTO YOUR WEBPAGE * * */
      var disqus_shortname = 'mishkal'; // required: replace example with your forum shortname

      /* * * DON'T EDIT BELOW THIS LINE * * */

      var dsq = document.createElement('script'); dsq.type = 'text/javascript'; dsq.async = true;
      dsq.src = 'http://' + disqus_shortname + '.disqus.com/embed.js';
      (document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(dsq);

   }

   useEffect(() => {
      handleDisqus()
   },[]);

   return (
      <div className="page-wrapper mb-2" style={{minHeight: '90vh'}}>
    <div className="container-xl mt-2 ">
        <div className="card mb-2 p-4">
            <h3 className="text-primary">المطورون</h3>

            <ul>
                <li>برمجة المكتبات و الموقع: <a href="http://tahadz.wordpress.com">طه زروقي</a> (taha.zerrouki at gmail dot com)
                </li>
                <li>برمجة واجهة الموقع: <a href="https://www.linkedin.com/in/tarek-berkane-58bb151ba/">طارق بركان</a> (berkane.t320 at gmail dot com)
                </li>
            </ul>
        </div>

        <div className="card mb-2 p-4">
            <h1>اُترك تعليقا</h1>

            <div id="disqus_thread"></div>
        </div>

        <div className="card d-none d-md-block mb-2 p-4">
            <h1>للاتصال بنا</h1>
            <iframe className="m-auto text-center" height="500" frameborder="0" marginheight="0" marginwidth="0" src=
            "https://docs.google.com/spreadsheet/embeddedform?formkey=dG9vWVQ2NG9JaUNCOGRYYkdkZ2pKOGc6MA"
            width="760">Loading...</iframe>
        </div>

        <div className="card d-md-none mb-2 p-4">
            <h1>للاتصال بنا</h1><iframe className="m-auto" height="500" width="300" frameborder="0"  marginheight="0" marginwidth="0" src=
            "https://docs.google.com/spreadsheet/embeddedform?formkey=dG9vWVQ2NG9JaUNCOGRYYkdkZ2pKOGc6MA"
            width="760">Loading...</iframe>
        </div>
    </div>
</div>

   )
}

export default Contact
