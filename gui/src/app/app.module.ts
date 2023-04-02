import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from "@angular/common/http"
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { AppRoutingModule } from './app-routing.module';

import { AppComponent } from './app.component';
import { LoadingComponent } from './loading/loading.component';
import { StorageComponent } from './storage/storage.component';
import { ErrorComponent } from './error/error.component';
import { BodyComponent } from './dashboard/body/body.component';
import { HeaderComponent } from './header/header.component';
import { FooterComponent } from './footer/footer.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { SidebarComponent } from './sidebar/sidebar.component';
import { ConfigurationComponent } from './configuration/configuration.component';
import { ProcessComponent } from './process/process.component';
import { TableComponent } from './process/table/table.component';
import { NetworkComponent } from './network/network.component';
import { SecurityComponent } from './security/security.component';
import { LogoutComponent } from './logout/logout.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { WAFComponent } from './waf/waf.component';

@NgModule({
  declarations: [
    AppComponent,
    ErrorComponent,
    StorageComponent,
    HeaderComponent,
    FooterComponent,
    SidebarComponent,
    LoadingComponent,
    DashboardComponent,
    BodyComponent,
    TableComponent,
    NetworkComponent,
    ProcessComponent,
    ConfigurationComponent,
    SecurityComponent,
    LogoutComponent,
    LoginComponent,
    RegisterComponent,
    WAFComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
