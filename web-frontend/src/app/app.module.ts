import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { VideoShowComponent } from './video-show/video-show.component';
import { ConversationComponent } from './conversation/conversation.component';


@NgModule({
  declarations: [
    AppComponent,
    VideoShowComponent,
    ConversationComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
