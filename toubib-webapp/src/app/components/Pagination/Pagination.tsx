
import "./Pagination.css";

const Pagination = ( { totalNumberOfPatientsRecord, numberOfRecordsPerPage, setCurrentPage }) => {

    // Create an array with the page numbers
    let pageNumbers = [];
    for ( let i = 1; i<= Math.ceil(totalNumberOfPatientsRecord/numberOfRecordsPerPage) ; i++ ) {
        pageNumbers.push(i);
    }

    return (
    <div className="pagination">
        {
        pageNumbers.map
        (
            (pageNumber, index) => {
                return (
                <button key={index} onClick={ () => {setCurrentPage(pageNumber)} } className="pagination-button">{pageNumber}</button>
                )
            } 
        )
        }
    </div>
    );

}

export default Pagination;