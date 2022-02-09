import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css']
})
export class NetworkComponent implements OnInit {

  apiRoot = '';
  interval;
  network = [];

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cookie: CookieService
  ) { }

  ngOnInit() {
    this.apiRoot = this.cookie.get("api")
    console.log(" Network api root" + this.apiRoot + "api root")
    if (this.apiRoot == "") {
      console.log("Network api root is null going to config")
      this.router.navigate(['/config']);
    }
    console.log("Network Api is" + this.cookie.get("api"))
    this.getNetwork();
    this.interval = setInterval(() => {
      this.getNetwork();
    }, 3000);
  }

  getNetwork() {
    const posturl = `${this.apiRoot}netio`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.network = res['data'];
        // console.log(res);
      }
    });
  }
}
