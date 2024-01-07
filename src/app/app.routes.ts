import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RootComponent } from './pages/root/root.component';
import { FloodWarningComponent } from './pages/flood/warning/flood.warning.component';

export const routes: Routes = [
    {
        title: 'Welcome',
        path: '',
        component: RootComponent
    },
    {
        title: "Home",
        path: 'home',
        component: HomeComponent
    },
    {
        title: "Flood Warning",
        path: 'flood/warning',
        component: FloodWarningComponent
    }
];
