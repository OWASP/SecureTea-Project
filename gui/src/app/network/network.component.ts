import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-network',
  templateUrl: './network.component.html',
  styleUrls: ['./network.component.css']
})
export class NetworkComponent implements OnInit {

  apiRoot = '';
  interval;
  network = [];

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.getNetwork();
    this.interval = setInterval(() => {
      this.getNetwork();
    }, 3000);
  }

  getNetwork() {
    const posturl = `${this.apiRoot}netio`;
    this.http.post(posturl,{ "username":localStorage.getItem('user_name')}).subscribe((res) => {
      if (res.status === 200) {
        this.network = res.json()['data'];
        console.log(this.network);
      }
    });
  }
}
