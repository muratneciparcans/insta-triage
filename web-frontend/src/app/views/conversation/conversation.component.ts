import { Component, OnInit } from '@angular/core';
import { Direction, MessageModel } from '../../models/message.model';
import {WebsocketService} from '../../services/websocket.service';

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
    ws.on('message', (data) => {
      console.log(data);
      const msg = new MessageModel(
        data.direction === 'in' ? Direction.IN : Direction.OUT,
        data.message
      );
      this.messages.push(msg);
    });
  }

  ngOnInit() {
  }

}
