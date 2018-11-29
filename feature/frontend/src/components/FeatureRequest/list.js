import React, { Component } from 'react';
import { FEATURED_REQUEST_API } from '../../endpoints';
import FeatureRequest from './item';
import './list.css';
import PropTypes from 'prop-types';

class FeatureRequestList extends Component {
    constructor(props){
        super(props);
        this.state = {
            data: [],
        };
    }

    componentDidMount(){
        fetch(FEATURED_REQUEST_API)
            .then(response => response.json())
            .then(data => this.setState({ data }));
    }

    render(){
        const showActions = this.props.user != '';
        return (
            <div className='featureRequest-list'>
                { this.state.data.map((featureRequest, i) => <FeatureRequest data={featureRequest} key={i} showActions={showActions} /> ) }
            </div>
        )
    }
}

FeatureRequestList.propTypes = {
    user: PropTypes.string.isRequired,
};

export default FeatureRequestList;