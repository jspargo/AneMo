/* eslint-disable  func-names */
/* eslint quote-props: ["error", "consistent"]*/

'use strict';

const Alexa = require('alexa-sdk');

const APP_ID = "amzn1.ask.skill.13992e94-a5a6-4cc0-a098-c0f97611a367";

var languageStrings = {
  "en": {
    "translation": {
      "SKILL_NAME" : "Anemo Thermostat",
      "TEMP_MESSAGE" : "The current temperature is ",
      "STATE_MESSAGE" : "The heating is currently ",
      "OVERRIDE_MESSAGE_ON_1" : "OK, I'll turn the heating on for you for ",
      "OVERRIDE_MESSAGE_ON_2" : " minutes. Just let me know if you need me to turn it off again",
      "OVERRIDE_MESSAGE_OFF" : "No problem. I've turned the heating off for you",
      "HELP_MESSAGE" : "You can ask me what the current temperature is, or override the heating now, if you're cold.",
      "HELP_REPROMPT" : "What can I help you with?",
      "STOP_MESSAGE" : "Goodbye!"
    }
  }
};

const handlers = {
  'LaunchRequest': function () {
    const speechOutput = this.t('HELP_MESSAGE');
    const reprompt = this.t('HELP_REPROMPT');
    this.emit(':ask', speechOutput, reprompt);
  },
  'GetTemperature': function () {
    httpsGet((response) => {
      const speechOutput = this.t('TEMP_MESSAGE') + response[0].recorded_temp + ' degrees';
      this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
    });
  },
  'GetState': function () {
    httpsGet((response) => {
      var stateString
      if (response[0].return_state == true) {
        stateString = "on"
      } else {
        stateString = "off"
      }
      const speechOutput = this.t('STATE_MESSAGE') + stateString;
      this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
    });
  },
  'SetStateOn': function () {
    let seconds = toSeconds(this.event.request.intent.slots.Duration.value);
    let minutes = seconds / 60
    httpsPost('on', seconds.toString(), (response) => {
      const speechOutput = this.t('OVERRIDE_MESSAGE_ON_1') + minutes.toString() + this.t('OVERRIDE_MESSAGE_ON_2');
      this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
    });
  },
  'SetStateOff': function () {
    httpsPost('off', '3600', (response) => {
      const speechOutput = this.t('OVERRIDE_MESSAGE_OFF');
      this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
    });
  },
  'AMAZON.HelpIntent': function () {
    const speechOutput = this.t('HELP_MESSAGE');
    const reprompt = this.t('HELP_MESSAGE');
    this.emit(':ask', speechOutput, reprompt);
  },
  'AMAZON.CancelIntent': function () {
    this.emit(':tell', this.t('STOP_MESSAGE'));
  },
  'AMAZON.StopIntent': function () {
    this.emit(':tell', this.t('STOP_MESSAGE'));
  },
  'SessionEndedRequest': function () {
    this.emit(':tell', this.t('STOP_MESSAGE'));
  },
  'Unhandled': function () {
    this.emit(':tell', this.t('HELP_MESSAGE'));
  }
};

exports.handler = (event, context) => {
  const alexa = Alexa.handler(event, context);
  alexa.APP_ID = APP_ID;
  // To enable string internationalization (i18n) features, set a resources object.
  alexa.resources = languageStrings;
  alexa.registerHandlers(handlers);
  alexa.execute();
};


// Networking Function  =================================================================================================

var https = require('https');
var querystring = require('querystring');

var options = {
   host: 'anemo.jackspargo.com',
   port: 443,
   path: '/v2/state',
   // authentication headers
   headers: {
      'x-api-key': process.env.API_KEY
   }
};

function httpsGet(callback) {
  https.get(options, (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    callback(JSON.parse(data));
  });

  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });
}

function httpsPost(state, duration, callback) {
  var postOptions = options;
  postOptions.method = 'PUT';
  postOptions.path = '/v2/state?override=' + state + '&duration=' + duration

  var req = https.request(postOptions, function(res) {
    res.setEncoding('utf8');
    res.on('data', function (chunk) {
      console.log('BODY: ' + chunk);
      callback(JSON.parse(chunk));
    });
  });

  req.on('error', function(e) {
    console.log('problem with request: ' + e.message);
  });

  // write data to request body
  req.write('data\n');
  req.write('data\n');
  req.end();
}

function toSeconds(durationValue) {
  let arr = durationValue.split(/(\d+)/);
  var mins = arr[arr.length - 2];
  var hours = 0
  if (arr.length > 3 ) {
    hours = arr[arr.length - 4];
  }
  return (hours * 3600) + (mins * 60);
}
