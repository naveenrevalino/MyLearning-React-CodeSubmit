import "./Pagination.css";


/**
 * 
 * @param param1 : Total : Total number of records we get from database.
 * @param param2 : Limit : Number of records to display on each page.
 * @param param3 : setCurrentPageNumber : Manages the current page state.
 * 
 * @returns : Pagination buttons to be displayed at the bottom of the parients grid.
 */

// Create Array : Based on the size of the records returned from the database.
const range = ( start:number, end:number ) => {
    return ( [...Array(end).keys()].map( (eachElement)=> eachElement+start) )
}

const Pagination = ( { total, limit, setCurrentPageNumber }) => {

    const pageCount = Math.ceil( total/limit );
    const pages = range(1, pageCount);


    return (
    <ul className="pagination">
        <button onClick={ () => {setCurrentPageNumber(pages[0])} } className="pagination-jump">First</button>
        {
            pages.map( (eachPage) => (
            <button key={eachPage} onClick={ () => {setCurrentPageNumber(eachPage)} } className="pagination-button">{eachPage}</button>
            ))
        }
        <button onClick={ () => {setCurrentPageNumber(pages.length)} } className="pagination-jump">Last</button>
    </ul>
    );

}

export default Pagination;