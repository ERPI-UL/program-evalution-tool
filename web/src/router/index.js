import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from "@/stores/UserStore";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import('@/views/Home.vue'),
  },
  {
    path: "/login",
    name: "LogIn",
    props: true,
    component: () => import('@/views/LogIn.vue'),
  },
  {
    path: "/register",
    name: "Register",
    component: () => import('@/views/SignIn.vue'),
  },
  {
    path: "/recovery",
    name: "Account-Recovery",
    props: true,
    component: () => import('@/views/Recovery.vue'),
  },
  {
    path: "/programs",
    name: "Programs",
    meta: { showAddProgBtn: true, requiresAuth: true, },
    component: () => import('@/views/program/Program-List.vue'),
  },
  {
    path: "/program/:progid/detail",
    name: "ProgramDetail",
    props: true,
    component: () => import('@/views/program/Program-Detail.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/program/",
    name: "Program-Form",
    meta: { requiresAuth: true, },
    component: () => import('@/views/program/Program-Form.vue'),
  },
  {
    path: "/indicator/:indid",
    name: "Indicator-Detail",
    props: true,
    component: () => import('@/views/indicator/Indicator-Detail.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/indicator/add",
    name: "Indicator-Add",
    component: () => import('@/views/indicator/Indicator-Form.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/indicators/all",
    name: "Indicators",
    meta: { showAddIndBtn: true, requiresAuth: true, },
    component: () => import('@/views/indicator/Indicator-List.vue'),
  },
  {
    path: "/evaluations/all",
    name: "Evaluations",
    component: () => import('@/views/evaluation/Evaluation-List.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/evaluation/:evalid/",
    name: "Evaluation-Form",
    component: () => import('@/views/evaluation/Evaluation-Form.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/dashboard/all",
    name: "Dashboards",
    component: () => import('@/views/dashboard/Dashboard-List.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/dashboard/all2",
    name: "Dashboard-Detail",
    
    component: () => import('@/views/dashboard/Dashboard-Detail.vue'),
    meta: {
      showTabs: true,
      requiresAuth: true,
    },
  },
  {
    path: "/project/:projid/dasboard",
    name: "Project-Dashboard",
    props: true,
    component: () => import('@/views/dashboard/Dashboard-Detail2.vue'),
    meta: {
      showTabs: true,
      requiresAuth: true,
    },
  },
  {
    path: "/project/:projid/evaluation",
    name: "Project-Evalution-Form",
    props: true,
    component: () => import('@/views/evaluation/Evaluation-Form2.vue'),
    meta: {
      showTabs: true,
      requiresAuth: true,
    },
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  }, {
    path: '/:catchAll(.*)',
    component: () => import('@/components/404.vue'),
    hidden: true
  }
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach(async (to, from, next) => {
  const userStore = useUserStore();
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    await userStore.checkUser()
    if (userStore.isLogged) {
      console.log("Logged, go to page");
      next();
      return;
    } else {
      console.log("not logged redirected to login page");
      next({ name: 'LogIn' });
      return;
    }
  } else {
    next();
  }
});

export default router;
