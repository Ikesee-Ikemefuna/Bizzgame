const post=async(endpoint, form_data)=>{
    const fetch_data=await fetch("https://curly-waffle-q5vqpjgg75jc5jp-8000.app.github.dev/"+endpoint+".php", {
        method:"post",
        body:form_data
    }).catch(err=>alert(err));
    return await fetch_data.json();
}
// const post=async(endpoint, form_data)=>{
//     const fetch_data=await fetch("../../apis/"+endpoint+".php", {
//         method:"post",
//         body:form_data
//     }).catch(err=>alert(err));
//     return await fetch_data.json();
// }

const get=async(endpoint, params=null)=>{
    const url=params?endpoint+".php?"+params:endpoint+".php";
    const fetch_data=await fetch("../../apis/"+url).catch(err=>alert(err));
    return await fetch_data.json();
}


export {get, post};
