// GET Request :

// axios.get("http://127.0.0.1:8000/apiV1/status/")
// .then(res=>console.log(res))
// .catch(err=>console.log(err.message))


//  Detail Request :

// axios.get("http://127.0.0.1:8000/apiV1/status/detail/53/")
// .then(res=>console.log(res))
// .catch(err=>console.log(err.message))







// POST request :
// let postData = {
//     user: 4,
//     content: "I am POSTED DATA 1",
//     image: null
// }

// axios.post("http://127.0.0.1:8000/apiV1/status/create/",postData,{
//     headers : {
//         "Content-Type" : "application/json"
//     }
// })
// .then(res=>console.log(res))
// .catch(err=>console.log(err.message))






// Delete Request :

// axios.delete("http://127.0.0.1:8000/apiV1/status/delete/52/")
// .then(res=>console.log(res))
// .catch(err=>console.log(err.message))





// PUT or PATCH Request for update data :
let updateData = {

    content: "I am Updated data using patch 1",

}
axios.patch("http://127.0.0.1:8000/apiV1/status/update/8/",updateData,{
    headers : {
        "Content-Type" : "application/json"
    }
})
.then(res=>console.log(res))
.catch(err=>console.log(err.message))