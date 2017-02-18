#!/usr/local/bin/node

const _ = require('lodash')
const fs = require('fs')
const path = require('path')
const request = require('request')
const rp = require('request-promise')
const http = require('http')
const https = require('https')
const bodyParser = require('body-parser')

const username = process.env.ANEMO_REC_USER
const password = process.env.ANEMO_REC_PASSWORD

const localUrl = 'http://localhost:8000'
const remoteUrl = 'http://anemo.jackspargo.com'
const auth = "Basic " + new Buffer(username + ":" + password).toString("base64");

var getContent = new Promise((resolve, reject) => {
    // return new pending promise
    const url = remoteUrl + '/state'
    var options = {
      uri: url,
      headers: {
          'Authorization': auth
      },
      json: true // Automatically parses the JSON string in the response
    };

    rp(options).then((response) => {
      resolve(response)
    }).catch((err) => {
      reject(err)
      console.error(err)
    })
})

var currentdate = new Date();
var datetime = "[" + currentdate.getDate() + "/"
                + (currentdate.getMonth()+1)  + "/"
                + currentdate.getFullYear() + " @ "
                + currentdate.getHours() + ":"
                + currentdate.getMinutes() + ":"
                + currentdate.getSeconds() + "]";

var response = getContent
  .then((body) => {
    var stateBool = 0
    const data = body[0].return_state
    if (data === true) {
      console.log(datetime + ' - switching on')
      stateBool = 1
    } else {
      console.log(datetime + ' - switching off')
      stateBool = 0
    }
    var spawn = require("child_process").spawn;
    scriptPath = path.join(__dirname, '../setRelayState.py')
    var process = spawn('python',[scriptPath, stateBool]);
  })
  .catch((error) => console.log(error))
