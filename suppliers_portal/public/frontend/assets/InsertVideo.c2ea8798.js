import{_ as D,j as v,Y as h,a0 as C,e as u,T as k,U as w,V as x,f as t,w as i,F as B,g as r,o as c,m as U,v as n,t as y,N as F,p}from"./vendor.3e69a9be.js";const N={name:"InsertImage",props:["editor"],expose:["openDialog"],data(){return{addVideoDialog:{url:"",file:null,show:!1}}},components:{Button:v,Dialog:h,FileUploader:C},methods:{openDialog(){this.addVideoDialog.show=!0},onVideoSelect(l){let o=l.target.files[0];!o||(this.addVideoDialog.file=o)},addVideo(l){this.editor.chain().focus().insertContent(`<video src="${l}"></video>`).run(),this.reset()},reset(){this.addVideoDialog=this.$options.data().addVideoDialog}}},I={class:"flex items-center space-x-2"},S=n(" Remove "),A=["src"],b=n(" Insert Video "),j=n("Cancel");function L(l,o,P,R,e,a){const s=r("Button"),V=r("FileUploader"),g=r("Dialog");return c(),u(B,null,[k(l.$slots,"default",w(x({onClick:a.openDialog}))),t(g,{options:{title:"Add Video"},modelValue:e.addVideoDialog.show,"onUpdate:modelValue":o[2]||(o[2]=d=>e.addVideoDialog.show=d),onAfterLeave:a.reset},{"body-content":i(()=>[t(V,{"file-types":"video/*",onSuccess:o[0]||(o[0]=d=>e.addVideoDialog.url=d.file_url)},{default:i(({file:d,progress:f,uploading:_,openFileSelector:m})=>[U("div",I,[t(s,{onClick:m},{default:i(()=>[n(y(_?`Uploading ${f}%`:e.addVideoDialog.url?"Change Video":"Upload Video"),1)]),_:2},1032,["onClick"]),e.addVideoDialog.url?(c(),F(s,{key:0,onClick:()=>{e.addVideoDialog.url=null,e.addVideoDialog.file=null}},{default:i(()=>[S]),_:2},1032,["onClick"])):p("",!0)])]),_:1}),e.addVideoDialog.url?(c(),u("video",{key:0,src:e.addVideoDialog.url,class:"mt-2 w-full rounded-lg",type:"video/mp4",controls:""},null,8,A)):p("",!0)]),actions:i(()=>[t(s,{variant:"solid",onClick:o[1]||(o[1]=d=>a.addVideo(e.addVideoDialog.url))},{default:i(()=>[b]),_:1}),t(s,{onClick:a.reset},{default:i(()=>[j]),_:1},8,["onClick"])]),_:1},8,["modelValue","onAfterLeave"])],64)}var z=D(N,[["render",L]]);export{z as default};