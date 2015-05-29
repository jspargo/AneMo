/**
 * Sample React Native App
 * https://github.com/facebook/react-native
 */
'use strict';

var React = require('react-native');

var {
  AppRegistry,
  StyleSheet,
  Text,
  Image,
  View,
} = React;

var AneMoApp = React.createClass({
  render: function() {
    return (
      <View style={styles.container}>
        <Text style={styles.welcome}>
          Current Temperature
        </Text>
        <Text style={styles.instructions}>
          20.5
        </Text>
      </View>
    );
  }
});

var styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#000000',
  },
  welcome: {
    fontSize: 20,
    textAlign: 'center',
    margin: 8,
    color: '#FFFFFF',
  },
  instructions: {
    fontSize: 32,
    textAlign: 'center',
    color: '#EEEEEE',
    marginBottom: 5,
  },
});

AppRegistry.registerComponent('AneMoApp', () => AneMoApp);
