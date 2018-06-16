import { Injectable } from '@angular/core';

import * as io from 'socket.io-client';
import * as ss from 'socket.io-stream';

import { WebCamComponent } from 'ng2-webcam';

@Injectable()
export class WebsocketService {

  // stuff
  private url = 'http://localhost:5000';
  private socket;

  constructor() {
    this.socket = io.connect(this.url);
    this.testVideo();
  }

  public testVideo() {
    // video
    // var file = e.target.files[0];
    // var video = null;
    // var stream = ss.createStream();
    //
    // // upload a file to the server.
    // ss(this.socket).emit('file', stream, {size: video.size});
    // ss.createBlobReadStream(video).pipe(stream);

    // let video = this.hardwareVideo.nativeElement;

    // const n = <any>navigator;
    // n.getUserMedia = ( n.getUserMedia || n.webkitGetUserMedia || n.mozGetUserMedia  || n.msGetUserMedia );
    // n.mediaDevices.getUserMedia({ video: true }).then(function(stream) {
    //   // console.log( stream );
    //   // console.log( window.URL.createObjectURL(stream) );
    //   // video.src = window.URL.createObjectURL(stream);
    //   // video.play();
    //
    //   // we now have a stream
    //   // we now can send to websocket
    // });
  }

  on(event: string, callback: Function) {
    this.socket.on(event, callback);
  }
}
