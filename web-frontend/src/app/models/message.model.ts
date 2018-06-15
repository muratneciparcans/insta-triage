
export enum Direction {
  IN, OUT
}
export class MessageModel {
  constructor(public direction: Direction, public payload: string) {}
}
