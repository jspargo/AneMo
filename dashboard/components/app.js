import React from 'react';

export default class AppComponent extends React.Component {
	render() {
    	return (
      		<div>
        		<h2>Welcome to my App</h2>
        		{ this.props.children }
      		</div>
    	);
  	}
}
