
import App from '../App'

export default [{
  path: '/',
  component: App,
  children: [{
    path: '/',
    component: r => require.ensure([], () => r(require('@/components/Index')), 'index')
  }, {
    path: '/advancedsearch',
    component: r => require.ensure([], () => r(require('@/components/AdvancedSearch')), 'advancedsearch')
  },{
    path: '/search',
    component: r => require.ensure([], () => r(require('@/components/SearchPage')), 'search')
  }, {
    path: '/profile',
    component: r => require.ensure([], () => r(require('@/components/Profile')), 'profile')
  }
  ]
}]
