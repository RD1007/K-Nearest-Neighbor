import React from 'react';

export function App () {
    const handleMenuOne = () => {
        console.log('clicked one');
    };

    const handleMenuTwo = () => {
        console.log('clicked two');
    };

    return React.createElement(Dropdown, {
        trigger: React.createElement('button', null, 'Dropdown'),
        menu: [
            React.createElement('button', { onClick: handleMenuOne }, 'Menu 1'),
            React.createElement('button', { onClick: handleMenuTwo }, 'Menu 2')
        ]
    });
};

const Dropdown = ({ trigger, menu }) => {
    const [open, setOpen] = React.useState(false);

    const handleOpen = () => {
        setOpen(!open);
    };

    return React.createElement('div', { className: 'dropdown' },
        React.cloneElement(trigger, { onClick: handleOpen }),
        open ? React.createElement('ul', { className: 'menu' },
            menu.map((menuItem, index) =>
                React.createElement('li', { key: index, className: 'menu-item' },
                    React.cloneElement(menuItem, {
                        onClick: () => {
                            menuItem.props.onClick();
                            setOpen(false);
                        }
                    })
                )
            )
        ) : null
    );
};
