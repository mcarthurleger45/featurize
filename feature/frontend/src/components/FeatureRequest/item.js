import React, { Component } from 'react';
import PropTypes from 'prop-types';
import './item.css';

class FeatureRequest extends Component {
    constructor(props){
        super(props);
        this.state = {
        }
    }
    render(){
        return <div className='featureRequest-item'> {this.props.data.title}, actions: {this.props.showActions.toString()} </div>
    }
}

FeatureRequest.propTypes = {
    'showActions': PropTypes.bool.isRequired
}

export default FeatureRequest;
