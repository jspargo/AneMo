import AppComponent from './components/app';
import IndexComponent from './components/index';
import ApiAppComponent from './components/ajax';

const routes = {
  path: '',
  component: AppComponent,
  childRoutes: [
    {
      path: '/',
      component: IndexComponent
    },
    {
      path: '/t',
      component: ApiAppComponent
    }
  ]
}

export { routes };