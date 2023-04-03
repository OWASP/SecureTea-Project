import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-ids',
  templateUrl: './ids.component.html',
  styleUrls: ['./ids.component.css']
})
export class IDSComponent implements OnInit {

  apiRoot = '';
  interval;
  login = [];

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cookie: CookieService
  ) { }

  ngOnInit() {
    this.apiRoot = this.cookie.get("api")
    console.log(" Login api root" + this.apiRoot + "api root")
    if (this.apiRoot == "") {
      console.log("Login api root is null going to config")
      this.router.navigate(['/config']);
    }
    console.log("Login Api is" + this.cookie.get("api"))
    this.getIDSLogs();
    this.interval = setInterval(() => {
      this.getIDSLogs();
    }, 3000);
  }

  getIDSLogs() {
    const posturl = `${this.apiRoot}/ids`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.login = res['data'];
        console.log(res);
      }
    });
  }
}
