import { Component, OnInit } from '@angular/core';
import { RequestComponent } from './request/request.component';
import { RequestService} from './request.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{

  requests: RequestComponent[];

   constructor(private requestService: RequestService){

   }

   ngOnInit(){
      return this.requestService.getRequests()
      .subscribe(data=> this.requests = data);
   }
}
