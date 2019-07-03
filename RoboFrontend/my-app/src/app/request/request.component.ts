import { Component, OnInit } from '@angular/core';
import { FormBuilder} from "@angular/forms";
import {RequestService} from '../request.service';


@Component({
  selector: 'app-request',
  templateUrl: './request.component.html',
  styleUrls: ['./request.component.css']
})

export class RequestComponent implements OnInit {
  uid: number;
  robot_to_send:1;
  executed: boolean;
  joint_1:number;
  joint_2:number;
  joint_3:number;
  joint_4:number;
  joint_5:number;
  joint_6:number;
  data:[];

  requestForm;

  constructor(private requestService: RequestService,
              private formBuilder: FormBuilder,) {
                  this.data = this.requestService.getRequests();

                  this.requestForm = this.formBuilder.group({
                    uid:'',
                    robot_to_send:'',
                    executed:'',
                    joint_1:'',
                    joint_2:'',
                    joint_3: '',
                    joint_4:'',
                    joint_5:'',
                    joint_6:''
                  });
               }
        
  ngOnInit() {
  }

  onSubmit(requestData){
      console.warn('Request for robot has been submitted', requestData);

      this.data =this.requestService.clearRequests();//This doesn't work with data cause i never use it, must specify each variable individually
      this.requestForm.reset();
  }
}
