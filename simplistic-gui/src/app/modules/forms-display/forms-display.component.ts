import { Component, Input, OnInit, TestabilityRegistry } from '@angular/core';
import { Form, FormBuilder, FormControl, FormGroup, FormsModule, Validators } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/common-resources/api.service';
import { SharedService } from 'src/app/common-resources/shared.service';
import { ApiRequestService } from './api-request.service';

@Component({
  selector: 'app-forms-display',
  templateUrl: './forms-display.component.html',
  styleUrls: ['./forms-display.component.css']
})
export class FormsDisplayComponent implements OnInit {

  constructor(
    private route: ActivatedRoute, 
    private service:ApiRequestService,
    private shared:SharedService,
    private api:ApiService
  ) { }

  @Input() module_meta: any = "";
  params_length: number;  
  input_form: FormGroup;
  flag: boolean = false
  test: any;
  display_data: any;
  cmd_list: any[] = [];
  loaded_module: string

  args_html_list: [number, string][] = [
    [0, "arg0"],
    [1, "arg1"],
    [2, "arg2"],
    [3, "arg3"],
    [4, "arg4"],
    [5, "arg5"],
    [6, "arg6"],
    [7, "arg7"],
    [8, "arg8"],
    [9, "arg9"],
  ]

  ngOnInit(): void {

    this.params_length = this.module_meta[0].length

    this.input_form = new FormGroup({
      "arg0": new FormControl(0 < this.params_length ? this.module_meta[1][0] : null),
      "arg1": new FormControl(1 < this.params_length ? this.module_meta[1][1] : null),
      "arg2": new FormControl(2 < this.params_length ? this.module_meta[1][2] : null),
      "arg3": new FormControl(3 < this.params_length ? this.module_meta[1][3] : null),
      "arg4": new FormControl(4 < this.params_length ? this.module_meta[1][4] : null),
      "arg5": new FormControl(5 < this.params_length ? this.module_meta[1][5] : null),
      "arg6": new FormControl(6 < this.params_length ? this.module_meta[1][6] : null),
      "arg7": new FormControl(7 < this.params_length ? this.module_meta[1][7] : null),
      "arg8": new FormControl(8 < this.params_length ? this.module_meta[1][8] : null),
      "arg9": new FormControl(9 < this.params_length ? this.module_meta[1][9] : null),
    })
  }

  onSubmit() {
    this.cmd_list = []
    this.flag = true
    console.log(this.input_form.value);

    for (let index = 0; index < this.params_length; index++) {
      /*
      if (this.input_form.value[this.args_html_list[index][1]]) {
        this.cmd_list.push(this.input_form.value[this.args_html_list[index][1]])
      }
      */
      this.cmd_list.push(this.input_form.value[this.args_html_list[index][1]])

    }

    console.log(this.cmd_list)

    this.loaded_module = this.route.snapshot.params['modulename']
    this.api.run_cmd(this.loaded_module, this.cmd_list).subscribe(data=>{
      this.display_data = data
    })

    // this.test = this.api.run_cmd(this.input_form.value)

  }
}
