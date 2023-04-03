import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { ErrorComponent } from './error/error.component';
import { StorageComponent } from './storage/storage.component';
import { DashboardComponent } from './dashboard/dashboard.component';
import { ConfigurationComponent } from './configuration/configuration.component';
import { ProcessComponent } from './process/process.component';
import { NetworkComponent } from './network/network.component';
import { SecurityComponent } from './security/security.component';
import { LogoutComponent } from './logout/logout.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';
import { IDSComponent } from './ids/ids.component';
import { WAFComponent } from './waf/waf.component';

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'config', component: ConfigurationComponent },
  { path: 'storage', component: StorageComponent },
  { path: 'processes', component: ProcessComponent },
  { path: 'network', component: NetworkComponent},
  { path: 'login', component: LoginComponent},
  { path: 'security', component: SecurityComponent},
  { path: 'logout', component: LogoutComponent },
  { path: 'error', component: ErrorComponent },
  { path: 'waf', component: WAFComponent},
  { path: 'ids', component: IDSComponent},
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: '**', component: ErrorComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
