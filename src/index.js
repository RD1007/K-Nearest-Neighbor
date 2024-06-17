// import './styles.css';
import React from 'react';
import { createRoot } from 'react-dom/client';
import { Comments, Navigation } from './Components.js';
import { App } from './button.js'

const navDomNode = document.getElementById('navigation');
if (navDomNode) {
    const navRoot = createRoot(navDomNode);
    navRoot.render(<Navigation />);
}

const commentDomNode = document.getElementById('comments');
if (commentDomNode) {
    const commentRoot = createRoot(commentDomNode);
    commentRoot.render(<Comments />);
}

const buttonDomNode = document.getElementById('button');
if (buttonDomNode) {
    const buttonRoot = createRoot(buttonDomNode);
    buttonRoot.render(<App />);
}

if (module.hot) {
    module.hot.accept('./Components.js', () => {
        const NextNavigation = require('./Components.js').Navigation;
        const NextComments = require('./Components.js').Comments;
        if (navDomNode) {
            navRoot.render(<NextNavigation />);
        }
        if (commentDomNode) {
            commentRoot.render(<NextComments />);
        }
    });

    module.hot.accept('./button.js', () => {
        const NextApp = require('./button.js').App;
        if (buttonDomNode) {
            buttonRoot.render(<NextApp />);
        }
    });
}