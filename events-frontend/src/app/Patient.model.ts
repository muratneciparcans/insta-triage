export class PatientModel {
  public name: string;
  public start_date: Date;
  public end_date: Date;
  public action: string;
  public notified: string;
  public estimated_waiting: string;
  public heartrate: string;
  public pain: number;
  public patient_infos: string[];
  constructor() {}
}
