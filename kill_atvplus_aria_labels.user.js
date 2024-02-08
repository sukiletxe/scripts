// ==UserScript==
// @name         Kill aria labels in Apple TV+
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Removes useless aria labels from Apple TV+
// @author       Sukil Etxenike
// @match        https://tv.apple.com/*
// @icon         data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==
// @grant        none
// ==/UserScript==

(function() {
    'use strict';
    // The only reason I use setInterval is because the onreadystatechange event doesn't seem to work. Ideas for improvements welcome.
    setInterval(()=> {
        document.querySelectorAll("a>h2").forEach((item) => item.parentElement.removeAttribute("aria-label"));
        document.getElementsByTagName("amp-locale-switcher")[0].shadowRoot.querySelectorAll(".button-container>ul>li>a").forEach((item)=> item.removeAttribute("aria-label"));
    }, 5000);
})();
