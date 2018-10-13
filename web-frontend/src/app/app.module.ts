import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { VideoShowComponent } from './views/video-show/video-show.component';
import { ConversationComponent } from './views/conversation/conversation.component';
import { MessageComponent } from './views/message/message.component';

@NgModule({
  declarations: [
    AppComponent,
    VideoShowComponent,
    ConversationComponent,
    MessageComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
