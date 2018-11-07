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

const routes: Routes = [
  { path: 'dashboard', component: DashboardComponent },
  { path: 'config', component: ConfigurationComponent },
  { path: 'storage', component: StorageComponent },
  { path: 'processes', component: ProcessComponent },
  { path: 'network', component: NetworkComponent},
  { path: 'security', component: SecurityComponent},
  { path: 'logout', component: LogoutComponent },
  { path: 'error', component: ErrorComponent },
  { path: '', redirectTo: '/dashboard', pathMatch: 'full' },
  { path: '**', component: ErrorComponent },

];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
