import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
// import { HttpClient } from 'selenium-webdriver/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';
import {RequestComponent, MovementRequest} from './request/request.component';
const DJANGO_API = 'http://192.168.1.21:8000/requests'

const httpOptions = {
    headers: new HttpHeaders({
        'Content-Type':'application/json',
        'Authorization':'Basic'+ 'mec123:mec123'
    })
};

@Injectable({
    providedIn: 'root'
})

export class RequestService{

    requests  ;

    // askServerForRequests(){
    //     // Here we need to identify how to make HTTP requests to our django server
    // }

    constructor(private http: HttpClient){
        this.requests = [];
    }

    addRequest(request:JSON){
        //Should do an HTTP POST Method
        // this.requests.push(request);
        return this.http.post(DJANGO_API, request, {
            headers: {
                "Access-Control-Allow-Headers": "Access-Control-Allow-Credentials,access-control-allow-methods,Access-Control-Allow-Methods,Access-Control-Allow-Origin,Origin,Accept, X-Requested-With, Access-Control-Request-Method, Access-Control-Request-Headers,Content-Type, Authorization, user, password",
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Methods": "GET,HEAD,OPTIONS,POST,PUT",
                "Access-Control-Allow-Credentials": "true",
                'Content-Type':'application/json',
                'user': 'mec123',
                'password': 'mec123'
            }
        })
        .pipe(
            // catchError(this.handleError('addRequest', request))
            // console.log("Uh-oh something went wrong while posting!");
        );
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
