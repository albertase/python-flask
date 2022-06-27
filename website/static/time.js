const time = document.querySelector('.list-groups')



// const now = new Date();

// const timestamp = now.getTime();
// const myDate = new Date(timestamp);
// console.log(myDate.getFullYear())

// time.innerText = myDate.getDay()

const now = moment()

console.log(now.toString())

now.minute(1)
console.log(now.toString())

now.add(1, "week").subtract(20, "days")
// now.add(1, "year").subtract(20, "days")
console.log(now.toString())
console.log(now.format('MMMM Do, YYYY'))
console.log(now.fromNow())

const nowTimeStamp = now.valueOf()

console.log(nowTimeStamp)
console.log(moment(nowTimeStamp).toString())




const getSavedNotes = function () {
    // CHECK FOR EXISTING SAVED DATA. TO GET IT
    const notesJSON = localStorage.getItem('note');

    try{
        if (notesJSON !== null) {
        return JSON.parse(notesJSON)
    }else{
        return [];
    }
    }catch (e) {
        return []
    }
    
}

// Save the notes to localStorage
const saveNotes = function (notes) {
    localStorage.setItem('note', JSON.stringify(notes));
}



let notes = getSavedNotes();



const button = document.getElementById('create-note')
    button.addEventListener('click', function(e) {
    const id = uuidv4() // NEW
    const timestamp = moment().valueOf()
    notes.push({
        // id: uuidv4()
        id: id,
        title: '',
        body: '',
        createdAt: timestamp,
        updatedAt: timestamp
    })
    saveNotes(notes)
        // renderNotes(notes, filters)
    location.assign(`/edit.html#${id}`)
})


const generateLastEdited = function (timestamp) {          // A FUNCTION OF MOMENT
    // return `Last visited: ${moment(timestamp).format("MMMM Do, YYYY, h:mm:ss a")}`
    return `Time visited: ${moment(timestamp).subtract(button, 'days').calendar()}`

}

time.textContent = generateLastEdited(notes.createdAt)

// fromNow()