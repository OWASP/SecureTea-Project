import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { HttpParams } from '@angular/common/http';
import { Router} from '@angular/router';

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
    private router: Router
  ) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.getStorage();
  }

  getStorage() {
    const geturl = `${this.apiRoot}hdd`;
    this.http.post(
      geturl,
      { 
        "username":localStorage.getItem('user_name')
      }
    ).subscribe((res) => {
      if (res === 200) {
        // this.storage = res.json()['data'];
        console.log(res)
      }
    });
  }
}
