import React from 'react';
import $ from 'jquery';

export default class ApiAppComponent extends React.Component {
    render() {
    	// if (typeof this.state.someData !== 'undefined') {
    	// 	return <div>{this.state.someData}</div>
    	// }
		if (typeof this.props.someData !== 'undefined') {
    		return <div>{this.props.someData}</div>
    	}
    	return <div>Awaiting AJAX response</div>
  	}

  	// This method is always called, on the client, when the component has been
  	// rendered onto the DOM.
  	componentDidMount() {
    	$.get('http://52.19.110.248:8000/temp/').then(data => {
      		this.setState('someData', data);
    	});
  	}
}

// React.render(<ApiAppComponent />, document.getElementById('target'));