document.addEventListener('DOMContentLoaded', () => {
    const continueButton = document.getElementById('continue-button');
    const personalInfo = document.getElementById('personal-info');
    const appointmentInfo = document.getElementById('appointment-info');
    const personalInfoForm = document.querySelector('.personal-info');
    const appointmentForm = document.getElementById('appointment-form');
    const dateInput = document.getElementById('appointment-date');
    const appointments = JSON.parse(localStorage.getItem('appointments')) || [];

    continueButton.addEventListener('click', () => {
        if (personalInfoForm.checkValidity()) {
            personalInfo.style.display = 'none';
            appointmentInfo.style.display = 'block';
        } else {
            personalInfoForm.reportValidity();
        }
    });

    dateInput.addEventListener('input', () => {
        const selectedDate = dateInput.value;
        const isDateTaken = appointments.some(app => app.date === selectedDate);
        if (isDateTaken) {
            alert('Esta fecha ya no está disponible. Por favor, selecciona otra.');
            dateInput.value = '';
        }
    });

    appointmentForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const name = document.getElementById('full-name').value;
        const phone = document.getElementById('phone-number').value;
        const email = document.getElementById('email').value;
        const location = document.getElementById('location').value;
        const date = document.getElementById('appointment-date').value;
        const time = document.getElementById('appointment-time').value;
        
        const newAppointment = { name, phone, email, location, date, time };
        appointments.push(newAppointment);
        localStorage.setItem('appointments', JSON.stringify(appointments));
        
        personalInfoForm.reset();
        appointmentForm.reset();
        personalInfo.style.display = 'block';
        appointmentInfo.style.display = 'none';
        alert('Cita agendada exitosamente');
    });
});
