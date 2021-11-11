import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  readonly api_url = "http://127.0.0.1:8000/"

  constructor(private http: HttpClient) { }

  get_meta() {
    return this.http.get(this.api_url + "meta")
  }

  get_module_meta(modulename: string) {
    return this.http.get(this.api_url + "module_meta/?module=" + modulename)
  }

  run_cmd(modulename:string, cmd_list: any[]) {
    return this.http.get(this.api_url + "cmd/?modulename=" + modulename +"&cmd_list=" + cmd_list)
  }



}
