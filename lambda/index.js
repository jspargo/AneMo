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
      "STATE_MESSAGE" : "The current state is ",
      "OVERRIDE_MESSAGE_ON" : "OK, I'll turn the heating on for you. Just let me know if you need me to turn it off again",
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
    httpsGet((result) => {
      const speechOutput = this.t('TEMP_MESSAGE') + result + ' degrees';
      this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
    });
  },
  'GetState': function () {
    this.emit(':tell', this.t('STATE_MESSAGE'));
  },
  'SetState': function () {
    const speechOutput = this.t('OVERRIDE_MESSAGE_ON');
    this.emit(':tellWithCard', speechOutput, this.t('SKILL_NAME'), speechOutput);
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


// TEMP:

module.exports.testAlexa = function () {
  httpsPost(true, (result) => {
    console.log('Output: ' + result);
  });
  console.log('testing');
};


// 3. Helper Function  =================================================================================================

var https = require('https');
var querystring = require('querystring');

var options = {
   host: 'anemo.jackspargo.com/v2',
   port: 443,
   path: '/state/',
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
    // console.log(JSON.parse(data)[0].state_date);
    console.log(JSON.parse(data)[0].return_state);
  });

  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });
}

function httpsPost(bool, callback) {

  var postData = querystring.stringify({
    "state_date": new Date()
      .toISOString()
      .replace(/T/, ' ')
      .replace(/\..+/, ''),
    "override_state": bool
  });

  var postOptions = {
    method: 'POST',
    host: 'anemo.jackspargo.com',
    port: 443,
    path: '/state/',
    // authentication headers
    headers: {
      'Authorization': 'Basic ' + new Buffer('jack:spar87go').toString('base64'),
      'Content-Length': Buffer.byteLength(postData),
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  };

  console.log(postData);

  var req = https.request(postOptions, (resp) => {
  let data = '';

  // A chunk of data has been recieved.
  resp.on('data', (chunk) => {
    data += chunk;
  });

  // The whole response has been received. Print out the result.
  resp.on('end', () => {
    // console.log(JSON.parse(data)[0].state_date);
    console.log('statusCode:', resp.statusCode);
    console.log('headers:', resp.headers);
    console.log(JSON.parse(data)[0]);
  });

  }).on("error", (err) => {
    console.log("Error: " + err.message);
  });
  req.write(postData);
  req.end();
}
