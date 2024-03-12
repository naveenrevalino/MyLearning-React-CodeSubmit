// FIXME: 🥸 Connect with the api

import axios from "axios";

const getBaseURL = axios.create({
    
    // Configuration : BaseURL, Timeout, Header, and so on.
    baseURL: 'http://localhost:8000',
    
})

export default getBaseURL;
