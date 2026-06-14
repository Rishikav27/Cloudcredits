const API_URL =
"https://6o9om9sori.execute-api.us-east-1.amazonaws.com/tasks";



// ADD TASK FUNCTION

async function addTask(){

    console.log("Add button clicked");


    let taskName =
    document.getElementById("taskName").value;


    let description =
    document.getElementById("description").value;



    if(taskName === "" || description === ""){

        alert("Please enter task name and description");
        return;

    }



    try{


        let response = await fetch(API_URL, {


            method:"POST",


            headers:{

                "Content-Type":"application/json"

            },


            body:JSON.stringify({


                taskName:taskName,

                description:description


            })


        });



        let data =
        await response.json();


        console.log(data);


        alert(data.message);



        document.getElementById("taskName").value="";
        document.getElementById("description").value="";


        loadTasks();


    }


    catch(error){


        console.log(error);


        alert("Error while adding task");


    }


}





// LOAD TASKS FUNCTION

async function loadTasks(){


    let response =
    await fetch(API_URL);


    let tasks =
    await response.json();


    console.log(tasks);



    let taskList =
    document.getElementById("taskList");


    taskList.innerHTML="";



    tasks.forEach(task=>{


        taskList.innerHTML += `


        <div class="task">


            <h3>${task.taskName}</h3>


            <p>${task.description}</p>



            <button 
            class="delete"
            onclick="deleteTask('${task.id}')">

            Delete

            </button>



        </div>


        `;


    });


}





// DELETE TASK FUNCTION

async function deleteTask(id){



    await fetch(API_URL, {


        method:"DELETE",


        headers:{


            "Content-Type":"application/json"


        },


        body:JSON.stringify({


            id:id


        })


    });



    alert("Task Deleted Successfully");


    loadTasks();


}




loadTasks();