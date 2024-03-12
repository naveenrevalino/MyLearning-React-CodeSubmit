import "./index.css";
import PatientCard from "../PatientCard";
import {useState, useEffect} from "react";
import getBaseURL from "../../../api/toubib";
import Pagination from "../Pagination/Pagination";

const PatientPage = () => {
  //🥸 Hook the component with the api

  // STATE 1 : Maintains Patients Array List:
  const [patient, setPatient] = useState([]);

  // STATE 2 : To Manage Current Page Number Selected By The User : Initially(1)
  const [ currentPageNumber, setCurrentPageNumber ] = useState(1);

  // Number Of Records To Fetch:
  const limit:number = 100;

  // Number Of Records Per Page:
  const numOfRecordsPerPage:number = 10;

  // Calculate - Last Post Index : Number of the last record displayed (in the current page ).
  const lastPostIndex:number = currentPageNumber * numOfRecordsPerPage;

  // Calculate - First Post Index : Number of the first record displayed (in the current page ).
  const firstPostIndex:number = lastPostIndex - numOfRecordsPerPage;
 
  // Slice - Patients Array : Based on firstPostIndex and  lastPostIndex.
  const slicedPatientRecords = patient.slice( firstPostIndex, lastPostIndex );

  // Fetch Patients List
  const fetchPatients = async() =>{
    // const response = await getPatientRecords.get(`/v1/patients?offset=${0}&limit=${limit}`)
    await getBaseURL.get(`/v1/patients`, { params:{offset:0, limit:limit} })
    .then( function(response) { setPatient(response.data.data), console.log(response)  })
    .catch( function(error) { console.log(error)})
  }

  // Delete Patient ( Required : Patient ID )
  const deletePatientHandler = async(patient_id:number) => {
    const confirmOperation = window.confirm("Click on Ok to delete the patient record.");
    if (confirmOperation) {
    await getBaseURL.delete(`/v1/patients/`+ patient_id)
    .then( (response) => { 
      if (response.status = 204) {
        const updatedList = patient.filter( p => p.id !==patient_id )
        setPatient(updatedList)
      }
     })
    .then( () => { console.log(`Patient Record ID: ${patient_id} has been deleted`) })
    .catch( (error) => { console.log(error) })
    }
  }

  // UseEffect : To Load Patients Record When App Mounts
  useEffect( () => {
    fetchPatients();
  }, [ ])

  return (
  
  <div className="PatientPage-container">
    
    <div className="PatientPage-title">
      <h2>Patients</h2>
    </div>
    
    <div className="PatientPage-cards"> 
      {
      // Render Sliced Patient Record To Patient Card With Pagination
      slicedPatientRecords.map(
        // (patient) => ( <PatientCard key={patient.id} patient={patient} onDelete={(patient_id:number) => {deletePatientHandler(patient_id)} } />)
        (patient) => ( <PatientCard key={patient.id} patient={patient} onDelete={ deletePatientHandler} />)
        )
      }
    </div>
    
    <Pagination totalNumberOfPatientsRecord={patient.length} numberOfRecordsPerPage={numOfRecordsPerPage} setCurrentPage={setCurrentPageNumber} />

  </div>
  );
};

export default PatientPage;
