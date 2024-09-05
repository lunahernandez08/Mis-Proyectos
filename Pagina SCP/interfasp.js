// JavaScript del psicólogo (psicologa.js)
document.addEventListener('DOMContentLoaded', () => {
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];
    const appointmentsTableBody = document.querySelector('#appointments-table tbody');
    const editModal = document.getElementById('edit-modal');
    const editForm = document.getElementById('edit-form');
    const editDateInput = document.getElementById('edit-date');
    const editTimeSelect = document.getElementById('edit-time');
    const closeModalButton = document.getElementById('close-modal');
    let selectedAppointmentIndex = null;

    const renderAppointments = () => {
        appointmentsTableBody.innerHTML = '';

        appointments.forEach((appointment, index) => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${appointment.name}</td>
                <td>${appointment.phone}</td>
                <td>${appointment.email}</td>
                <td>${appointment.location}</td>
                <td>${appointment.date}</td>
                <td>${appointment.time}</td>
                <td>${appointment.reason}</td>
                <td>${appointment.confirmed ? 'Confirmada' : 'Pendiente'}</td>
                <td>
                    <button onclick="confirmAppointment(${index})">Confirmar</button>
                    <button onclick="editAppointment(${index})">Editar</button>
                    <button onclick="deleteAppointment(${index})">Eliminar</button>
                </td>
            `;
            appointmentsTableBody.appendChild(row);
        });
    };

    window.confirmAppointment = (index) => {
        appointments[index].confirmed = true;
        localStorage.setItem('appointments', JSON.stringify(appointments));
        renderAppointments();
    };

    window.editAppointment = (index) => {
        selectedAppointmentIndex = index;
        const appointment = appointments[index];
        editDateInput.value = appointment.date;
        editTimeSelect.value = appointment.time;
        editModal.style.display = 'block';
    };

    editForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const newDate = editDateInput.value;
        const newTime = editTimeSelect.value;
        const today = new Date();
        const threeDaysFromNow = new Date(today.setDate(today.getDate() + 3));
        const selectedDate = new Date(newDate);

        // Validar que la nueva fecha sea al menos 3 días en el futuro
        if (selectedDate < threeDaysFromNow) {
            alert('Las citas deben ser reprogramadas con al menos 3 días de anticipación.');
            return;
        }

        // Validar que no haya más de 5 citas para la nueva fecha
        const appointmentsOnSameDay = appointments.filter(app => app.date === newDate);
        if (appointmentsOnSameDay.length >= 5) {
            alert('No se pueden agendar más de 5 citas por día.');
            return;
        }

        // Validar que no haya otra cita a la misma hora en la nueva fecha
        const sameDateAndTime = appointmentsOnSameDay.some(app => app.time === newTime && app !== appointments[selectedAppointmentIndex]);
        if (sameDateAndTime) {
            alert('Ya hay una cita programada a esta hora en este día. Por favor, elija otra hora.');
            return;
        }

        appointments[selectedAppointmentIndex].date = newDate;
        appointments[selectedAppointmentIndex].time = newTime;

        localStorage.setItem('appointments', JSON.stringify(appointments));
        renderAppointments();
        editModal.style.display = 'none';
    });

    closeModalButton.addEventListener('click', () => {
        editModal.style.display = 'none';
    });

    window.deleteAppointment = (index) => {
        appointments.splice(index, 1);
        localStorage.setItem('appointments', JSON.stringify(appointments));
        renderAppointments();
    };

    renderAppointments();
});
