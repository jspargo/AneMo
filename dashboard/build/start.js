var HelloWorld = React.createClass({
  displayName: "HelloWorld",

  render: function () {
    return React.createElement(
      "p",
      null,
      "Hello, ",
      React.createElement("input", { type: "text", placeholder: "Your name here" }),
      "! It is ",
      this.props.date.toTimeString()
    );
  }
});

setInterval(function () {
  ReactDOM.render(React.createElement(HelloWorld, { date: new Date() }), document.getElementById('example'));
}, 500);