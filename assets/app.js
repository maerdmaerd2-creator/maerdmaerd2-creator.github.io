'use strict';
(function(){
  const button=document.getElementById('copyReply');
  const status=document.getElementById('copyStatus');
  if(!button||!status)return;
  button.addEventListener('click',async()=>{
    const value='WR-001';
    try{
      if(!navigator.clipboard || !window.isSecureContext) throw new Error('Clipboard unavailable');
      await navigator.clipboard.writeText(value);
      status.textContent='REPLY KEY COPIED: WR-001';
    }catch(_error){
      status.textContent='REPLY KEY: WR-001 — select and copy this text.';
    }
  });
})();

(function(){
  const form=document.getElementById('doorForm');
  if(!form)return;
  const input=document.getElementById('doorAnswer');
  const hint=document.getElementById('doorHint');
  form.addEventListener('submit',function(event){
    event.preventDefault();
    const candidate=(input.value||'').trim().toLowerCase().replace(/[^a-z]/g,'');
    if(candidate==='stranger'){
      const path=location.pathname.replace(/(?:index\.html)?$/, '').replace(/\/door\/$/, '/');
      const target=(path.endsWith('/door/')?path:path+'door/')+'stranger/';
      location.assign(target);
    }else{
      hint.textContent='No. Look for the exact word immediately before “not smaller” in the first sentence under holdsTo.';
      input.focus();
    }
  });
})();
