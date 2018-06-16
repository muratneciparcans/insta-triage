import { Component, OnInit } from '@angular/core';
import { WebsocketService } from './websocket.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  public name: string;
  public born: Date;

  public estimated_waiting_time: string;

  public pain: number;

  public no_patient: boolean;

  public patient_infos: string[] = [
    'Pain in the left arm',
    'The patient is not able to move the limb'
  ];

  constructor(private ws: WebsocketService) {}

  ngOnInit() {
    this.ws.on('registry', (data) => this.checkDataFromPayload(data.payload) );
    this.ws.on('reset', (data) => this.reset(data));
  }

  reset(data: any) {
    console.log("Reset DATA: ", data);
  }

  checkDataFromPayload(payload: any) {
    console.log("Payload DATA", payload);
    // @todo: implement
  }

  getProgressValue(): number {
    return this.pain * 10;
  }
}


