import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { IDSComponent } from './ids.component';

describe('LoginComponent', () => {
  let component: IDSComponent;
  let fixture: ComponentFixture<IDSComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ IDSComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(IDSComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
