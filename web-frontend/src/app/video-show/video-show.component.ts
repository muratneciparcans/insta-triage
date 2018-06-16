import { Component, ElementRef, OnInit, ViewChild } from '@angular/core';
import {WebsocketService} from '../websocket.service';

@Component({
  selector: 'app-video-show',
  templateUrl: './video-show.component.html',
  styleUrls: ['./video-show.component.scss']
})
export class VideoShowComponent implements OnInit {

  @ViewChild('videoEl') videoEl: ElementRef;

  constructor(
    private ws: WebsocketService
  ) {}

  ngOnInit() {
    this.ws.on('video', (data) => {
      console.log(data);
      this.setVideoUrl(data.file);
    });

    this.ws.send('started');
  }

  setVideoUrl(url: string) {
    this.videoEl.nativeElement.src = 'http://localhost:4200' + url;
    this.videoEl.nativeElement.play();
  }

}
