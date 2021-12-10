import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';
import * as toastr from 'toastr';
import * as io from 'socket.io-client';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})

export class HeaderComponent implements OnInit {

  username = localStorage.getItem('user_name');
  apiRoot =  '';
  socket: any;


  constructor(
    private http: HttpClient, 
    private router: Router
  ) {}

  ngOnInit() {
    /*
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    toastr.options ={
      "progressBar": true
    }
    this.socket = io(this.apiRoot);
    this.socket.on('newmessage', (msg) => {
      if(msg.message.charAt(0) === "W")
      {
        toastr.warning(msg.message.substring(1));
      }
      else if(msg.message.charAt(0) === "S")
      {
        toastr.success(msg.message.substring(1));
      }
      else
      {
        toastr.error(msg.message.substring(1));
      }
    });
    this.getUsername();
    */
  }

  getUsername() {
    const geturl = `${this.apiRoot}username`;
    this.http.get(geturl).subscribe((res) => {
      if (res === 200) {
        // res.json().username;
      }
    });
  }
}
