import { Component, OnInit } from '@angular/core';
import { WebsocketService } from './websocket.service';
import {PatientModel} from './Patient.model'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})

export class AppComponent implements OnInit {
  public patient: PatientModel = new PatientModel();
  constructor(private ws: WebsocketService) {}

  ngOnInit() {
    this.ws.on('data', (data) => this.checkDataFromPayload(data) );
    this.ws.on('reset', (data) => this.reset(data));
  }

  reset(data: any) {
    console.log('Reset DATA: ', data);
    this.patient = new PatientModel();
  }

  checkDataFromPayload(data: any) {
    console.log('Payload DATA', data);
    for (let k of Object.getOwnPropertyNames(data)) {
      console.log(k, ' :',  data[k])
      this.patient[k] = data[k];
    }
    console.log(this.patient);
  }

  getProgressValue(): number {
    return this.patient.pain * 10;
  }
}


