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
    /*
  	  const posturl = localStorage.getItem('endpoint').concat('userlogout');
      this.http.post(
        posturl,
        {
          'username':localStorage.getItem('user_name')
        }
      ).subscribe((res) => {
            if (res === 200) {
                    localStorage.removeItem('endpoint');
                    localStorage.removeItem('user_name');
                    this.router.navigate(['/config']);
            } else {
              console.log(res);
            }
          }, (err) => {
              console.log(err.status);
            }
          );
    */


    this.cookie.delete("username")
    this.router.navigate(['/config']);
  }
}
