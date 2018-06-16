import { Component } from '@angular/core';
import { WebsocketService } from './websocket.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  public payloads: any = [];

  public estimated_waiting_time: string;

  constructor(private ws: WebsocketService) {}

  ngOnInit() {
    this.ws.on('registry', (data) => {
      console.log(data);
      // do stuff
      this.payloads.push(data.payload);
    });
  }
}
