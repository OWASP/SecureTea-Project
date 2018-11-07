import { Component, OnInit } from '@angular/core';
import { Http } from '@angular/http';
import { Router} from '@angular/router';

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
    tableData = [ ];

    constructor(private http: Http, private router: Router) { }

    toggleVisibility(e) {
        this.reload = !this.reload;
    }
    ngOnInit() {
        this.apiRoot = localStorage.getItem('endpoint');
        if (!this.apiRoot) {
            this.router.navigate(['/config']);
        }
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
        if (res.status === 200) {
            this.tableData = res.json()['data'];
            // this.sortBy('cpu');
        } else {
            console.log('Status: ' + res.status);
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
