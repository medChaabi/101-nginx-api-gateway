import  express  from "express";

const app = express();

app.get("/",(request,response)=>{
    response.json("Hi! From NodeJs :)");
})

app.listen(8001, () => console.log(`SSCAR FORUM API! run on 8001`));