import "./index.css";
import PatientCard from "../PatientCard";

const PatientPage = () => {
  //🥸 Hook the component with the api
  return (
    <div className="PatientPage-container">
      <div className="PatientPage-title">
        <h2>Patients</h2>
      </div>
      <div className="PatientPage-cards">
        {[
          {
            id: 1,
            first_name: "John",
            last_name: "Doe",
            email: "john.doe@gmail.com",
            date_of_birth: "1990-01-01",
          },
          {
            id: 2,
            first_name: "Jane",
            last_name: "Doe",
            email: "jane.doe@gmail.com",
            date_of_birth: "1990-01-01",
          },
        ].map((patient) => (
          <PatientCard key={patient.id} patient={patient} onDelete={() => {}} />
        ))}
      </div>
    </div>
  );
};

export default PatientPage;
