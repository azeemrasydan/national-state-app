import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { RootComponent } from './pages/root/root.component';

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
    }
];
