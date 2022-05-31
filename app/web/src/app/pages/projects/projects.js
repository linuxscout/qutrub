import React, {useState, useEffect} from "react"
import * as axios from "axios"
import './projects.css'

const Projects = () => {
   const [libraries, set_libraries] = useState(undefined)
   const [websites, set_websites] = useState(undefined)
   const [is_mounted, set_mounted] = useState(false)

   useEffect(() => {
      axios.get('projects')
      .then(function (response) {
         console.log(response)
         set_libraries(response.data.libraries)
         set_websites(response.data.websites)
         set_mounted(true)
      })
   },[]);

    const show_more = (container_id, event) => {
        let project_container = document.getElementById(container_id);
        project_container?.classList.remove('hide-extra-card')
        event.target.remove();
    }

   return is_mounted && (<div className="page-wrapper">
   <div className="container-xl mt-2 " style={{minHeight: '90vh'}}>
     <div className="cntainer-libraries py-2 hide-extra-card" id="libraries-project-area">
       <h2 className="text-primary">المكتبات البرمجية</h2>
       <div className="row">
         {libraries.map((library, index) => (
         <div className={`col-lg-3 col-md-4 col-sm-6 my-2 ${index > 8 && 'extra-card'} m-auto`} key={index}>
           <div className="card ">
             <div className="card-body text-center">

               <div className="text-area" style={{height: '90px'}}>
                 <a href={library.link} className="link" target="blank" style={{textDecoration: 'none'}}>
                   <h2>{library.title}</h2>
                 </a>
                 {library.description}
               </div>
             </div>
             <div className="card-footer text-center">
               <div className="link-area">
                 <a href={library.link} className="mx-1" title="github" target="blank">
                   <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24"
                     strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round">
                     <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                     <path d="M12 9h-7a2 2 0 0 0 -2 2v4a2 2 0 0 0 2 2h3" />
                     <path d="M12 15h7a2 2 0 0 0 2 -2v-4a2 2 0 0 0 -2 -2h-3" />
                     <path
                       d="M8 9v-4a2 2 0 0 1 2 -2h4a2 2 0 0 1 2 2v5a2 2 0 0 1 -2 2h-4a2 2 0 0 0 -2 2v5a2 2 0 0 0 2 2h4a2 2 0 0 0 2 -2v-4" />
                     <line x1="11" y1="6" x2="11" y2="6.01" />
                     <line x1="13" y1="18" x2="13" y2="18.01" />
                   </svg>
                 </a>
                 {(library.website) &&
                  <a href={library.website} className="mx-1" title="موقع" target="blank">
                   <svg xmlns="http://www.w3.org/2000/svg" className="icon" width="24" height="24" viewBox="0 0 24 24"
                     strokeWidth="2" stroke="currentColor" fill="none" strokeLinecap="round" strokeLinejoin="round">
                     <path stroke="none" d="M0 0h24v24H0z" fill="none" />
                     <circle cx="12" cy="12" r="9" />
                     <ellipse cx="12" cy="12" rx="4" ry="9" />
                     <ellipse cx="12" cy="12" rx="4" ry="9" transform="rotate(90 12 12)" />
                   </svg>
                 </a>
                 }
               </div>
             </div>
           </div>
         </div>
         ))}
       </div>
       <div className="container text-center">
         {(libraries.length > 8) &&
         <a className="text-primary curson-pointer" style={{textDecoration: 'none'}}
           onClick={(event) => show_more('libraries-project-area',event)}>
           <h3>إظهار المزيد</h3>
         </a>
         }
       </div>
     </div>
     <div className="cntainer-libraries py-2 hide-extra-card" id="websites-project-area">
       <h2 className="text-primary">مشاريع أخرى </h2>
       <div className="row">
       {websites.map((website, index) => (
         <div className={`col-lg-3 col-md-4 col-sm-6 my-2 ${index > 8 && 'extra-card'} m-auto`} key={index}>
           <div className="card ">
             <div className="card-body text-center">
               <div className="text-area d-flex justify-content-center align-items-center" style={{height: '60px'}}>
                 <a href={website.link} className="link" target="blank" style={{textDecoration: 'none'}}>
                   <h4 className="mb-0 ">{website.title}</h4>
                 </a>
               </div>
             </div>
           </div>
         </div>
       ))}
       </div>
       <div className="container text-center">
         {(websites.length > 8) &&
         <a className="text-primary curson-pointer" style={{textDecoration: 'none'}}
           onClick={(event) => show_more('websites-project-area', event)}>
           <h3>إظهار المزيد</h3>
         </a>
         }
       </div>
     </div>
   </div>
 </div>
)
}

export default Projects
