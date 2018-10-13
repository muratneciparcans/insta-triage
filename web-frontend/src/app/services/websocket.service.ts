import { Injectable } from '@angular/core';

import * as io from 'socket.io-client';
import * as ss from 'socket.io-stream';

import { WebCamComponent } from 'ng2-webcam';

import { environment } from "../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class WebsocketService {

  // stuff
  private url = environment.baseURL;
  private socket;

  constructor() {
    this.socket = io.connect(this.url);
  }
  on(event: string, callback: Function) {
    this.socket.on(event, callback);
  }
  send( video: string ) {
    this.socket.emit(video);
    this.socket.send(video);
  }
}
