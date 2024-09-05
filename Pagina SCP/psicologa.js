document.addEventListener('DOMContentLoaded', () => {
    const appointmentsTable = document.getElementById('appointments-table').querySelector('tbody');
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];

    const renderAppointments = () => {
        appointmentsTable.innerHTML = '';
        appointments.forEach(appointment => {
            const row = appointmentsTable.insertRow();
            row.insertCell(0).textContent = appointment.name;
            row.insertCell(1).textContent = appointment.phone;
            row.insertCell(2).textContent = appointment.email;
            row.insertCell(3).textContent = appointment.location;
            row.insertCell(4).textContent = appointment.date;
            row.insertCell(5).textContent = appointment.time;
        });
    };
    
    renderAppointments();
});
