import { Component, Injectable, OnInit } from '@angular/core';
import { ApiService } from '../common-resources/api.service';
import { SharedService } from '../common-resources/shared.service';

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})

export class DashboardComponent implements OnInit {

  constructor(private api: ApiService, private shared:SharedService) {
    
  }

  meta: any
  
  ngOnInit(): void {
    this.meta = {}
    this.api.get_meta().subscribe(data=>{
      this.meta = data
    })

  }
}
