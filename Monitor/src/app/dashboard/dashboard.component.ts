import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

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

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
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
    const geturl = `${this.apiRoot}ram`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.ram = res.json().percent;
        this.ExRam = res.json();
      } else {
        this.ram = '0';
      }
    }, (err) => {
        this.ram = '0';
      }
    );
  }

  getCpu() {
    const geturl = `${this.apiRoot}cpu`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.cpu = res.json().percentage;
        this.ExCpu = res.json();
      } else {
        this.cpu = '0';
      }
    }, (err) => {
        this.cpu = '0';
      }
    );
  }

  getSwap() {
    const geturl = `${this.apiRoot}swap`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.swap = res.json().percent;
        this.ExSwap = res.json();
      } else {
        this.swap = '0';
      }
    }, (err) => {
        this.swap = '0';
      }
    );
  }

  getUptime() {
    const geturl = `${this.apiRoot}uptime`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.uptime = res.json().uptime;
      } else {
        this.uptime = '__ : __ : __';
      }
    }, (err) => {
        this.uptime = '__ : __ : __';
      }
    );
  }
}
