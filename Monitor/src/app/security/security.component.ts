import { Component, OnInit } from '@angular/core';
import { FormGroup, FormControl } from '@angular/forms';
import { Http } from '@angular/http';
import { Router} from '@angular/router';
import $ from 'jquery';
import swal from 'sweetalert';

@Component({
  selector: 'app-security',
  templateUrl: './security.component.html',
  styleUrls: ['./security.component.css']
})
export class SecurityComponent implements OnInit {

  apiRoot = '';
  error: String;
  status = '';
  twitterForm = new FormGroup({
    apikey: new FormControl(''),
    apiSecret: new FormControl(''),
    token: new FormControl(''),
    tokenSecret: new FormControl('')
  });

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.checkStatus();
  }
  Submit() {
    const posturl = `${this.apiRoot}sleep`;
    if (this.twitterForm.valid) {
      this.error = '';
      const data = {
        'api_key': this.twitterForm.value.apikey,
        'api_secret_key': this.twitterForm.value.apiSecret,
        'access_token': this.twitterForm.value.token,
        'access_token_secret': this.twitterForm.value.tokenSecret
      };
      swal({
        title: 'Are you sure?',
        text: 'This will monitor your system with new configuration.',
        icon: 'warning',
        buttons: ['No', 'Yes'],
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.http.post(posturl, data).subscribe((res) => {
            if (res.status === 201) {
              this.twitterForm.reset();
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
            } else if (res.status === 200) {
              $('#startForm').hide();
              $('#stopForm').show();
              swal('Already monitoring', {
                icon: 'success',
              });
              this.error = '';
            }
          }, (err) => {
            this.error = 'Something went wrong';
          });
        }
      });
    } else {
      swal({
        title: 'Are you sure?',
        text: 'This will monitor your system with existsting configuration.',
        icon: 'warning',
        buttons: ['No', 'Yes'],
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          this.http.get(posturl).subscribe((res) => {
            if (res.status === 201) {
              this.twitterForm.reset();
              $('#startForm').hide();
              $('#stopForm').show();
              this.error = '';
              swal('Great! Your system is going to sleep in 5s.', {
                icon: 'success',
              });
            } else if (res.status === 200) {
              $('#startForm').hide();
              $('#stopForm').show();
              swal('Already monitoring', {
                icon: 'success',
              });
              this.error = '';
            }
          }, (err) => {
            this.error = 'Something went wrong';
          });
        }
      });
    }
  }

  Stop() {
    const posturl = `${this.apiRoot}stop`;
    this.http.get(posturl).subscribe((res) => {
      if (res.status === 200) {
        $('#stopForm').hide();
        $('#startForm').show();
        this.error = '';
      }
    }, (err) => {
      console.log(err);
    });
  }

  checkStatus() {
    const geturl = `${this.apiRoot}status`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        $('#startForm').hide();
        $('#stopForm').show();
        this.error = '';
      } else if (res.status === 204) {
        $('#startForm').show();
        $('#stopForm').hide();
        this.error = '';
      }
    }, (err) => {
      $('#startForm').show();
      $('#stopForm').hide();
      this.error = '';
    });
  }
}
