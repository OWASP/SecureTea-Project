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
  error: String;

  constructor(private http: Http, private router: Router) { }

  ngOnInit() {
    this.endpoint = new FormControl('');
    this.myform = new FormGroup({
      endpoint: this.endpoint
    });
  }

  Submit() {
    if (this.myform.valid) {
      this.http.get(this.endpoint.value).subscribe((res) => {
        if (res.status === 200) {
          this.error = 'End point is not working';
          localStorage.setItem('endpoint', res.url);
          this.router.navigate(['/dashboard']);
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
