import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../common-resources/api.service';

@Component({
  selector: 'app-modules',
  templateUrl: './modules.component.html',
  styleUrls: ['./modules.component.css']
})
export class ModulesComponent implements OnInit {

  constructor(
    private route: ActivatedRoute,
    private api: ApiService
  ) { }

  meta: any
  loaded_module: string = '';
  keys: string[] = [''];
  module_meta: any;
  
  ngOnInit(): void {
    this.api.get_meta().subscribe(data=>{
      this.meta = data
    })

    this.loaded_module = this.route.snapshot.params['modulename']
    this.api.get_module_meta(this.loaded_module).subscribe(data=>{
      this.module_meta = data
    })

  }

}
