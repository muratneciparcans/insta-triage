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
    console.log(this.videoEl);
    this.ws.on('video', (data) => {
      console.log(data);
      this.setVideoUrl(data.file);
    });
  }

  setVideoUrl(url: string) {
    this.videoEl.nativeElement.src = url;
    this.videoEl.nativeElement.play();
  }

}
