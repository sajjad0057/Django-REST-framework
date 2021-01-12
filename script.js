let myImage= null


document.getElementById('image').addEventListener('change',(e)=>{
    myImage = e.target.files[0]
    console.log("myImage----> :",myImage);
})

document.getElementById('myForm').addEventListener('submit',(e)=>{
    e.preventDefault();
    let user = document.getElementById('user').value 
    let content = document.getElementById('content').value
    let form_data = new FormData();   // Here The FormData() class constructor creates a new FormData object.
    form_data.append('user',user)
    form_data.append('content',content)
    form_data.append('image',myImage)

    // for (let [key,value] of form_data){
    //     console.log(key ," : ",value)
    // }

    axios.delete("http://127.0.0.1:8000/apiV1/status/57/",{
        header : {
            "Content-Type" : "application/json"
        }
    })
    .then(res=>console.log(res))
    // .then(data=>console.log("data--->",data))

})

