"use strict";
function getName(u) {
    return `${u.firstName} ${u.lastName}`;
}
let userName = getName({ firstName: "Django", lastName: "Pipeline" });
