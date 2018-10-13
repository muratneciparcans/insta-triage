import { Component, Input, OnInit } from '@angular/core';
import { Direction, MessageModel } from './../../models/message.model';

@Component({
  selector: 'app-message',
  templateUrl: './message.component.html',
  styleUrls: ['./message.component.scss']
})
export class MessageComponent implements OnInit {

  @Input('message') message: MessageModel;

  constructor() { }

  ngOnInit() {
    console.log(this.message);
  }

  isMessageMe( message: MessageModel ): boolean {
    return (message.direction === Direction.IN);
  }
}
