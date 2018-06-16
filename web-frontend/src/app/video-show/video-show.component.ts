import { Component, OnInit } from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
  selector: 'app-video-show',
  templateUrl: './video-show.component.html',
  styleUrls: ['./video-show.component.scss']
})
export class VideoShowComponent implements OnInit {

  constructor(
    private ws: WebsocketService
  ) {
    ws.on('video', (data) => {
      console.log(data)
    });
  }

  ngOnInit() {
  }

}
