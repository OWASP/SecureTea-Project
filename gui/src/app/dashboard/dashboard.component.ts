import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {

  ram = '0';
  cpu = '0';
  swap = '0';
  core = '0';
  bits = '0';
  brand = '_';
  ExRam: any;
  ExCpu: any;
  ExSwap: any;
  frequency = '0';
  l2_cache = '0';
  apiRoot: any;
  interval;
  uptime = '__ : __ : __';

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cookie: CookieService
  ) { }

  ngOnInit() {
    this.apiRoot = this.cookie.get("api")
    console.log("api root" + this.apiRoot + "api root")
    if (this.apiRoot == "") {
      console.log("api root is null going to config")
      this.router.navigate(['/config']);
    }
    console.log("Api isssss" + this.cookie.get("api"))
    this.getCpu();
    this.getRam();
    this.getSwap();
    this.getUptime();
    this.interval = setInterval(() => {
      this.getCpu();
      this.getRam();
      this.getSwap();
      this.getUptime();
    }, 5000);
  }

  getRam() {
    const posturl = `${this.apiRoot}/ram`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.ram = res["percent"];
        this.ExRam = JSON.parse(JSON.stringify(res));
        console.log(res)
      } else {
        this.ram = '0';
      }
    }, (err) => {
        this.ram = '0';
      }
    );
  }

  getCpu() {
    const posturl = `${this.apiRoot}/cpu`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.cpu = res["percentage"];
        this.ExCpu = JSON.parse(JSON.stringify(res));
        console.log(res)
      } else {
        this.cpu = '0';
      }
    }, (err) => {
        this.cpu = '0';
      }
    );
  }

  getSwap() {
    const posturl = `${this.apiRoot}/swap`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.swap = res["percent"];
        this.ExSwap = JSON.parse(JSON.stringify(res));
        console.log(res)
      } else {
        this.swap = '0';
      }
    }, (err) => {
        this.swap = '0';
      }
    );
  }

  getUptime() {
    const posturl = `${this.apiRoot}/uptime`;
    this.http.post(
      posturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.uptime = res["uptime"];
        console.log(JSON.parse(JSON.stringify(res)))
      } else {
        this.uptime = '__ : __ : __';
      }
    }, (err) => {
        this.uptime = '__ : __ : __';
      }
    );
  }
}
