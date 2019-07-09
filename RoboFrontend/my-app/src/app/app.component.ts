import { Component, OnInit } from '@angular/core';
import { RequestComponent, Movement } from './request/request.component';
import { RequestService} from './request.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  requests: RequestComponent[];
  moveModel = new Movement(11,1,false,
                              0.0,0.0,0.0,0.0,0.0,0.0);
   constructor(private requestService: RequestService){

   }

   ngOnInit(){
      return this.requestService.getRequests()
      .subscribe(data=> this.requests = data);
   }
}
