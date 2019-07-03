import {Injectable} from '@angular/core';
import {HttpClient} from '@angular/common/http';
// import { HttpClient } from 'selenium-webdriver/http';
import {RequestComponent} from './request/request.component';
const DJANGO_API = 'http://192.168.1.21:8000/requests/'

@Injectable({
    providedIn: 'root'
})

export class RequestService{

    requests ;

    askServerForRequests(){
        // Here we need to identify how to make HTTP requests to our django server
    }

    constructor(private http: HttpClient){

    }

    getRequests(){
        // return this.requests;
        this.requests = this.http.get<RequestComponent[]>(DJANGO_API);
        return this.requests;
    }

    clearRequests(){
        this.requests = [];
        return this.requests;
    }
}