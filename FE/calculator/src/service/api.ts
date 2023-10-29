import axios from "axios";
import {getSupportedOperatorsResponse, postCalculateResponse} from "./responses";
import {postCalculateRequest} from "./requests";

const URLS = {
    "getSupportedOperators": "/api/operators",
    "postCalculateResponse": "/api/calculate",
}
export const getSupportedOperators = (): Promise<getSupportedOperatorsResponse> => {
    return axios.get<getSupportedOperatorsResponse>(URLS.getSupportedOperators).then((response) => {
        return response.data
    })
}
export const postCalculate = (request: postCalculateRequest): Promise<postCalculateResponse> => {
    return axios.post<postCalculateResponse>(URLS.postCalculateResponse, request).then((response) => {
        return response.data
    })
}