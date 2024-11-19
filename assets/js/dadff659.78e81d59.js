"use strict";(self.webpackChunkwiki=self.webpackChunkwiki||[]).push([[5106],{2527:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>c,default:()=>u,frontMatter:()=>i,metadata:()=>o,toc:()=>d});var r=t(4848),s=t(8453);const i={title:"Currency Convertor"},c=void 0,o={id:"community-contributions/cc-sentences/currency-convertor",title:"Currency Convertor",description:"Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled.",source:"@site/docs/community-contributions/cc-sentences/currency-convertor.md",sourceDirName:"community-contributions/cc-sentences",slug:"/community-contributions/cc-sentences/currency-convertor",permalink:"/View-Assist/docs/community-contributions/cc-sentences/currency-convertor",draft:!1,unlisted:!1,tags:[],version:"current",frontMatter:{title:"Currency Convertor"},sidebar:"tutorialSidebar",previous:{title:"Calculations",permalink:"/View-Assist/docs/community-contributions/cc-sentences/conversions"},next:{title:"Extended Device Controls",permalink:"/View-Assist/docs/community-contributions/cc-sentences/extended-device-controls"}},l={},d=[{value:"Prequisites",id:"prequisites",level:2},{value:"Pyscript",id:"pyscript",level:3},{value:"Intent Script",id:"intent-script",level:3},{value:"Custom Sentences",id:"custom-sentences",level:3},{value:"Rapid API Key",id:"rapid-api-key",level:2},{value:"Changelog",id:"changelog",level:2}];function a(e){const n={a:"a",blockquote:"blockquote",br:"br",code:"code",h2:"h2",h3:"h3",img:"img",li:"li",p:"p",pre:"pre",strong:"strong",table:"table",tbody:"tbody",td:"td",th:"th",thead:"thead",tr:"tr",ul:"ul",...(0,s.R)(),...e.components};return(0,r.jsxs)(r.Fragment,{children:[(0,r.jsx)(n.p,{children:(0,r.jsx)(n.a,{href:"https://my.home-assistant.io/redirect/blueprint_import/?blueprint_url=https%3A%2F%2Fraw.githubusercontent.com%2Fdinki%2FView-Assist%2Frefs%2Fheads%2Fmain%2FView_Assist_custom_sentences%2Fcommunity_contributions%2FCurrency_Convertor%2Fblueprint-currencyconvertor.yaml",children:(0,r.jsx)(n.img,{src:"https://my.home-assistant.io/badges/blueprint_import.svg",alt:"Open your Home Assistant instance and show the blueprint import dialog with a specific blueprint pre-filled."})})}),"\n",(0,r.jsx)(n.h2,{id:"prequisites",children:"Prequisites"}),"\n",(0,r.jsx)(n.h3,{id:"pyscript",children:"Pyscript"}),"\n",(0,r.jsxs)(n.p,{children:["You must have Pyscript installed ",(0,r.jsx)(n.a,{href:"https://www.youtube.com/watch?v=jpJxZaisbGQ",children:"See installation video"})]}),"\n",(0,r.jsxs)(n.p,{children:["Download these from the ",(0,r.jsx)(n.a,{href:"https://github.com/dinki/View-Assist/tree/main/View_Assist_custom_sentences/community_contributions/Currency_Convertor",children:"currency convertor GH page"})]}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsx)(n.li,{children:"viewassist-currencyconvertor.py"}),"\n",(0,r.jsx)(n.li,{children:"viewassist-response_handler.py"}),"\n",(0,r.jsx)(n.li,{children:"viewassist_currencyconvertor_digits.yaml"}),"\n"]}),"\n",(0,r.jsxs)(n.p,{children:["and place this files in your ",(0,r.jsx)(n.strong,{children:"pyscripts"})," directory on your Home Assistant server. ",(0,r.jsx)(n.br,{}),"\n","The pyscript variables ",(0,r.jsx)(n.strong,{children:"hass_all_imports"})," and ",(0,r.jsx)(n.strong,{children:"hass_is_global"})," need to be set to true. This can be done in the UI or via an entry"]}),"\n",(0,r.jsx)(n.pre,{children:(0,r.jsx)(n.code,{children:"pyscript:\n  allow_all_imports: true\n  hass_is_global: true\n"})}),"\n",(0,r.jsxs)(n.p,{children:["in ",(0,r.jsx)(n.strong,{children:"configuration.yaml"}),"."]}),"\n",(0,r.jsx)(n.h3,{id:"intent-script",children:"Intent Script"}),"\n",(0,r.jsxs)(n.p,{children:["If not exist create a directory ",(0,r.jsx)(n.strong,{children:"intent_script"})," in your 'config' directory on your Home Assistant server. ",(0,r.jsx)(n.br,{}),"\n","Download"]}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsx)(n.li,{children:"viewassist_currenyconvertor.intent.yaml"}),"\n"]}),"\n",(0,r.jsxs)(n.p,{children:["and place it in this 'intent_script' directory. ",(0,r.jsx)(n.br,{}),"\n","The 'intent_script' directory must be accessed via the entry"]}),"\n",(0,r.jsxs)(n.blockquote,{children:["\n",(0,r.jsx)(n.p,{children:"intent_script: !include_dir_merge_named intent_script/"}),"\n"]}),"\n",(0,r.jsxs)(n.p,{children:["in ",(0,r.jsx)(n.strong,{children:"configuration.yaml"}),"."]}),"\n",(0,r.jsx)(n.h3,{id:"custom-sentences",children:"Custom Sentences"}),"\n",(0,r.jsxs)(n.p,{children:["If not exist create a directory ",(0,r.jsx)(n.strong,{children:"custom_sentences"})," in your 'config' directory on your Home Assistant server. ",(0,r.jsx)(n.br,{}),"\n","If not exist create your preferred ",(0,r.jsx)(n.strong,{children:"language directory"})," (esp. 'en') in this 'custom_sentences' directory. ",(0,r.jsx)(n.br,{}),"\n","Download the"]}),"\n",(0,r.jsxs)(n.ul,{children:["\n",(0,r.jsx)(n.li,{children:"viewassist_currencyconvertor_intent.yaml"}),"\n",(0,r.jsx)(n.li,{children:"viewassist_currencyconvertor_response.yaml"}),"\n",(0,r.jsx)(n.li,{children:"viewassist_currencyconvertor_currencies.yaml"}),"\n"]}),"\n",(0,r.jsx)(n.p,{children:"files from your preferred language directory (esp. 'en') and place this files in the corresponding language directory on your Home Assistant server."}),"\n",(0,r.jsx)(n.h2,{id:"rapid-api-key",children:"Rapid API Key"}),"\n",(0,r.jsxs)(n.p,{children:["You must get an API key from ",(0,r.jsx)(n.strong,{children:"rapidapi.com"})," for the ",(0,r.jsx)(n.a,{href:"https://rapidapi.com/pwshub-pwshub-default/api/crypto-market-prices",children:"required API"})," (totally free no credit card needed) ",(0,r.jsx)(n.br,{}),"\n","You must add your API key to the 'rapidapikey' field in the blueprint."]}),"\n",(0,r.jsx)(n.h2,{id:"changelog",children:"Changelog"}),"\n",(0,r.jsxs)(n.table,{children:[(0,r.jsx)(n.thead,{children:(0,r.jsxs)(n.tr,{children:[(0,r.jsx)(n.th,{children:"Version"}),(0,r.jsx)(n.th,{children:"Description"})]})}),(0,r.jsx)(n.tbody,{children:(0,r.jsxs)(n.tr,{children:[(0,r.jsx)(n.td,{children:"v 1.0.0"}),(0,r.jsx)(n.td,{children:"Initial release"})]})})]})]})}function u(e={}){const{wrapper:n}={...(0,s.R)(),...e.components};return n?(0,r.jsx)(n,{...e,children:(0,r.jsx)(a,{...e})}):a(e)}},8453:(e,n,t)=>{t.d(n,{R:()=>c,x:()=>o});var r=t(6540);const s={},i=r.createContext(s);function c(e){const n=r.useContext(i);return r.useMemo((function(){return"function"==typeof e?e(n):{...n,...e}}),[n,e])}function o(e){let n;return n=e.disableParentContext?"function"==typeof e.components?e.components(s):e.components||s:c(e.components),r.createElement(i.Provider,{value:n},e.children)}}}]);