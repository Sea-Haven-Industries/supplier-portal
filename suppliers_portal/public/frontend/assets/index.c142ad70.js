var h=(e,s,i)=>new Promise((n,r)=>{var t=u=>{try{l(i.next(u))}catch(g){r(g)}},c=u=>{try{l(i.throw(u))}catch(g){r(g)}},l=u=>u.done?n(u.value):Promise.resolve(u.value).then(t,c);l((i=i.apply(e,s)).next())});import{c as m,r as L,a as k,b as I,d as S,_ as y,e as E,f as P,g as b,o as C,h as R,s as T,i as w,j as $,C as U,I as j,k as O}from"./vendor.3e69a9be.js";const A=function(){const s=document.createElement("link").relList;if(s&&s.supports&&s.supports("modulepreload"))return;for(const r of document.querySelectorAll('link[rel="modulepreload"]'))n(r);new MutationObserver(r=>{for(const t of r)if(t.type==="childList")for(const c of t.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&n(c)}).observe(document,{childList:!0,subtree:!0});function i(r){const t={};return r.integrity&&(t.integrity=r.integrity),r.referrerpolicy&&(t.referrerPolicy=r.referrerpolicy),r.crossorigin==="use-credentials"?t.credentials="include":r.crossorigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function n(r){if(r.ep)return;r.ep=!0;const t=i(r);fetch(r.href,t)}};A();const x="modulepreload",v={},N="/assets/suppliers_portal/frontend/",d=function(s,i){return!i||i.length===0?s():Promise.all(i.map(n=>{if(n=`${N}${n}`,n in v)return;v[n]=!0;const r=n.endsWith(".css"),t=r?'[rel="stylesheet"]':"";if(document.querySelector(`link[href="${n}"]${t}`))return;const c=document.createElement("link");if(c.rel=r?"stylesheet":x,r||(c.as="script",c.crossOrigin=""),c.href=n,document.head.appendChild(c),r)return new Promise((l,u)=>{c.addEventListener("load",l),c.addEventListener("error",u)})})).then(()=>s())},_=m({url:"frappe.auth.get_logged_user",cache:"User",onError(e){e&&e.exc_type==="AuthenticationError"&&p.push({name:"LoginPage"})}});function f(){let s=new URLSearchParams(document.cookie.split("; ").join("&")).get("user_id");return s==="Guest"&&(s=null),s}function V(){return new URLSearchParams(document.cookie.split("; ").join("&")).get("supplier_id")}function D(){return new URLSearchParams(document.cookie.split("; ").join("&")).get("supplier_name")}const o=L({supplier_login:m({url:"suppliers_portal.suppliers_portal.api.validate_supplier_id",makeParams({supplier_id:e}){return{supplier_id:e}},onSuccess(e){e&&e.status==="success"&&(_.reload(),o.user=f(),document.cookie=`supplier_id=${e.supplier_id}`,document.cookie=`supplier_name=${e.supplier_name}`,o.supplier_id=e.supplier_id,o.supplier_name=e.supplier_name,o.login.reset(),p.replace({name:"SupplierInvoiceList"}))},onError(e){console.error("Login failed",e)}}),login:m({url:"login",makeParams({email:e,password:s}){return{usr:e,pwd:s}},onSuccess(e){e&&(_.reload(),o.user=f(),document.cookie=`supplier_id=${o.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,document.cookie=`supplier_id=${o.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,o.supplier_id="",o.supplier_name="",o.login.reset(),p.replace({name:"SupplierInvoiceList"}))},onError(e){console.error("Login failed",e)}}),logout:m({url:"logout",onSuccess(){document.cookie=`supplier_id=${o.supplier_id}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,document.cookie=`supplier_id=${o.supplier_name}; expires=Thu, 01 Jan 1970 00:00:00 UTC'`,o.supplier_id="",o.supplier_name="",_.reset(),o.user=f(),p.replace({name:"Login"})}}),user:f(),supplier_id:V(),supplier_name:D(),isLoggedIn:k(()=>!!o.user)}),J=[{name:"Login",path:"/login",component:()=>d(()=>import("./Login.80913e45.js"),["assets/Login.80913e45.js","assets/vendor.3e69a9be.js","assets/vendor.43acabc4.css"])},{name:"SupplierInvoiceList",path:"/",component:()=>d(()=>import("./SupplierInvoiceList.55bab896.js"),["assets/SupplierInvoiceList.55bab896.js","assets/SupplierInvoiceList.e8de1e21.css","assets/vendor.3e69a9be.js","assets/vendor.43acabc4.css"])},{name:"SupplierInvoice",path:"/invoices/:supplierInvoiceNumber",component:()=>d(()=>import("./SupplierInvoice.beb0f4cf.js"),["assets/SupplierInvoice.beb0f4cf.js","assets/SupplierInvoice.9dfb3ca8.css","assets/vendor.3e69a9be.js","assets/vendor.43acabc4.css"]),props:!0},{name:"SupplierInvoiceCreate",path:"/invoices/new",component:()=>d(()=>import("./NewInvoice.1228f5fc.js"),["assets/NewInvoice.1228f5fc.js","assets/NewInvoice.67c196f0.css","assets/vendor.3e69a9be.js","assets/vendor.43acabc4.css"])}];let p=I({history:S("/frontend"),routes:J});p.beforeEach((e,s,i)=>h(void 0,null,function*(){let n=o.isLoggedIn;try{yield _.promise}catch(r){n=!1}e.name==="Login"&&n?i({name:"SupplierInvoiceList"}):e.name!=="Login"&&!n?i({name:"Login"}):i()}));const q={};function B(e,s){const i=b("router-view");return C(),E("div",null,[P(i)])}var F=y(q,[["render",B]]);let a=R(F);T("resourceFetcher",O);a.use(p);a.use(w);a.component("Button",$);a.component("Card",U);a.component("Input",j);a.mount("#app");export{f as a,V as b,D as c,p as r,o as s};