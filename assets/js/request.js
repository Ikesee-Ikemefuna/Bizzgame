const post=async(endpoint, form_data)=>{
    const fetch_data=await fetch("https://ikesee-ikemefuna.github.io/Bizzgame/apis/"+endpoint+".php", {
        method:"post",
        body:form_data
    }).catch(err=>alert(err));
    return await fetch_data.json();
}

const get=async(endpoint, params=null)=>{
    const url=params?endpoint+".php?"+params:endpoint+".php";
    const fetch_data=await fetch("https://ikesee-ikemefuna.github.io/Bizzgame/apis/"+url).catch(err=>alert(err));
    return await fetch_data.json();
}


export {get, post};
