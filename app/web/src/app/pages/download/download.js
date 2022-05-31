import React from "react"

const Download = () => {

   return (
      <div className="page-wrapper mb-2" style={{minHeight: '90vh'}}>
         <div className="container-xl mt-2 ">
            <div className="card  p-1 p-md-2 pt-md-3 mb-2 ">
               <h1 className="text-center">
                  {'تحميل'}
                  <span className="text-primary">{'قُطْرُب'}</span>
               </h1>
            </div>
            <div className="row">
               <div className="col-8 col-sm-5 col-md-5 col-lg-3 mb-2 m-auto">
                     <div className="card text-center p-1 pt-3">
                        <div className="avatar avatar-xl m-auto m-4 mb-3">
                           <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24"
                                 strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round"
                                 strokeLinejoin="round">
                                 <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                                 <path
                                    d="M17.8 20l-12 -1.5c-1 -.1 -1.8 -.9 -1.8 -1.9v-9.2c0 -1 .8 -1.8 1.8 -1.9l12 -1.5c1.2 -.1 2.2 .8 2.2 1.9v12.1c0 1.2 -1.1 2.1 -2.2 1.9z" />
                                 <line x1="12" y1="5" x2="12" y2="19" />
                                 <line x1="4" y1="12" x2="20" y2="12" />
                           </svg>
                        </div>
                        <h3>{'تحميل لل windows'}</h3>
                        <a href="https://sourceforge.net/projects/qutrub/" className="btn btn-outline-primary m-auto">{'تحميل'}</a>
                     </div>
               </div>
               <div className="col-8 col-sm-5 col-md-5 col-lg-3 mb-2 m-auto">
                  <div className="card text-center p-1 pt-3">
                     <div className="avatar avatar-xl m-auto m-4 mb-3">
                        <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M8 9l3 3l-3 3" /><line x1="13" y1="15" x2="16" y2="15" /><rect x="3" y="4" width="18" height="16" rx="2" /></svg>
                     </div>
                     <h3>{'تحميل لل Linux'}</h3>
                     <a href="https://sourceforge.net/projects/qutrub/" className="btn btn-outline-primary m-auto">{'تحميل'}</a>
                  </div>
               </div>
               <div className="col-8 col-sm-5 col-md-5 col-lg-3 mb-2 m-auto">
                  <div className="card text-center p-1 pt-3">
                     <div className="avatar avatar-xl m-auto m-4 mb-3">
                           <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M6 20.735a2 2 0 0 1 -1 -1.735v-14a2 2 0 0 1 2 -2h7l5 5v11a2 2 0 0 1 -2 2h-1" /><path d="M11 17a2 2 0 0 1 2 2v2a1 1 0 0 1 -1 1h-2a1 1 0 0 1 -1 -1v-2a2 2 0 0 1 2 -2z" /><line x1="11" y1="5" x2="10" y2="5" /><line x1="13" y1="7" x2="12" y2="7" /><line x1="11" y1="9" x2="10" y2="9" /><line x1="13" y1="11" x2="12" y2="11" /><line x1="11" y1="13" x2="10" y2="13" /><line x1="13" y1="15" x2="12" y2="15" /></svg>
                     </div>
                     <h3>{'ملف مضغوط'}</h3>
                     <a href="https://sourceforge.net/projects/qutrub/files/qutrub0.9.zip/download" className="btn btn-outline-primary m-auto">{'تحميل'}</a>
                  </div>
               </div>
               <div className="col-8 col-sm-5 col-md-5 col-lg-3 mb-2 m-auto">
                  <div className="card text-center p-1 pt-3">
                     <div className="avatar avatar-xl m-auto m-4 mb-3">
                        <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round"><path stroke="none" d="M0 0h24v24H0z" fill="none"/><path d="M9 19c-4.3 1.4 -4.3 -2.5 -6 -3m12 5v-3.5c0 -1 .1 -1.4 -.5 -2c2.8 -.3 5.5 -1.4 5.5 -6a4.6 4.6 0 0 0 -1.3 -3.2a4.2 4.2 0 0 0 -.1 -3.2s-1.1 -.3 -3.5 1.3a12.3 12.3 0 0 0 -6.2 0c-2.4 -1.6 -3.5 -1.3 -3.5 -1.3a4.2 4.2 0 0 0 -.1 3.2a4.6 4.6 0 0 0 -1.3 3.2c0 4.6 2.7 5.7 5.5 6c-.6 .6 -.6 1.2 -.5 2v3.5" /></svg>
                     </div>
                     <h3>{'رابط الملف المصدري'}</h3>
                     <a href="https://github.com/linuxscout/qutrub" className="btn btn-outline-primary m-auto">{'تحميل'}</a>
                  </div>
               </div>
            </div>
         </div>
      </div>
   )

}

export default Download