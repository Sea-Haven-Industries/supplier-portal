var h=(e,s,i)=>new Promise((n,r)=>{var t=p=>{try{l(i.next(p))}catch(g){r(g)}},c=p=>{try{l(i.throw(p))}catch(g){r(g)}},l=p=>p.done?n(p.value):Promise.resolve(p.value).then(t,c);l((i=i.apply(e,s)).next())});import{c as m,r as L,a as k,b as I,d as S,_ as y,e as E,f as P,g as C,o as R,h as T,s as b,i as w,j as $,C as U,I as j,k as O}from"./vendor.ea68c68e.js";const A=function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const r of document.querySelectorAll('link[rel="modulepreload"]'))n(r);new MutationObserver(r=>{for(const t of r)if(t.type==="childList")for(const c of t.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&n(c)}).observe(document,{childList:!0,subtree:!0});function i(r){const t={};return r.integrity&&(t.integrity=r.integrity),r.referrerpolicy&&(t.referrerPolicy=r.referrerpolicy),r.crossorigin==="use-credentials"?t.credentials="include":r.crossorigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function n(r){if(r.ep)return;r.ep=!0;const t=i(r);fetch(r.href,t)}};A();const x="modulepreload",v={},N="/assets/suppliers_portal/frontend/",d=function(s,i){return!i||i.length===0?s():Promise.all(i.map(n=>{if(n=`${N}${n}`,n in v)return;v[n]=!0;const r=n.endsWith(".css"),t=r?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${n}"]${t}`))return;const c=document.createElement("link");if(c.rel=r?"stylesheet":x,r||(c.as="script",c.crossOrigin=""),c.href=n,document.head.appendChild(c),r)return new Promise((l,p)=>{c.addEventListener("load",l),c.addEventListener("error",p)})})).then(()=>s())},_=m({url:"frappe.auth.get_logged_user",cache:"User",onError(e){e&&e.exc_type==="AuthenticationError"&&u.push({name:"LoginPage"})}});function f(){let s=new URLSearchParams(document.cookie.split("; ").join("&")).get("user_id");return s==="Guest"&&(s=null),s}function V(){return new URLSearchParams(document.cookie.split("; ").join("&")).get("supplier_id")}function D(){return new URLSearchParams(document.cookie.split("; ").join("&")).get("supplier_name")}const o=L({supplier_login:m({url:"suppliers_portal.suppliers_portal.api.validate_supplier_id",makeParams({supplier_id:e}){return{supplier_id:e}},onSuccess(e){e&&e.status==="success"&&(_.reload(),o.user=f(),document.cookie=`supplier_id=${e.supplier_id}`,document.cookie=`supplier_name=${e.supplier_name}`,o.supplier_id=e.supplier_id,o.supplier_name=e.supplier_name,o.login.reset(),u.replace({name:"SupplierInvoiceList"}))},onError(e){console.error("Login failed",e)}}),login:m({url:"login",makeParams({email:e,password:s}){return{usr:e,pwd:s}},onSuccess(e){e&&(_.reload(),o.user=f(),document.cookie=`supplier_id=${o.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,document.cookie=`supplier_id=${o.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,o.supplier_id="",o.supplier_name="",o.login.reset(),u.replace({name:"SupplierInvoiceList"}))},onError(e){console.error("Login failed",e)}}),logout:m({url:"logout",onSuccess(){document.cookie=`supplier_id=${o.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,document.cookie=`supplier_id=${o.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,o.supplier_id="",o.supplier_name="",_.reset(),o.user=f(),u.replace({name:"Login"})}}),user:f(),supplier_id:V(),supplier_name:D(),isLoggedIn:k(()=>!!o.user)}),J=[{name:"Login",path:"/account/login",component:()=>d(()=>import("./Login.cac288e8.js"),["assets/Login.cac288e8.js","assets/vendor.ea68c68e.js","assets/vendor.43acabc4.css"])},{name:"SupplierInvoiceList",path:"/",component:()=>d(()=>import("./SupplierInvoiceList.a65688cd.js"),["assets/SupplierInvoiceList.a65688cd.js","assets/SupplierInvoiceList.516f990a.css","assets/vendor.ea68c68e.js","assets/vendor.43acabc4.css"])},{name:"SupplierInvoice",path:"/invoices/:supplierInvoiceNumber",component:()=>d(()=>import("./SupplierInvoice.0af8ab9f.js"),["assets/SupplierInvoice.0af8ab9f.js","assets/SupplierInvoice.1ae7ac54.css","assets/vendor.ea68c68e.js","assets/vendor.43acabc4.css"]),props:!0},{name:"SupplierInvoiceCreate",path:"/invoices/new",component:()=>d(()=>import("./NewInvoice.77131025.js"),["assets/NewInvoice.77131025.js","assets/NewInvoice.6080e5af.css","assets/vendor.ea68c68e.js","assets/vendor.43acabc4.css"])}];let u=I({history:S("/supplier-portal"),routes:J});u.beforeEach((e,s,i)=>h(void 0,null,function*(){let n=o.isLoggedIn;try{yield _.promise}catch(r){n=!1}e.name==="Login"&&n?i({name:"SupplierInvoiceList"}):e.name!=="Login"&&!n?i({name:"Login"}):i()}));const q={};function B(e,s){const i=C("router-view");return R(),E("div",null,[P(i)])}var F=y(q,[["render",B]]);let a=T(F);b("resourceFetcher",O);a.use(u);a.use(w);a.component("Button",$);a.component("Card",U);a.component("Input",j);a.mount("#app");export{V as a,D as b,u as r,o as s};
