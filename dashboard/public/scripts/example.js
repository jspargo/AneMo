// Copyright 2016 - Jack Spargo
// Anemo Dashboard
//
// Built using React - https://facebook.github.io/
// Based on tutorial - https://facebook.github.io/react/tips/initial-ajax.html


var TempReading = React.createClass({
  rawMarkup: function() {
    var rawMarkup = marked(this.props.children.toString(), {sanitize: true});
    return { __html: rawMarkup };
  },

  render: function() {
    return (
      <div className="comment">
        <h2 className="commentAuthor">
          {this.props.author}
        </h2>
        <span dangerouslySetInnerHTML={this.rawMarkup()} />
      </div>
    );
  }
});

var CommentBox = React.createClass({
  loadCommentsFromServer: function() {
    $.ajax({
      url: this.props.url,
      type: 'GET',
      username: 'dashboard',
      password: 'D4shb0ard',
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
        <CommentList data={this.state.data} />
        <CommentForm onCommentSubmit={this.handleCommentSubmit} />
      </div>
    );
  }
});

//var FormattedDate = ReactIntl.FormattedDate;

var CommentList = React.createClass({
  render: function() {
    var commentNodes = this.props.data.map(function(temp) {
      return (
        <TempReading recorded_date={temp.recorded_date} recorded_temp={temp.recorded_temp}>
          {temp.recorded_date} - {temp.recorded_temp}
        </TempReading>
      );
    });
    return (
      <div className="commentList">
        {commentNodes}
      </div>
    );
  }
});

var CommentForm = React.createClass({
  getInitialState: function() {
    return {author: ''};
  },
  handleAuthorChange: function(e) {
    this.setState({author: e.target.value});
  },
  render: function() {
    return (
      <form className="commentForm" onSubmit={this.handleSubmit}>
        <input
          type="text"
          placeholder="Set Temp"
          value={this.state.author}
          onChange={this.handleAuthorChange}
        />
        <input type="submit" value="Post" />
      </form>
    );
  }
});

ReactDOM.render(
  <CommentBox url="http://52.19.110.248:8000/temp/" pollInterval={10000} />,
  document.getElementById('content')
);
