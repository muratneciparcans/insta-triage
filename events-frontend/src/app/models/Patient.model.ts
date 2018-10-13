export class PatientModel {
  public name: string = undefined;
  public start_date: Date = undefined;
  public end_date: Date = undefined;
  public action: string = undefined;
  public notified: string = undefined;
  public estimated_waiting: string = undefined;
  public heartrate: string = undefined;
  public pain: number = undefined;
  public patient_infos: string[];
  public born: Date = undefined;
  constructor() {}
}
