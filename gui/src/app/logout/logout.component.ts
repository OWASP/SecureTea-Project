import { Component, OnInit } from '@angular/core';
import { Router} from '@angular/router';
import { Http } from '@angular/http';
import { HttpParams } from '@angular/common/http';

@Component({
  selector: 'app-logout',
  templateUrl: './logout.component.html',
  styleUrls: ['./logout.component.css']
})

export class LogoutComponent implements OnInit {

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
  	  const posturl = localStorage.getItem('endpoint').concat('userlogout');
      this.http.post(posturl,{'username':localStorage.getItem('user_name')}).subscribe((res) => {
            if (res.status === 200) {
                    localStorage.removeItem('endpoint');
                    localStorage.removeItem('user_name');
                    this.router.navigate(['/config']);
            } else {
              console.log(res.status);
            }
          }, (err) => {
              console.log(err.status);
            }
          );

  }
}
