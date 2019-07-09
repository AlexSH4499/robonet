import { Component, OnInit } from '@angular/core';
// import { FormBuilder} from "@angular/forms";
import {RequestService} from '../request.service';
// import { REACTIVE_FORM_DIRECTIVES } from '@angular/forms';
import { FormGroup, FormControl, Validators, FormBuilder }  from '@angular/forms';

@Component({
  selector: 'app-request',
  templateUrl: './request.component.html',
  styleUrls: ['./request.component.css']
})

export class RequestComponent implements OnInit {

  rangeValue: number;
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

               }
        
  ngOnInit() {
    this.data = this.requestService.getRequests();

    this.requestForm = this.formBuilder.group({
      uid:11,
      robot_to_send:1,
      executed:false,
      joint_1:0.0,
      joint_2:0.0,
      joint_3: 0.0,
      joint_4:0.0,
      joint_5:0.0,
      joint_6:0.0
    });
    this.data = this.requestService.getRequests();
  }

  onSubmit(requestData){
      console.warn('Request for robot has been submitted', requestData);
      
      // var request = '{"uid":'+this.uid+
      // ',"robot_to_send":'+this.robot_to_send+
      // ',"executed":'+this.executed +
      // ',"joint_1":'+this.joint_1+
      // ',"joint_2":'+this.joint_2+
      // ',"joint_3":'+this.joint_3 +
      // ',"joint_4":'+this.joint_4+
      // ',"joint_5":'+this.joint_5+
      // ',"joint_6":'+this.joint_6+'}';
                            
      // var request = {"uid":this.uid
      //                 ,"robot_to_send":this.robot_to_send
      //                 ,"executed":this.executed 
      //                 ,"joint_1":this.joint_1
      //                 ,"joint_2":this.joint_2
      //                 ,"joint_3":this.joint_3
      //                 ,"joint_4":this.joint_4
      //                 ,"joint_5":this.joint_5
      //                 ,"joint_6":this.joint_6};

      this.requestService.addRequest(requestData).subscribe(data => console.log('Success',data),error => console.error('', error));
      //this.data =this.requestService.clearRequests();//This doesn't work with data cause i never use it, must specify each variable individually
      this.uid =  0;
      this.robot_to_send = 1;
      this.executed = false;
      this.joint_1 = 0.0;
      this.joint_2 = 0.0;
      this.joint_3= 0.0;
      this.joint_4 = 0.0;
      this.joint_5= 0.0;
      this.joint_6 = 0.0;
      this.requestForm.reset();
  }
}


export interface MovementRequest{
  uid: Number;
  robot_to_send: Number;
  executed: boolean;
  joint_1:Number;
  joint_2:Number;
  joint_3:Number;
  joint_4:Number;
  joint_5:Number;
  joint_6:Number;
}

export class Movement{

  constructor(
    public uid: Number,
    public robot_to_send: Number,
    public executed: boolean,
    public joint_1:Number,
    public joint_2:Number,
    public joint_3:Number,
    public joint_4:Number,
    public joint_5:Number,
    public joint_6:Number
  ){}
}