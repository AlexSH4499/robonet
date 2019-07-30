import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RequestsListComponent } from './requests-list/requests-list.component';
import { RequestComponent } from './request/request.component';
import {RequestService} from './request.service';
import {FormsModule} from '@angular/forms';
import {ReactiveFormsModule} from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import {MDCDataTable} from '@material/data-table';
import {MatButtonModule, MatCheckboxModule, MatSliderModule} from '@angular/material';

@NgModule({
  declarations: [
    AppComponent,
    RequestsListComponent,
    RequestComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule,
    BrowserAnimationsModule,
    MatSliderModule,
  ],
  providers: [RequestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
