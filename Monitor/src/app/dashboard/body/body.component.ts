import { Component, OnInit, Input } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

@Component({
  selector: 'app-body',
  templateUrl: './body.component.html',
  styleUrls: ['./body.component.css']
})
export class BodyComponent implements OnInit {

  @Input() ram: any;
  @Input() cpu: any;
  @Input() swap: any;

  interval;
  apiRoot = '';

  brand = '_';
  vendor_id = '_';
  bits = '_';
  count = '_';
  hz_advertised = '_';
  l1_data_cache_size = '_';
  l1_instruction_cache_size = '_';
  l2_cache_size = '_';
  l3_cache_size = '_';

  ram_total = '0';
  ram_free = '0';
  ram_used = '0';
  ram_percentage = '0';
  ram_width: string;

  swap_total = '0';
  swap_free = '0';
  swap_used = '0';
  swap_percentage = '0';
  swap_width: string;

  read = 0;
  write = 0;

  constructor(private http: Http,  private router: Router) { }

  ngOnInit() {
    this.apiRoot = localStorage.getItem('endpoint');
    if (!this.apiRoot) {
      this.router.navigate(['/config']);
    }
    this.getRam();
    this.getSwap();
    this.getNetworkSpeed();
    this.getProcessor();
    this.interval = setInterval(() => {
      this.getRam();
      this.getSwap();
      this.getNetworkSpeed();
    }, 1000);
  }

  getProcessor() {
    const geturl = `${this.apiRoot}processor`;
    this.http.get(geturl).subscribe((res) => {
      if (res.status === 200) {
        this.brand = res.json().brand;
        this.vendor_id = res.json().vendor_id;
        this.bits = res.json().bits;
        this.count = res.json().count;
        this.hz_advertised = res.json().hz_advertised;
        this.l1_data_cache_size = res.json().l1_data_cache_size;
        this.l1_instruction_cache_size = res.json().l1_instruction_cache_size;
        this.l2_cache_size = res.json().l2_cache_size;
        this.l3_cache_size = res.json().l3_cache_size;
      }
    }, (err) => {
        console.log(err);
      }
    );
  }

  getRam() {
    try {
      this.ram_total = this.ram.total;
      this.ram_free = this.ram.free;
      this.ram_used = this.ram.used;
      this.ram_percentage = this.ram.percent;
      this.ram_width = this.ram_percentage + '%';
    } catch (error) {
      console.log(error);
    }
  }
  getSwap() {
    try {
      this.swap_total = this.swap.total;
      this.swap_free = this.swap.free;
      this.swap_used = this.swap.used;
      this.swap_percentage = this.swap.percent;
      this.swap_width = this.swap_percentage + '%';
    } catch (error) {
      console.log(error);
    }
  }

  getNetworkSpeed() {
    try {
      const geturl = `${this.apiRoot}diskio`;
      this.http.get(geturl).subscribe((res) => {
        if (res.status === 200) {
          this.read = res.json().read;
          this.write = res.json().write;
        }
      }, (err) => {
          console.log(err);
        }
      );
    } catch (error) {
      console.log(error);
    }
  }
  // pro() {
  //   $('mydiv').append();
  // }
}
