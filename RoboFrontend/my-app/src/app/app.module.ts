import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RequestsListComponent } from './requests-list/requests-list.component';
import { RequestComponent } from './request/request.component';
import {RequestService} from './request.service';

@NgModule({
  declarations: [
    AppComponent,
    RequestsListComponent,
    RequestComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [RequestService],
  bootstrap: [AppComponent]
})
export class AppModule { }
