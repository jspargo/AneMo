// Copyright 2016 - Jack Spargo
// Anemo Dashboard
//
// Built using React - https://facebook.github.io/
// Based on tutorial - https://facebook.github.io/react/tips/initial-ajax.html

var monthNames = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];

var TempReading = React.createClass({
  rawMarkup: function() {
    var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
    return { __html: rawMarkup };
  },
  render: function() {
    return (
      <div className="comment">
        <span dangerouslySetInnerHTML={this.rawMarkup()} />
      </div>
    );
  }
});

var ThermostatDisplay = React.createClass({
  timeForDisplay: function() {
    var hour = this.props.children[0].toString();
    var minute = this.props.children[1].toString();
    var timeStr = hour.concat(":", minute)
    return {__html: timeStr};
  },
  tempForDisplay: function() {
    var results = this.props.children[2];
    return {__html: results};  
  },
  render: function() {
    return (
      <div className="time">
        <p id="time" dangerouslySetInnerHTML={this.timeForDisplay()} />
        <p id="temp" dangerouslySetInnerHTML={this.tempForDisplay()} />
      </div>
    );
  }
});

var CommentBox = React.createClass({
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      type: 'GET',
      dataType: 'json',
      cache: false,
      success: function(data) {
        this.setState({data: data});
      }.bind(this),
      error: function(xhr, status, err) {
        console.error(this.props.url, status, err.toString());
      }.bind(this)
    });
  },
  getInitialState: function() {
    return {data: []};
  },
  componentDidMount: function() {
    this.loadCommentsFromServer();
    setInterval(this.loadCommentsFromServer, this.props.pollInterval);
  },
  render: function() {
    return (
      <div className="commentBox">
        <h1>AneMo</h1>
        <Thermostat data={this.state.data} />
        <h1>Data</h1>
        <Temp data={this.state.data} />
        <SetTempForm onCommentSubmit={this.handleTempChange} />
      </div>
    );
  }
});

var Thermostat = React.createClass({
  render: function() {
    var length = this.props.data.length - 1
    var tempNodes = this.props.data.map(function(temp) {
      var date = new Date((temp.recorded_date || "").replace(/-/g,"/").replace(/[TZ]/g," "))
      var hourStr = date.getHours()
      var minuteStr = date.getMinutes()

      return (
        <ThermostatDisplay recorded_date={temp.recorded_date} recorded_temp={temp.recorded_temp}>
          {hourStr}{minuteStr}{temp.recorded_temp}
        </ThermostatDisplay>
      );
    });
    return (
      <div className="commentList">
        {tempNodes[length]}
      </div>
    );
  }
});

var Temp = React.createClass({
  render: function() {
    var tempNodes = this.props.data.map(function(temp) {
      var date = new Date((temp.recorded_date || "").replace(/-/g,"/").replace(/[TZ]/g," "))
      return (
        <TempReading recorded_date={date} recorded_temp={temp.recorded_temp}>
          {date} - {temp.recorded_temp}
        </TempReading>
      );
    });
    return (
      <div className="commentList">
        {tempNodes}
      </div>
    );
  }
});

var SetTempForm = React.createClass({
  getInitialState: function() {
    return {recorded_temp: ''};
  },
  handleTempChange: function(e) {
    this.setState({recorded_temp: e.target.value});
  },
  render: function() {
    return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Set Temp"
          value={this.state.recorded_temp}
          onChange={this.handleTempChange}
        />
        <input type="submit" value="Post" />
      </form>
    );
  }
});

ReactDOM.render(
  <CommentBox url="http://52.19.110.248:8000/latest/" pollInterval={30000} />,
  document.getElementById('content')
);
