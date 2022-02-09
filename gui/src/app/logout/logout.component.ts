import { Component, OnInit } from '@angular/core';
import { Router} from '@angular/router';
import { HttpClient } from '@angular/common/http';
import { HttpParams } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})

export class LogoutComponent implements OnInit {

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cookie: CookieService
  ) { }

  ngOnInit() {
    this.cookie.deleteAll()
    // sessionStorage.clear();
    // localStorage.clear();

    this.router.navigate(['/dashboard']);
  }
}
