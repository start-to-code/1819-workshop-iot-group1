/*
Start 2 Code
============
Workshop: Internet of Things
Application: Ambilight
Description: 
  - Change the RGBMatrix on the RaspberryPi via Firestore
  - Input-fields: color and switch
  - Listen to updates in the corresponding Firestore document (and update the UI)
Technology:
  - HTML
  - CSS
    - Libraries:
      - fontawesome
  - JavaScript
    - Libraries:
      - firebasejs
Cloud:
  - Firestore (Firebase)
*/

'use strict'

/*
Configuration
-------------
...
example:

pi_id: stc_pi_1 ... stc_pi_10

use stc_pi_1 for Raspberry Pi: pi-nmd-iot-1
use stc_pi_10 for Raspberry Pi: pi-nmd-iot-10

student: {
  firstName: 'Philippe',
  lastName: 'De Pauw - Waterschoot'
}
*/
const config = {
  firebase: {
    apiKey: 'AIzaSyAb_oy301KscmyVEypq_3zvmZT-jABqG6I',
    authDomain: 'start-to-code.firebaseapp.com',
    databaseURL: 'https://start-to-code.firebaseio.com',
    projectId: 'start-to-code',
    storageBucket: 'start-to-code.appspot.com',
    messagingSenderId: '659804621253',
  },
  pis_collection_name: 'pis',
  pi_id: '...',
  student: {
    firstName: '...',
    lastName: '...'
  }
}

;((window) => {
  const app = {
    init() {
    }
  }

  // Initalize application
  app.init()
})(window)