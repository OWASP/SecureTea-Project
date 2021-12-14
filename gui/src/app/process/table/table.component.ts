import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router} from '@angular/router';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'app-table',
  templateUrl: './table.component.html',
  styleUrls: ['./table.component.css']
})

export class TableComponent implements OnInit {
    apiRoot = '';
    searchText: string;
    interval;
    reload = true;
    private sorted = false;
    tableData :any;

    constructor(
        private http: HttpClient, 
        private router: Router,
        private cookie: CookieService
    ) { }

    toggleVisibility(e) {
        this.reload = !this.reload;
    }
    ngOnInit() {
        this.apiRoot = this.cookie.get("api")
        console.log("Table api root" + this.apiRoot + "api root")
        if (this.apiRoot == "") {
          console.log("Table api root is null going to config")
          this.router.navigate(['/config']);
        }
        console.log("Table Api is" + this.cookie.get("api"))
        this.getProcess();
        this.interval = setInterval(() => {
            if (this.reload) {
                this.getProcess();
            }
        }, 3000);
    }

    getProcess() {
        const geturl = `${this.apiRoot}process`;
        this.http.get(geturl).subscribe((res) => {
        if (res["status"] === 200) {
            this.tableData = res;
            this.sortBy('cpu');
        } else {
            console.log('Status: ' + res);
        }
        }, (err) => {
            console.log(err);
        }
        );
    }

    search() {
        return this.tableData;
    }

    sortBy(by: string | any): void {
        this.tableData.sort((a: any, b: any) => {
          if (a[by] < b[by]) {
            return this.sorted ? 1 : -1;
          }
          if (a[by] > b[by]) {
            return this.sorted ? -1 : 1;
          }
          return 0;
        });
        this.sorted = !this.sorted;
    }
}
