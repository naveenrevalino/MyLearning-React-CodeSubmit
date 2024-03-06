import "./index.css";

const PatientCard = ({ patient, onDelete }) => {
  return (
    <div className="PatientCard-container">
      <button onClick={() => onDelete(patient.id)}>X</button>
      <h3>
        {patient.first_name} {patient.last_name}
      </h3>
      <p>{patient.email}</p>
      <p>{patient.date_of_birth}</p>
    </div>
  );
};

export default PatientCard;
