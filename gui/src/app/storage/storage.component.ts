import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpParams } from '@angular/common/http';
import { Router} from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-storage',
  templateUrl: './storage.component.html',
  styleUrls: ['./storage.component.css']
})
export class StorageComponent implements OnInit {

  apiRoot = '';
  storage = [];

  constructor(
    private http: HttpClient, 
    private router: Router,
    private cookie: CookieService
  ) { }

  ngOnInit() {
    this.apiRoot = this.cookie.get("api")
    console.log("Storage api root" + this.apiRoot + "api root")
    if (this.apiRoot == "") {
      console.log("Storage api root is null going to config")
      this.router.navigate(['/config']);
    }
    console.log("Storage Api is" + this.cookie.get("api"))
    this.getStorage();
  }

  getStorage() {
    const geturl = `${this.apiRoot}/hdd`;
    console.log(geturl)
    this.http.post(
      geturl,
      { 
        "username":this.cookie.get('user_name')
      }
    ).subscribe((res) => {
      if (res["status"] === 200) {
        this.storage = res['data'];
        console.log(res)
      }
    });
  }
}
