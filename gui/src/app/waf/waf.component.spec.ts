import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { WAFComponent } from './waf.component';

describe('LoginComponent', () => {
  let component: WAFComponent;
  let fixture: ComponentFixture<WAFComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ WAFComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(WAFComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
