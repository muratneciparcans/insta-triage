import { Component } from '@angular/core';
import { WebsocketService } from './websocket.service';
import {PatientModel} from './Patient.model'

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public payloads: any = [];
  public patient: PatientModel = new PatientModel();

  public estimated_waiting_time: string;

  constructor(private ws: WebsocketService) {}

  ngOnInit() {
    this.ws.on('data', (data) => {
      console.log(data);
      // do stuff
      this.payloads.push(data);
      for (let k of Object.getOwnPropertyNames(data)) {
        console.log(k, ' :',  data[k])
        this.patient[k] = data[k];
      }
      console.log(this.patient);
    });
  }
}
