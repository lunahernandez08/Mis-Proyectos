// JavaScript del estudiante (usuario.js)
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
        const selectedDate = new Date(dateInput.value);
        const today = new Date();
        const threeDaysFromNow = new Date(today.setDate(today.getDate() + 3));
        today.setHours(0, 0, 0, 0); // Configura la hora a las 00:00 para comparación de solo fecha

        // Validar que la fecha seleccionada sea al menos 3 días en el futuro
        if (selectedDate < today) {
            alert('La fecha seleccionada no puede ser en el pasado.');
            dateInput.value = '';
            return;
        } else if (selectedDate < threeDaysFromNow && selectedDate > today) {
            alert('Las citas deben ser agendadas con al menos 3 días de anticipación.');
            dateInput.value = '';
            return;
        }

        // Validar que no haya más de 5 citas para la fecha seleccionada
        const appointmentsOnSameDay = appointments.filter(app => app.date === dateInput.value);
        if (appointmentsOnSameDay.length >= 5) {
            alert('No se pueden agendar más de 5 citas por día.');
            dateInput.value = '';
        }
    });

    appointmentForm.addEventListener('submit', (e) => {
        e.preventDefault();

        const name = document.getElementById('name').value;
        const phone = document.getElementById('phone').value;
        const email = document.getElementById('email').value;
        const location = document.getElementById('location').value;
        const date = document.getElementById('appointment-date').value;
        const time = document.getElementById('appointment-time').value;
        const reason = document.getElementById('reason').value;

        // Validar que no haya más de 5 citas para la fecha seleccionada
        const appointmentsOnSameDay = appointments.filter(app => app.date === date);
        if (appointmentsOnSameDay.length >= 5) {
            alert('No se pueden agendar más de 5 citas por día.');
            return;
        }

        // Validar que no haya otra cita a la misma hora en la misma fecha
        const sameDateAndTime = appointmentsOnSameDay.some(app => app.time === time);
        if (sameDateAndTime) {
            alert('Ya hay una cita programada a esta hora en este día. Por favor, elija otra hora.');
            return;
        }

        const appointment = {
            name,
            phone,
            email,
            location,
            date,
            time,
            reason,
            confirmed: false
        };

        appointments.push(appointment);
        localStorage.setItem('appointments', JSON.stringify(appointments));

        alert('Cita agendada con éxito.');
        appointmentForm.reset();
        personalInfo.style.display = 'block';
        appointmentInfo.style.display = 'none';
    });
});
