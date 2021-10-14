import { createRouter, createWebHistory } from 'vue-router';
import view1 from '/src/views/view1';
import view2 from '/src/views/view2';


const routes = [
  { path: 'view1', name: 'view1', component: view1 },
  { path: 'view2', name: 'view2', component: view2 },
];

const router = createRouter({
history: createWebHistory(process.env.BASE_URL),
routes
});

export default router;
