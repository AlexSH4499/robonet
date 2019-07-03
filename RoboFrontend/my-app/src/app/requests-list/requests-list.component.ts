import {Component, OnInit} from '@angular/core';

import {requests} from '../requests-list/requests';
import {RequestService} from '../request.service';

@Component({
    selector: 'app-requests-list',
    templateUrl: './requests-list.component.html',
    styleUrls: ['./requests-list.component.css']
})

export class RequestsListComponent implements OnInit{
    requests = [];

    // share(){
    //     window.alert('Something happened');
    // }

    constructor(private requestService: RequestService){
        this.requests = requestService.getRequests();
    }

    ngOnInit(){

    }
}   