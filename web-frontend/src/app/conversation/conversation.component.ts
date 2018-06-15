import { Component, OnInit } from '@angular/core';
import { Direction, MessageModel } from '../models/message.model';

@Component({
  selector: 'app-conversation',
  templateUrl: './conversation.component.html',
  styleUrls: ['./conversation.component.scss']
})
export class ConversationComponent implements OnInit {

  public messages: MessageModel[] = [];

  constructor() {
    const messageIn: MessageModel = new MessageModel(Direction.IN, 'I am message INPUT payload');
    const messageOut: MessageModel = new MessageModel(Direction.OUT, 'I am message OUTPUT payload');

    this.messages.push(messageIn);
    this.messages.push(messageIn);
    this.messages.push(messageOut);
    this.messages.push(messageIn);
    this.messages.push(messageOut);
  }

  ngOnInit() {
  }

}
