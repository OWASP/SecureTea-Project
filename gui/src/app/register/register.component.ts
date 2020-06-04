import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Http } from '@angular/http';
import { Router} from '@angular/router';


@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent implements OnInit {

  myform: FormGroup;
  endpoint: FormControl;
  uname: FormControl;
  pass: FormControl;
  cpass: FormControl;
  sec: FormControl;
  error: String;


  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.endpoint = new FormControl('');
    this.uname = new FormControl('');
    this.pass = new FormControl('');
    this.cpass = new FormControl('');
    this.sec = new FormControl('');
    this.myform = new FormGroup({
      endpoint: this.endpoint,
      uname: this.uname,
      pass: this.pass,
      cpass: this.cpass,
      sec: this.sec
    });
  }
  Submit() {
  var end_point_login=this.endpoint.value.concat('/register').replace("//register","/register");
  if (this.endpoint.valid) {
    this.http.get(this.endpoint.value).subscribe((res) => {
      if (res.status === 200) {
        this.error = 'End point is working';
        if(this.pass.value===this.cpass.value && this.pass.value!='') {
          this.http.post(end_point_login,{'username':this.uname.value,'password':this.pass.value,'ns':this.sec.value}).subscribe((res) => {
            if (res.status === 200) {
              this.router.navigate(['/config']);
            } else {
              console.log(res.status);
              this.error = 'Wrong Credentials';
            }
          }, (err) => {
              console.log(err.status);
              this.error = 'Login Error';
            }
          );
          }
          else
          {
            this.error = "Password cannot be empty";
          }
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

}
