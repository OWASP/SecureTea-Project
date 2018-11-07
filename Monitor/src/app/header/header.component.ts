import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})

export class HeaderComponent implements OnInit {

  username = 'username';
  apiRoot =  '';

  constructor(private http: Http, private router: Router) {
  }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.getUsername();
  }

  getUsername() {
    const geturl = `${this.apiRoot}username`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.username = res.json().username;
      }
    });
  }
}
