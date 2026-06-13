// The exact link to your local Django data stream
const API_URL = '/api/students/';

async function fetchStudents() {
    try {
        // 1. Send a request across the local network to Django
        const response = await fetch(API_URL);
        
        // 2. Parse the incoming text data into readable JavaScript objects
        const students = await response.json();
        
        // 3. Grab our HTML elements from index.html
        const grid = document.getElementById('student-grid');
        const countBadge = document.getElementById('student-count');
        
        // Update the counter text
        countBadge.innerText = `Total Registered Students: ${students.length}`;
        
        // Clear out any loading placeholders
        grid.innerHTML = '';
        
        // 4. Loop through the array of 100 students and construct HTML cards
        students.forEach(student => {
            const card = document.createElement('div');
            card.className = 'card';
            
            card.innerHTML = `
                <h3>👤 ${student.name}</h3>
                <p><strong>Reg No:</strong> ${student.reg_no}</p>
                <p><strong>Email:</strong> ${student.email}</p>
                <p><strong>Course:</strong> ${student.course || 'Information Technology'}</p>
            `;
            
            // Append the newly made card into the grid container
            grid.appendChild(card);
        });
        
    } catch (error) {
        console.error('Error fetching data:', error);
        document.getElementById('student-grid').innerHTML = `
            <p style="color: red; grid-column: 1/-1; text-align: center;">
                ❌ Failed to stream data. Make sure your Django server is running!
            </p>
        `;
    }
}

// Fire off the function the moment the page finishes loading
window.onload = fetchStudents;