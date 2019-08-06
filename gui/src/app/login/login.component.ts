import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  apiRoot = '';
  interval;
  login = [];

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.getLogin();
    this.interval = setInterval(() => {
      this.getLogin();
    }, 3000);
  }

  getLogin() {
    const geturl = `${this.apiRoot}login`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.login = res.json()['data'];
        console.log(this.login);
      }
    });
  }
}
