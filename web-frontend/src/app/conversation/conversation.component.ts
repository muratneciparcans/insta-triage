import { Component, OnInit } from '@angular/core';
import { Direction, MessageModel } from '../models/message.model';
import {WebsocketService} from '../websocket.service';

@Component({
  selector: 'app-conversation',
  templateUrl: './conversation.component.html',
  styleUrls: ['./conversation.component.scss']
})
export class ConversationComponent implements OnInit {

  public messages: MessageModel[] = [];

  constructor(
    private ws: WebsocketService
  ) {
    const messageIn: MessageModel = new MessageModel(Direction.IN, 'I am message INPUT payload');
    const messageOut: MessageModel = new MessageModel(Direction.OUT, 'I am message OUTPUT payload');
    ws.on('message', (data) => {
      console.log(data)
    })
  }

  ngOnInit() {
  }

}
