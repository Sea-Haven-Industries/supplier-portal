import{_ as d,j as g,U as m,V as L,e as f,Q as p,R as D,S as c,f as i,w as l,F as h,g as a,o as _,W as v,v as w}from"./vendor.ea68c68e.js";const V={name:"InsertLink",props:["editor"],components:{Button:g,FormControl:m,Dialog:L},data(){return{setLinkDialog:{url:"",show:!1}}},methods:{openDialog(){let t=this.editor.getAttributes("link").href;t&&(this.setLinkDialog.url=t),this.setLinkDialog.show=!0},setLink(t){t===""?this.editor.chain().focus().extendMarkRange("link").unsetLink().run():this.editor.chain().focus().extendMarkRange("link").setLink({href:t}).run(),this.setLinkDialog.show=!1,this.setLinkDialog.url=""},reset(){this.setLinkDialog=this.$options.data().setLinkDialog}}},x=w(" Save ");function C(t,e,R,B,n,s){const r=a("FormControl"),u=a("Button"),k=a("Dialog");return _(),f(h,null,[p(t.$slots,"default",D(c({onClick:s.openDialog}))),i(k,{options:{title:"Set Link"},modelValue:n.setLinkDialog.show,"onUpdate:modelValue":e[3]||(e[3]=o=>n.setLinkDialog.show=o),onAfterLeave:s.reset},{"body-content":l(()=>[i(r,{type:"text",label:"URL",modelValue:n.setLinkDialog.url,"onUpdate:modelValue":e[0]||(e[0]=o=>n.setLinkDialog.url=o),onKeydown:e[1]||(e[1]=v(o=>s.setLink(o.target.value),["enter"]))},null,8,["modelValue"])]),actions:l(()=>[i(u,{variant:"solid",onClick:e[2]||(e[2]=o=>s.setLink(n.setLinkDialog.url))},{default:l(()=>[x]),_:1})]),_:1},8,["modelValue","onAfterLeave"])],64)}var U=d(V,[["render",C]]);export{U as default};
