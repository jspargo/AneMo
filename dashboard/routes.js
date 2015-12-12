import AppComponent from './components/app';
import IndexComponent from './components/index';

const routes = {
  path: '',
  component: AppComponent,
  childRoutes: [
    {
      path: '/',
      component: IndexComponent
    }
  ]
}

export { routes };