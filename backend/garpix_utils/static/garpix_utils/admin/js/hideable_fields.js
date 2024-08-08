const initFields = (visibleFields) => {
    Object.entries(visibleFields).forEach(([index, elements]) => {
        for (let i = 0; i < elements.length; i++) {
            const field = getField(elements[i]);
            if (field) {
                visibleFields[index][i] = field;
            }
        }
    });

    return new Set([].concat(...Object.values(visibleFields)));
}

const getField = (name) => {
    return document.querySelector(`.field-${name}`);
}

const toggleFields = (type, allFields, visibleFields) => {
    if (!(type in visibleFields)) {
        allFields.forEach(el => {
            el.style.display = 'none';
        });

        return;
    }

    allFields.forEach(el => {
        el.style.display = 'none'
    });
    visibleFields[type].forEach(el => {
        el.style.display = ''
    });
}

window.initHideableFields = (visibleFields, input) => {
    if (!visibleFields) {
        return;
    }

    input = document.querySelector(`#id_${input}`);
    if (!input) {
        return;
    }

    const allFields = initFields(visibleFields);
    if (input instanceof HTMLSelectElement) {
        input.addEventListener('change', (event) => {
            toggleFields(event.currentTarget.value, allFields, visibleFields);
        });
    } else if (input instanceof HTMLInputElement && input.type === 'checkbox') {
        input.addEventListener('change', (event) => {
            const value = event.currentTarget.checked ? 'on' : 'off';
            toggleFields(value, allFields, visibleFields);
        });
    }

    input.dispatchEvent(new CustomEvent('change'));
}
