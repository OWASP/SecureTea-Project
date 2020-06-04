import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-configuration',
  templateUrl: './configuration.component.html',
  styleUrls: ['./configuration.component.css']
})
export class ConfigurationComponent implements OnInit {

  myform: FormGroup;
  endpoint: FormControl;
  uname: FormControl;
  pass: FormControl;
  sec: FormControl;
  error: String;

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    var apiRoot = localStorage.getItem('endpoint');
    var uname = localStorage.getItem('user_name');
    if(uname && apiRoot)
    {
      this.router.navigate(['/dashboard']);
    }
    else
    {
      this.endpoint = new FormControl('');
      this.uname = new FormControl('');
      this.pass = new FormControl('');
      this.sec = new FormControl('');
      this.myform = new FormGroup({
        endpoint: this.endpoint,
        uname: this.uname,
        pass: this.pass,
        sec: this.sec
      });
    }
  }

  Submit() {
    var end_point_login=this.endpoint.value.concat('/userlogin').replace("//userlogin","/userlogin");
    console.log(end_point_login)
    if (this.endpoint.valid) {
      this.http.get(this.endpoint.value).subscribe((res) => {
        if (res.status === 200) {
          this.error = 'End point is working';
          var orig_url=res.url;
          this.http.post(end_point_login,{'username':this.uname.value,'password':this.pass.value,'ns':this.sec.value}).subscribe((res) => {
            if (res.status === 200) {
              localStorage.setItem('endpoint', orig_url);
              localStorage.setItem('user_name', this.uname.value);
              this.router.navigate(['/dashboard']);
            } else {
              console.log(res.status);
              this.error = 'Wrong Credentials';
            }
          }, (err) => {
              console.log(err.status);
              this.error = 'Login Error';
            }
          );
        } else {
          this.error = 'End point is not working';
        }
      }, (err) => {
          this.error = 'End point is not working';
        }
      );

    } else {
      this.error = 'End point is not valid';
    }
  }
  Register() {
    this.router.navigate(['/register']);
  }
}
