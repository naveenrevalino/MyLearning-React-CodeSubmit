import "./index.css";
import PatientImage from "../../../assets/avatar.png";

const PatientCard = ({ patient, onDelete }) => {
 
  return (
    <div className="PatientCard-cell" style={{display: "inline-block"}}>

      <div className="PatientCard-container">

        <img src={ PatientImage } alt="PatientImage" className="PatientCard-img"></img>
        <button onClick={() => onDelete(parseInt(patient.id))} className="PatientCard-button">X</button>
        
        <div className="PatientCard-body">
          <h3>
            {patient.first_name} {patient.last_name}
          </h3>
          <p>{patient.email}</p>
          <p>{patient.date_of_birth}</p>
        </div>

      </div>
      
    </div>
  );
};

export default PatientCard;
