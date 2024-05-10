let projectsUrl = "http://127.0.0.1:8000/api/projects"

// Takes project list from url and returns projects object
let getProjects = () => {

    fetch(projectsUrl)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        buildProjects(data)
    })
}

// Take and manipulate json projects object
let buildProjects = (projects) => {
    let projectsWrapper = document.getElementById('projects-wrapper')
    projectsWrapper.innerHTML = ''
    // Loop trough each project
    for (let i = 0; i < projects.length; i++) {
        let project = projects[i]

        // Create card for each project
        let projectCard = `
            <div class="project--card">
                <img src="http://127.0.0.1:8000${project.featured_image}" />
                
                <div>
                    <div class="card--header">
                        <h3>${project.title}</h3>
                        <strong class="vote--option" data-vote="up" data-project="${project.id}" >&#43;</strong>
                        <strong class="vote--option" data-vote="down" data-project="${project.id}"  >&#8722;</strong>
                    </div>
                    <i>${project.vote_ratio}% Positive feedback </i>
                    <p>${project.description.substring(0, 150)}</p>
                </div>
        
            </div>
        `

        projectsWrapper.innerHTML += projectCard
    }

    addVoteEvents()
    
}

// Add event listener to every button
let addVoteEvents = () => {
    let voteBtns = document.getElementsByClassName('vote--option')
    
    for (let i = 0; i < voteBtns.length; i++) {
        // On click do:
        voteBtns[i].addEventListener('click', (e)=> {
            let token = localStorage.getItem('token')
            console.log('TOKEN:', token)

            // Set vote as data-vote("up"/"down") and project as data-project(project.id).
            let vote = e.target.dataset.vote
            let project = e.target.dataset.project
            
            fetch(`http://127.0.0.1:8000/api/projects/${project}/vote/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    Authorization: `Bearer ${token}`
                },
                body: JSON.stringify({ 'value': vote })
            })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data)
                    getProjects() // call API and load in more projects
                })

        })
    }
}

getProjects()